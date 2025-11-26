"""
Configuración del sistema de logging
"""
import logging # configuramos los logs
import os # maneja el directorio
import glob # para buscar los archivos en la carpeta
from datetime import datetime, timedelta # para manejar las fechas

def configurar_logging():
    """
    Configura el sistema de logging para la aplicación
    
    Returns:
        str: Nombre del archivo de log creado
    """
    log_dir = "Logs"
    os.makedirs(log_dir, exist_ok=True)

    log_filename = os.path.join(log_dir, f"reporte_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}")
    
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
    
    # Se eliminan los logs con mas de 7 en el archivo 
    threshold = datetime.now() - timedelta(days=7) 
    for log_file in glob.glob(os.path.join(log_dir, "*.log")): 
        file_time = datetime.fromtimestamp(os.path.getmtime(log_file)) 
        if file_time < threshold: 
            os.remove(log_file)

    return log_filename