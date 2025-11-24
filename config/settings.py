"""
Configuración general de la aplicación
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Credenciales
USUARIO_LOGIN = os.getenv('USUARIO_LOGIN')
CONTRASENA_LOGIN = os.getenv('CONTRASENA_LOGIN')

# Validar credenciales
if not USUARIO_LOGIN or not CONTRASENA_LOGIN:
    raise ValueError("Error: Las credenciales de login no están configuradas en el archivo .env")

# Configuración de Selenium
IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 10
WINDOW_SIZE = "1920,1080"

# Configuración de Chrome
CHROME_OPTIONS = {
    "disable_blink_features": "AutomationControlled",
    "disable_images": True,
    "disable_javascript": False,
    "exclude_switches": ["enable-automation"],
    "use_automation_extension": False
}

# Preferencias de Chrome
CHROME_PREFS = {
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_settings.popups": 0,
}

# Configuración de Excel
EXCEL_STYLES = {
    "header_color": "366092",
    "header_font_color": "FFFFFF",
    "max_column_width": 50
}