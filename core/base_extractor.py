"""
Clase base del extractor que orquesta todos los módulos
"""
import logging
import traceback
from httpcore import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.driver_manager import DriverManager
from modules import (
    AuthenticationModule,
    NavigationModule,
    DataExtractionModule,
    ExportHandler
)
from utils.selectors import TABLA_SELECTOR, FILAS_DATOS_SELECTOR
from utils.helpers import generar_nombre_archivo


class ExtractorDatosEmpresa:
    """
    Clase principal que orquesta todo el proceso de extracción
    """
    
    def __init__(self):
        self.driver_manager = DriverManager()
        self.auth_module = None
        self.navigation_module = None
        self.extraction_module = None
    
    def inicializar_modulos(self):
        """Inicializa todos los módulos necesarios"""
        driver = self.driver_manager.obtener_driver()
        wait = self.driver_manager.obtener_wait()
        
        self.auth_module = AuthenticationModule(driver, wait)
        self.navigation_module = NavigationModule(driver, wait)
        self.extraction_module = DataExtractionModule(driver, wait)
    
    def ejecutar_proceso_completo(self, municipios, url_login):
        """
        Ejecuta el proceso completo de extracción para múltiples municipios
        
        Args:
            municipios: Lista de municipios a procesar
            url_login: URL de la página de login
            
        Returns:
            dict: SIEMPRE retorna un diccionario con resultados detallados
        """
        try:
            print("Iniciando proceso de extracción de datos...")
            
            # Configurar driver
            if not self.driver_manager.configurar_driver():
                self.resultados["exitoso"] = False
                self.resultados["errores"].append("Error al configurar el driver")
                return self.resultados  # ← Retorna dict
            
            # Inicializar módulos
            self.inicializar_modulos()
            
            # Realizar login
            if not self.auth_module.realizar_login(url_login):
                self.resultados["exitoso"] = False
                self.resultados["errores"].append("Error en autenticación")
                return self.resultados  # ← Retorna dict
            
            # Navegar a empresas (primera vez)
            if not self.navigation_module.navegar_a_empresas():
                self.resultados["exitoso"] = False
                self.resultados["errores"].append("Error al navegar a empresas")
                return self.resultados  # ← Retorna dict
            
            # Procesar cada municipio
            for municipio in municipios:
                self._procesar_municipio(municipio)
            
            print("Proceso completado exitosamente!")
            return self.resultados  # ← Retorna dict
            
        except Exception as e:
            logging.error(f"Error en proceso completo: {str(e)}")
            print(f"Error en el proceso: {str(e)}")
            traceback.print_exc()
            self.resultados["exitoso"] = False
            self.resultados["errores"].append(str(e))
            return self.resultados  # ← Retorna dict
            
        finally:
            self.driver_manager.cerrar_driver()
    
    def _procesar_municipio(self, municipio):
        """
        Procesa un municipio específico
        
        Args:
            municipio: Nombre del municipio a procesar
        """
        try:
            print(f"\n--- Procesando datos para el municipio: {municipio} ---")
            
            # Limpiar datos previos
            self.extraction_module.limpiar_datos()
            
            # Hacer búsqueda avanzada
            if not self.navigation_module.hacer_consulta_avanzada(municipio):
                print(f"Saltando el municipio {municipio} debido a error en búsqueda")
                return
            
            # Esperar y extraer datos
            if self._esperar_y_extraer_datos(municipio):
                self._exportar_datos(municipio)
            
        except Exception as e:
            logging.error(f"Error procesando municipio {municipio}: {str(e)}")
            print(f"❌ Error procesando {municipio}: {str(e)}")
    
    def _esperar_y_extraer_datos(self, municipio):
        """
        Espera a que la tabla se actualice y extrae los datos
        
        Args:
            municipio: Nombre del municipio
            
        Returns:
            bool: True si se extrajeron datos
        """
        try:
            wait = self.driver_manager.obtener_wait()
            
            # Esperar a que la tabla se actualice
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, TABLA_SELECTOR + " " + FILAS_DATOS_SELECTOR)
            ))
            
            print(f"Tabla actualizada para '{municipio}', extrayendo datos...")
            
            # Navegar por todas las páginas
            self.extraction_module.navegar_paginas()
            
            return True
            
        except TimeoutException:
            print(f"No se encontraron datos para el municipio '{municipio}'")
            logging.info(f"No se encontraron datos para: {municipio}")
            return False
            
        except Exception as e:
            print(f"Error al procesar la tabla para '{municipio}': {e}")
            logging.warning(f"Error procesando tabla para {municipio}: {e}")
            return False
    
    def _exportar_datos(self, municipio):
        """
        Exporta los datos extraídos a Excel
        
        Args:
            municipio: Nombre del municipio
        """
        datos = self.extraction_module.obtener_datos()
        
        if not datos:
            print(f"No se extrajeron datos para: {municipio}")
            logging.info(f"No se extrajeron datos para: {municipio}")
            self.resultados["municipios_omitidos"].append(municipio)
            return
        
        # Intentar crear el archivo
        nombre_archivo = generar_nombre_archivo(municipio)
        resultado = ExportHandler.crear_archivo_excel(datos, nombre_archivo)
        
        # Procesar resultado (ahora SIEMPRE es un dict)
        if resultado["status"] == "ok":
            print(f"Archivo creado exitosamente para: {municipio}")
            logging.info(f"Archivo creado: {resultado['path']}")
            self.resultados["municipios_procesados"] += 1
            
        elif resultado["status"] == "nodata":
            print(f"No hay datos para exportar: {municipio}")
            logging.warning(f"Sin datos para {municipio}")
            self.resultados["municipios_omitidos"].append(municipio)
            
        elif resultado["status"] == "error":
            print(f"Error al crear archivo para {municipio}: {resultado['message']}")
            logging.error(f"Error exportando {municipio}: {resultado['message']}")
            self.resultados["errores"].append(f"{municipio}: {resultado['message']}")