"""
Gestión del WebDriver de Chrome
"""
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config import settings


class DriverManager:
    """Clase para gestionar el WebDriver de Chrome"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def configurar_driver(self):
        """
        Configura el driver de Chrome con opciones optimizadas
        
        Returns:
            bool: True si la configuración fue exitosa
        """
        try:
            chrome_options = Options()
            
            # Configurar tamaño de ventana
            chrome_options.add_argument(f"--window-size={settings.WINDOW_SIZE}")
            
            # Aplicar opciones de Chrome
            for key, value in settings.CHROME_OPTIONS.items():
                if key == "exclude_switches":
                    chrome_options.add_experimental_option("excludeSwitches", value)
                elif key == "use_automation_extension":
                    chrome_options.add_experimental_option('useAutomationExtension', value)
                elif key.startswith("disable_"):
                    chrome_options.add_argument(f'--{key.replace("_", "-")}={value}')
                else:
                    chrome_options.add_argument(f'--{key.replace("_", "-")}')
            
            # Configurar preferencias
            chrome_options.add_experimental_option("prefs", settings.CHROME_PREFS)
            
            # Inicializar driver
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Configurar tiempos de espera
            self.wait = WebDriverWait(self.driver, settings.EXPLICIT_WAIT)
            self.driver.implicitly_wait(settings.IMPLICIT_WAIT)
            
            logging.info("Driver configurado exitosamente")
            return True
            
        except Exception as e:
            logging.error(f"Error configurando driver: {str(e)}")
            return False
    
    def cerrar_driver(self):
        """Cierra el driver de forma segura"""
        if self.driver:
            try:
                self.driver.quit()
                logging.info("Driver cerrado exitosamente")
            except Exception as e:
                logging.error(f"Error cerrando driver: {str(e)}")
    
    def obtener_driver(self):
        """
        Retorna el driver actual
        
        Returns:
            WebDriver: Instancia del driver
        """
        return self.driver
    
    def obtener_wait(self):
        """
        Retorna el objeto WebDriverWait
        
        Returns:
            WebDriverWait: Instancia de wait
        """
        return self.wait