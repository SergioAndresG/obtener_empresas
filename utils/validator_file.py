"""
Utilidad para validar archivos antes de la extracción
"""
import os
from datetime import datetime
from utils.helpers import generar_nombre_archivo


class FileValidator:
    """Valida si los archivos ya existen antes de la extracción"""
    
    @staticmethod
    def verificar_archivos_existentes(municipios):
        """
        Verifica qué archivos ya existen para los municipios dados
        
        Args:
            municipios: Lista de municipios a verificar
            
        Returns:
            dict: {
                'existentes': [lista de municipios con archivos existentes],
                'nuevos': [lista de municipios sin archivos],
                'rutas_existentes': {municipio: ruta_completa}
            }
        """

        reports_dir = "Reportes"
        excel_subdir = f"REPORTE_EMPRESAS - {datetime.now().strftime('%Y-%m')}"
        full_dir_path = os.path.join(reports_dir, excel_subdir)
        
        resultado = {
            'existentes': [],
            'nuevos': [],
            'rutas_existentes': {}
        }
        
        for municipio in municipios:
            nombre_archivo = generar_nombre_archivo(municipio)
            ruta_completa = os.path.join(full_dir_path, nombre_archivo)
            
            if os.path.exists(ruta_completa):
                resultado['existentes'].append(municipio)
                resultado['rutas_existentes'][municipio] = ruta_completa
            else:
                resultado['nuevos'].append(municipio)
        
        return resultado
    
    @staticmethod
    def eliminar_archivos(municipios):
        """
        Elimina los archivos de los municipios especificados
        
        Args:
            municipios: Lista de municipios cuyos archivos se eliminarán
            
        Returns:
            dict: {'eliminados': int, 'errores': [lista de errores]}
        """
        reports_dir = "Reportes"
        excel_subdir = f"REPORTE_EMPRESAS - {datetime.now().strftime('%Y-%m')}"
        full_dir_path = os.path.join(reports_dir, excel_subdir)
        
        resultado = {
            'eliminados': 0,
            'errores': []
        }
        
        for municipio in municipios:
            try:
                nombre_archivo = generar_nombre_archivo(municipio)
                ruta_completa = os.path.join(full_dir_path, nombre_archivo)
                
                if os.path.exists(ruta_completa):
                    os.remove(ruta_completa)
                    resultado['eliminados'] += 1
            except Exception as e:
                resultado['errores'].append(f"{municipio}: {str(e)}")
        
        return resultado