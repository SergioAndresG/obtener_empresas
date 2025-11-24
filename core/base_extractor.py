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
            bool: True si el proceso fue exitoso
        """
        try:
            print("🚀 Iniciando proceso de extracción de datos...")
            
            # Configurar driver
            if not self.driver_manager.configurar_driver():
                return False
            
            # Inicializar módulos
            self.inicializar_modulos()
            
            # Realizar login
            if not self.auth_module.realizar_login(url_login):
                return False
            
            # Navegar a empresas (primera vez)
            if not self.navigation_module.navegar_a_empresas():
                return False
            
            # Procesar cada municipio
            for municipio in municipios:
                self._procesar_municipio(municipio)
            
            print("✅ Proceso completado exitosamente!")
            return True
            
        except Exception as e:
            logging.error(f"Error en proceso completo: {str(e)}")
            print(f"❌ Error en el proceso: {str(e)}")
            traceback.print_exc()
            return False
            
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
            
            # Re-navegar al módulo de empresas
            logging.info(f"Re-navegando al módulo de empresas para: {municipio}")
            if not self.navigation_module.navegar_a_empresas():
                logging.error(f"Fallo al re-navegar para {municipio}. Saltando.")
                return
            
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
            
            print(f"📄 Tabla actualizada para '{municipio}', extrayendo datos...")
            
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
        
        if datos:
            nombre_archivo = generar_nombre_archivo(municipio)
            ExportHandler.crear_archivo_excel(datos, nombre_archivo)
        else:
            print(f"No se extrajeron datos para: {municipio}")
            logging.info(f"No se extrajeron datos para: {municipio}")