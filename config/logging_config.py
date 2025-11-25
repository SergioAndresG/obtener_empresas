"""
Configuración del sistema de logging
"""
import logging
from datetime import datetime

def configurar_logging():
    """
    Configura el sistema de logging para la aplicación
    
    Returns:
        str: Nombre del archivo de log creado
    """
    log_filename = f"repote_empresas_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # También mostrar logs en consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    logging.getLogger().addHandler(console_handler)
    
    return log_filename