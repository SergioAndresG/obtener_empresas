"""
Selectores CSS utilizados
"""

# Selectores de la tabla principal
TABLA_SELECTOR = "table#bus-table"
ENCABEZADOS_SELECTOR = "thead tr th"
FILAS_DATOS_SELECTOR = "tbody tr"
CELDAS_SELECTOR = "td"
BOTON_SIGUIENTE_SELECTOR = "a#bus-table_next"
BOTON_ACCION_SELECTOR = "td button"

# Selectores para columnas específicas
SELECTORES_COLUMNAS = {
    "tipo_id": "td:nth-child(1)",
    "identificacion": "td:nth-child(2)",
    "nombre_empresa": "td:nth-child(3)",
    "actividad_economica": "td:nth-child(4)",
    "fecha_inscripcion": "td:nth-child(5)",
    "estado": "td:nth-child(6)",
    "accion": "td:nth-child(7)"
}

# Selectores de login
RADIO_PERSONA_SELECTOR = "//input[@type='radio' and @name='tipousuario' and @value='0']"
CAMPO_USUARIO_SELECTOR = "username"
CAMPO_CONTRASENA_SELECTOR = "password"
BOTON_ENTRAR_SELECTOR = "entrar"

# Selectores de navegación
DROPDOWN_EMPRESA_XPATH = "//a[@class='dropdown-toggle' and contains(text(), 'Empresa')]"
OPCION_REGISTRO_XPATH = "//ul[@class='dropdown-menu']//a[contains(text(), 'Registro y/o actualización de empresa')]"

# Selectores de búsqueda avanzada
BOTON_BUSQUEDA_AVANZADA = "btnBusqAvanzada"
MODAL_BUSQUEDA = "modalBusqAvanzada"
INPUT_PAIS = "bus-pais"
INPUT_DEPARTAMENTO = "bus-departamento"
INPUT_MUNICIPIO = "bus-municipio"
BOTON_BUSCAR = "btnBuscarAv" 