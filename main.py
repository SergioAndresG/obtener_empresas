"""
Script principal para ejecutar la extracción de datos
"""
import traceback

from config import configurar_logging
from core import ExtractorDatosEmpresa
from urls.urls import URL_LOGIN


def main():
    """Función principal"""
    try:
        # Configurar logging
        configurar_logging()
        
        # Lista de municipios a procesar
        municipios = [
            "Mosquera",
            "Madrid",
            "Bojacá",
            "Zipacón",
            "Facatativá",
            "El Rosal",
            "Subachoque",
            "Tabio",
            "Cota",
            "Funza",
            "Tenjo",
            "Guasca",
            "Gachetá",
            "Gama",
            "Ubalá",
            "Gachalá",
            "Junín"
        ]
        
        print("🚀 Iniciando el proceso de extracción de datos de empresas...")
        
        # Crear instancia del extractor
        extractor = ExtractorDatosEmpresa()
        
        # Ejecutar proceso completo
        extractor.ejecutar_proceso_completo(municipios, URL_LOGIN)
        
    except KeyboardInterrupt:
        print("\n⚠️ Proceso interrumpido por el usuario")
        
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        traceback.print_exc()


if __name__ == "__main__":
    main()