"""
Configuración general de la aplicación
"""
import os
# Variable global para el gestor de credenciales
_credentials_manager = None


def set_credentials_manager(manager):
    """
    Configura el gestor de credenciales para toda la aplicación
    
    Args:
        manager: Instancia de CredentialsManager
    """
    global _credentials_manager
    _credentials_manager = manager


def get_credentials():
    """
    Obtiene las credenciales desde el CredentialsManager
    
    Returns:
        tuple: (username, password) o (None, None) si no están configuradas
    """
    if _credentials_manager is None:
        print("CredentialsManager no está inicializado")
        return None, None
    
    username, password = _credentials_manager.load_credentials()
    
    if username and password:
        return username, password
    else:
        return None, None


def get_usuario_login():
    """Obtiene solo el usuario"""
    username, _ = get_credentials()
    return username


def get_contrasena_login():
    """Obtiene solo la contraseña"""
    _, password = get_credentials()
    return password


def credentials_configured():
    """Verifica si las credenciales están configuradas"""
    username, password = get_credentials()
    return username is not None and password is not None


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