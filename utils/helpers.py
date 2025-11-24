"""
Funciones auxiliares y helpers
"""
from datetime import datetime

def generar_nombre_archivo(municipio=None):
    """
    Genera un nombre de archivo con timestamp
    
    Args:
        municipio: Nombre del municipio (opcional)
        
    Returns:
        str: Nombre del archivo generado
    """
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    if municipio:
        return f"datos_empresas_{municipio}_{timestamp}.xlsx"
    
    return f"datos_empresas_{timestamp}.xlsx"


def limpiar_texto(texto):
    """
    Limpia y normaliza texto extraído
    
    Args:
        texto: Texto a limpiar
        
    Returns:
        str: Texto limpio
    """
    if not texto:
        return "N/A"
    
    return texto.strip()


def validar_url(url, fragmento_esperado):
    """
    Valida si una URL contiene el fragmento esperado
    
    Args:
        url: URL a validar
        fragmento_esperado: Fragmento que debe contener la URL
        
    Returns:
        bool: True si la URL es válida
    """
    return fragmento_esperado in url