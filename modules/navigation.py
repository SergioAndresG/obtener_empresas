"""
Módulo de navegación por la aplicación
"""
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from utils.selectors import *
from utils.helpers import validar_url


class NavigationModule:
    """Maneja la navegación por la aplicación"""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def navegar_a_empresas(self):
        """
        Navega al módulo de empresas
        
        Returns:
            bool: True si la navegación fue exitosa
        """
        try:
            print("Navegando a Empresas")
            
            # Click en dropdown Empresa
            dropdown_empresa = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, DROPDOWN_EMPRESA_XPATH))
            )
            print("Dropdown encontrado")
            dropdown_empresa.click()
            time.sleep(2)
            
            # Click en opción de registro
            opcion_registro = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OPCION_REGISTRO_XPATH))
            )
            print("Opción de registro encontrada")
            opcion_registro.click()
            time.sleep(2)
            
            # Verificar URL
            current_url = self.driver.current_url
            print(f"URL actual: {current_url}")
            
            if validar_url(current_url, "funcionario/empresa"):
                print("Navegación exitosa al módulo de empresas")
                return True
            else:
                print("No se pudo navegar al módulo de empresas")
                return False
                
        except Exception as e:
            logging.error(f"Error navegando a empresas: {str(e)}")
            print(f"Error en navegación: {str(e)}")
            return False
    
    def hacer_consulta_avanzada(self, municipio, pais="Colombia", departamento="Cundinamarca"):
        """
        Realiza una búsqueda avanzada con filtros
        
        Args:
            municipio: Nombre del municipio
            pais: Nombre del país (default: Colombia)
            departamento: Nombre del departamento (default: Cundinamarca)
            
        Returns:
            bool: True si la búsqueda fue exitosa
        """
        try:
            print("Haciendo búsqueda avanzada")
            
            # Abrir modal de búsqueda avanzada
            self._abrir_modal_busqueda()
            
            # Seleccionar país
            self._seleccionar_pais(pais)
            
            # Seleccionar departamento
            self._seleccionar_departamento(departamento)
            
            # Seleccionar municipio
            self._seleccionar_municipio(municipio)
            
            # Ejecutar búsqueda
            self._ejecutar_busqueda()
            
            return True
            
        except Exception as e:
            logging.error(f"Error en búsqueda avanzada: {str(e)}")
            print(f"Error en búsqueda avanzada: {str(e)}")
            return False
    
    def _abrir_modal_busqueda(self):
        """Abre el modal de búsqueda avanzada"""
        boton_avanzada = self.wait.until(
            EC.element_to_be_clickable((By.ID, BOTON_BUSQUEDA_AVANZADA))
        )
        boton_avanzada.click()
        time.sleep(3)
        
        # Esperar a que el modal sea visible
        self.wait.until(
            EC.visibility_of_element_located((By.ID, MODAL_BUSQUEDA))
        )
    
    def _seleccionar_pais(self, pais):
        """Selecciona el país en el filtro"""
        input_pais = self.wait.until(
            EC.presence_of_element_located((By.ID, INPUT_PAIS))
        )
        selector_pais = Select(input_pais)
        selector_pais.select_by_visible_text(pais)
        print(f"Se seleccionó {pais} en el input")
        time.sleep(1)
    
    def _seleccionar_departamento(self, departamento):
        """Selecciona el departamento en el filtro"""
        input_departamento = self.wait.until(
            EC.presence_of_element_located((By.ID, INPUT_DEPARTAMENTO))
        )
        selector_departamento = Select(input_departamento)
        selector_departamento.select_by_visible_text(departamento)
        print(f"Se seleccionó {departamento} en departamento")
        time.sleep(1)
    
    def _seleccionar_municipio(self, municipio):
        """Selecciona el municipio en el filtro"""
        input_municipio = self.wait.until(
            EC.presence_of_element_located((By.ID, INPUT_MUNICIPIO))
        )
        Select(input_municipio).select_by_visible_text(municipio)
        print(f"Se seleccionó el municipio {municipio}")
        time.sleep(2)
    
    def _ejecutar_busqueda(self):
        """Ejecuta la búsqueda avanzada"""
        boton_buscar = self.wait.until(
            EC.element_to_be_clickable((By.ID, BOTON_BUSCAR))
        )
        boton_buscar.click()
        time.sleep(2)