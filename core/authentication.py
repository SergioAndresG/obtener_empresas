"""
Módulo de autenticación
"""
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import settings
from utils.selectors import *


class AuthenticationModule:
    """Maneja la autenticación en la plataforma"""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def realizar_login(self, url_login):
        """
        Realiza el login en la plataforma
        
        Args:
            url_login: URL de la página de login
            
        Returns:
            bool: True si el login fue exitoso
        """
        try:
            self.driver.get(url_login)
            logging.info("Abriendo página de login...")
            
            # Esperar a que desaparezca el loader
            self.wait.until(EC.invisibility_of_element_located((By.ID, "content-load")))
            
            # Seleccionar tipo de usuario
            self._seleccionar_tipo_usuario()
            
            # Completar credenciales
            self._completar_credenciales()
            
            # Hacer click en entrar
            self._hacer_click_entrar()
            
            # Esperar a que cambie la URL (login exitoso)
            self.wait.until(EC.url_changes(url_login))
            
            logging.info("Login exitoso")
            time.sleep(3)  # Esperar a que cargue el dashboard
            return True
            
        except Exception as e:
            logging.error(f"Error durante el login: {str(e)}")
            print(f"Error durante el login: {str(e)}")
            return False
    
    def _seleccionar_tipo_usuario(self):
        """Selecciona el radio button de tipo de usuario"""
        radio_persona = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, RADIO_PERSONA_SELECTOR))
        )
        radio_persona.click()
    
    def _completar_credenciales(self):
        """Completa los campos de usuario y contraseña"""
        # Campo usuario
        campo_usuario = self.wait.until(
            EC.presence_of_element_located((By.ID, CAMPO_USUARIO_SELECTOR))
        )
        campo_usuario.clear()
        campo_usuario.send_keys(settings.USUARIO_LOGIN)
        
        # Campo contraseña
        campo_contrasena = self.driver.find_element(By.ID, CAMPO_CONTRASENA_SELECTOR)
        campo_contrasena.clear()
        campo_contrasena.send_keys(settings.CONTRASENA_LOGIN)
    
    def _hacer_click_entrar(self):
        """Hace click en el botón de entrar"""
        boton_entrar = self.driver.find_element(By.ID, BOTON_ENTRAR_SELECTOR)
        boton_entrar.click()