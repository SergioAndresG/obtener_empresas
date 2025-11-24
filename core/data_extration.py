"""
Módulo de extracción de datos de tablas
"""
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from httpcore import TimeoutException

from utils.selectors import *
from utils.helpers import limpiar_texto


class DataExtractionModule:
    """Maneja la extracción de datos de tablas"""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.datos_extraidos = []
    
    def extraer_datos_tabla(self):
        """
        Extrae datos de la tabla actual
        
        Returns:
            list: Lista de diccionarios con los datos extraídos
        """
        try:
            # Esperar a que la tabla esté presente
            tabla = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, TABLA_SELECTOR))
            )
            
            # Extraer filas
            filas = tabla.find_elements(By.CSS_SELECTOR, FILAS_DATOS_SELECTOR)
            datos_pagina = []
            
            for fila in filas:
                try:
                    fila_datos = self._extraer_datos_fila(fila)
                    datos_pagina.append(fila_datos)
                except Exception as e:
                    logging.warning(f"Error procesando fila: {str(e)}")
                    continue
            
            return datos_pagina
            
        except Exception as e:
            logging.error(f"Error extrayendo datos de tabla: {str(e)}")
            return []
    
    def _extraer_datos_fila(self, fila):
        """
        Extrae datos de una fila específica
        
        Args:
            fila: Elemento WebElement de la fila
            
        Returns:
            dict: Diccionario con los datos de la fila
        """
        fila_datos = {}
        
        # Tipo de ID
        try:
            tipo_id = fila.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
            fila_datos["Tipo Id."] = limpiar_texto(tipo_id)
        except:
            fila_datos["Tipo Id."] = "N/A"
        
        # Identificación
        try:
            identificacion = fila.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
            fila_datos["Identificación"] = limpiar_texto(identificacion)
        except:
            fila_datos["Identificación"] = "N/A"
        
        # Nombre Empresa
        try:
            nombre = fila.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
            fila_datos["Nombre Empresa"] = limpiar_texto(nombre)
        except:
            fila_datos["Nombre Empresa"] = "N/A"
        
        # Actividad Económica
        try:
            actividad = fila.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
            fila_datos["Actividad Económica"] = limpiar_texto(actividad)
        except:
            fila_datos["Actividad Económica"] = "N/A"
        
        # Fecha de Inscripción
        try:
            fecha = fila.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
            fila_datos["Fecha de Inscripción"] = limpiar_texto(fecha)
        except:
            fila_datos["Fecha de Inscripción"] = "N/A"
        
        # Estado
        try:
            estado = fila.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text
            fila_datos["Estado"] = limpiar_texto(estado)
        except:
            fila_datos["Estado"] = "N/A"
        
        return fila_datos
    
    def navegar_paginas(self):
        """
        Navega por todas las páginas de la tabla
        
        Returns:
            bool: True si la navegación fue exitosa
        """
        try:
            pagina_actual = 1
            
            while True:
                logging.info(f"Procesando página {pagina_actual}")
                
                # Extraer datos de la página actual
                datos_pagina = self.extraer_datos_tabla()
                self.datos_extraidos.extend(datos_pagina)
                
                # Buscar botón "Siguiente"
                if not self._ir_a_siguiente_pagina():
                    logging.info("Llegamos a la última página")
                    break
                
                time.sleep(2)  # Esperar a que cargue la nueva página
                pagina_actual += 1
            
            logging.info(f"Total de registros extraídos: {len(self.datos_extraidos)}")
            return True
            
        except Exception as e:
            logging.error(f"Error navegando páginas: {str(e)}")
            return False
    
    def _ir_a_siguiente_pagina(self):
        """
        Intenta ir a la siguiente página
        
        Returns:
            bool: True si pudo avanzar a la siguiente página
        """
        try:
            boton_siguiente = self.driver.find_element(By.ID, "bus-table_next")
            
            # Verificar si el botón está habilitado
            if "disabled" in boton_siguiente.get_attribute("class"):
                return False
            
            # Hacer click en siguiente
            self.driver.execute_script("arguments[0].click();", boton_siguiente)
            return True
            
        except Exception as e:
            logging.info("No se encontró botón siguiente o error navegando")
            return False
    
    def obtener_datos(self):
        """
        Retorna los datos extraídos
        
        Returns:
            list: Lista de diccionarios con los datos
        """
        return self.datos_extraidos
    
    def limpiar_datos(self):
        """Limpia los datos extraídos"""
        self.datos_extraidos = []