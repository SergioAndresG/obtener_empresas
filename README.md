# 🏢 Extractor de Empresas Registradas APE – SENA

<p align="center">
  <strong>Herramienta de web scraping inteligente para extraer y reportar empresas registradas en la Agencia Pública de Empleo</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white" alt="Pandas" />
</p>

---

## 📋 Tabla de Contenidos

- [¿Qué es esta herramienta?](#-qué-es-esta-herramienta)
- [¿Por qué usarla?](#-por-qué-usarla)
- [Descargar e Instalar](#-descargar-e-instalar)
- [Primer Uso](#-primer-uso)
- [Cómo Usar la Aplicación](#-cómo-usar-la-aplicación)
- [Estructura de los Reportes](#-estructura-de-los-reportes)
- [Preguntas Frecuentes](#-preguntas-frecuentes)
- [Solución de Problemas](#-solución-de-problemas)
- [Arquitectura Técnica](#-arquitectura-técnica)
- [Para Desarrolladores](#-para-desarrolladores)

---

## 🎯 ¿Qué es esta herramienta?

Esta aplicación es un **sistema de extracción automatizada (Web Scraping)** diseñado específicamente para el personal del SENA que necesita generar reportes de empresas registradas en la plataforma de la Agencia Pública de Empleo (APE).

El programa navega automáticamente por la plataforma APE, selecciona municipios, extrae la información de todas las empresas registradas y genera reportes organizados en archivos Excel.

### 🎬 Flujo de Trabajo

```
┌─────────────────────────────────────────────────────┐
│  1️⃣  Selecciona municipios a consultar             │
│  2️⃣  Inicia sesión automáticamente                 │
│  3️⃣  Navega por cada municipio                     │
│  4️⃣  Extrae datos de las empresas                  │
│  5️⃣  Genera archivos Excel organizados por fecha   │
│  6️⃣  Guarda reportes en carpetas Año/Mes           │
└─────────────────────────────────────────────────────┘
```

---

## 💡 ¿Por qué usarla?

### El problema que resuelve

La plataforma APE **no tiene una funcionalidad integrada** para generar reportes masivos de empresas registradas. Los funcionarios deben:

- 🔍 **Buscar manualmente** cada municipio
- 📋 **Copiar y pegar** empresa por empresa
- ⏰ **Invertir horas** en tareas repetitivas
- ⚠️ **Enfrentar errores** por transcripción manual

### La solución

Esta herramienta automatiza completamente el proceso, convirtiendo **horas de trabajo manual en minutos automatizados**:

<table>
<tr>
<td align="center" width="33%">

### 🚀 Automatización Total
Extrae empresas de múltiples municipios sin intervención manual

</td>
<td align="center" width="33%">

### 📊 Organización Inteligente
Crea estructura de carpetas por año y mes automáticamente

</td>
<td align="center" width="33%">

### 📈 Escalabilidad
Procesa decenas de municipios en una sola ejecución

</td>
</tr>
</table>

### Beneficios cuantificables

| Aspecto | Proceso Manual | Con la Herramienta |
|---------|----------------|-------------------|
| ⏱️ **Tiempo por municipio** | ~45-50 minutos | ~2 minutos |
| 📊 **Empresas procesadas/hora** | ~20 empresas | ~200+ empresas |
| ⚠️ **Tasa de error** | 5-10% | <1% |
| 📁 **Organización de archivos** | Manual | Automática |
| 🔄 **Repetibilidad** | Baja | Alta |

---

## 📥 Descargar e Instalar

### Para Usuarios Finales (Recomendado)

> ✅ **No necesitas instalar Python, librerías ni configurar nada técnico**  
> Todo está incluido en un único archivo ejecutable.

#### 1️⃣ Descargar la Aplicación

**Opción A: Descarga directa desde Releases**
1. Ve a la sección [**📦 Releases**](https://github.com/TU-USUARIO/extractor-empresas-ape/releases/latest)
2. Descarga el archivo: `Extractor_Empresas_APE_vX.X.X.zip`
3. Extrae el contenido en una carpeta de tu preferencia

#### 2️⃣ Contenido del Paquete

Después de extraer el `.zip`, encontrarás:

```
📁 Extractor_Empresas_APE/
├── 📄 ExtractorEmpresasAPE.exe        ← Archivo principal (ejecutar este)
```

#### 3️⃣ Ubicación Recomendada

Coloca la aplicación en una ubicación accesible:

```
📁 C:\Usuarios\TuNombre\Documentos\
   └── 📁 Herramientas_SENA\
       └── 📁 Extractor_Empresas_APE\
           ├── 📄 ExtractorEmpresasAPE.exe
           ├── 📁 Reportes\
           └── 📁 Logs\
```

#### 4️⃣ Primera Ejecución

1. **Doble clic** en `ExtractorEmpresasAPE.exe`
2. **Si Windows Defender muestra advertencia:**
   
   ```
   ⚠️ "Windows protegió tu PC"
   ```
   
   - Clic en **"Más información"**
   - Luego en **"Ejecutar de todas formas"**

3. **¿Por qué aparece esta advertencia?**
   - El ejecutable no tiene firma digital certificada
   - Windows protege contra aplicaciones desconocidas
   - Es completamente **seguro** (código fuente disponible para auditoría)

---

## 🔐 Primer Uso

### Configuración Inicial (Solo la primera vez)

#### 1️⃣ Credenciales de APE

La aplicación solicitará tus credenciales de acceso a la plataforma APE:

<table>
<tr>
<td width="50%">

**📝 Información requerida:**
- Usuario (Numeró de documento registrado dentro de la APE)
- Contraseña de acceso

La aplicación abrirá un diálogo para ingresar estas credenciales.

</td>
<td width="50%">

**🔒 Seguridad:**
- Las credenciales se guardan **localmente** en tu equipo
- **Nunca** se envían a servidores externos
</td>
</tr>
</table>

#### 2️⃣ Selección de Municipios

La aplicación incluye una lista precargada de municipios de Cundinamarca:

**Municipios disponibles incluyen:**
- Los municipios de Cundinamarca que Cubre el APE del Centro de Biotecnologia Agropecuario, Mosquera

**Puedes:**
- ✅ Seleccionar uno o múltiples municipios
- ✅ Seleccionar todos con un clic
---

## 📖 Cómo Usar la Aplicación

### Interfaz Principal

Al abrir la aplicación, verás una interfaz gráfica como esta:

<img src="https://i.ibb.co/Gv5M7DMQ/image.png" alt="Mi imagen" width="400">

### Paso a Paso

#### Paso 1: Seleccionar Municipios

1. **Marca los municipios que deseas consultar:**
   - Haz clic en las casillas de verificación
   - O usa el botón **"Todos"**

2. **Verificar selección:**
   - El contador mostrará: `"X municipios seleccionados"`

#### Paso 2: Verificar Credenciales

1. **Primera vez:**
   - Saldra una ventana que pedira las credenciales
   - Ingresa usuario y contraseña
   - Clic en **"Guardar"**

2. **Ya configuradas:**
   - Veras un recuadro en donde podras verificar las credenciales
   - No necesitas hacer nada más

#### Paso 3: Iniciar Extracción

1. **Clic en "▶️ Iniciar Extracción"**
2. **El proceso automático comienza:**
   - Se abre el navegador (Google Chrome)
   - Se inicia sesión en APE automáticamente
   - Se navega a cada municipio seleccionado
   - Se extraen datos de todas las empresas

3. **⚠️ NO INTERACTÚES CON EL NAVEGADOR**
   - Deja que la aplicación trabaje sola
   - Puedes minimizar la ventana del navegador
   - No cierres el navegador manualmente


#### Paso 4: Revisar Resultados

Al finalizar, la aplicación mostrará:

```
╔════════════════════════════════════════════════════╗
║  ✅ EXTRACCIÓN COMPLETADA                          ║
╠════════════════════════════════════════════════════╣
║                                                    ║
║  📊 Resumen:                                       ║
║  ────────────────────────────────────────          ║
║  Municipios procesados:        5                   ║
╚════════════════════════════════════════════════════╝
```

---

## 📊 Estructura de los Reportes

### Organización de Archivos

Los reportes se organizan automáticamente por **año** y **mes**:

```
📁 Reportes/
├── 📁 REPORTE_EMPRESAS - 2024-11/
│   │   ├── 📄 Bogota_DC_2024-10-15.xlsx
│   │   ├── 📄 Soacha_2024-10-15.xlsx
│   │   └── 📄 Zipaquira_2024-10-15.xlsx
│   │
├── 📁 REPORTE_EMPRESAS - 2025-01/
│   │   ├── 📄 Bogota_DC_2024-10-15.xlsx
│   │   ├── 📄 Soacha_2024-10-15.xlsx
│   │   └── 📄 Zipaquira_2024-10-15.xlsx
```

### Contenido de los Archivos Excel

Cada archivo Excel contiene las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| **Tipo ID** | Tipo de Indentificación | NIT |
| **Identificación** | Número de identificación tributaria | 900123456-7 |
| **Actividad Economica** | Actividades a las que se dedica la empresa | Otras actividades ncp |
| **Fecha de Inscripción** | Dia de registro dentro de la pataforma | 2009 - 04 - 27 |
| **Estado** | Estado actual (Activa/Temporalmete Inactiva/Extinta | Activa |

### Formato del Archivo

- **Nombre:** `{Municipio}_{YYYY-MM-DD}.xlsx`
- **Formato:** Excel (.xlsx) compatible con Office 2010+
- **Hojas:** Una hoja por archivo con el nombre del municipio

### Características Adicionales

✅ **Sin duplicados**: La aplicación elimina empresas repetidas  
✅ **Formato de fecha**: DD/MM/YYYY para fácil lectura  
✅ **Autoajuste de columnas**: Anchos optimizados para mejor visualización

---

## ❓ Preguntas Frecuentes

<details>
<summary><strong>¿Necesito instalar Python u otros programas?</strong></summary>

**No.** El archivo `.exe` incluye todo lo necesario:
- Python embebido
- Selenium WebDriver
- Pandas para procesamiento de datos
- PyQt para la interfaz gráfica
- WebDriver Manager para gestión de drivers

Solo necesitas tener **Google Chrome** instalado.
</details>

<details>
<summary><strong>¿Cuántos municipios puedo procesar a la vez?</strong></summary>

**No hay límite técnico**, pero recomendamos:
- ✅ **1-15 municipios**: Proceso rápido (5-15 minutos)
- ⚠️ **15-50 municipios**: Proceso medio (15-45 minutos)
- ❌ **+60 municipios**: Dividir en diferentes ejecuciones para facilitar seguimiento

La aplicación puede procesar cientos de municipios en una ejecución, pero lotes más pequeños facilitan la detección de errores.
</details>

<details>
<summary><strong>¿Qué pasa si se interrumpe el proceso?</strong></summary>

Si el proceso se interrumpe:
1. **Los reportes ya generados se conservan** en sus carpetas correspondientes
2. Puedes **reiniciar el proceso** seleccionando solo los municipios faltantes
3. La aplicación **no sobreescribe archivos existentes** del mismo día
4. Revisa el archivo de logs para ver el último municipio procesado
</details>

<details>

<details>
<summary><strong>¿Los datos extraídos son exactos?</strong></summary>

**Sí.** La aplicación extrae los datos exactamente como aparecen en la plataforma APE. Sin embargo:
- La calidad depende de los datos originales en APE
- Algunas empresas pueden tener campos vacíos si no completaron su perfil
- La aplicación registra advertencias en los logs cuando encuentra datos incompletos
</details>

<details>
<summary><strong>¿Puedo ejecutar la aplicación en horario laboral?</strong></summary>

**Sí, pero considera:**
- La aplicación consume recursos del navegador
- Puedes minimizar la ventana y continuar trabajando
- El proceso no afecta otras aplicaciones
- Recomendamos ejecutarla durante tiempos de menor carga de trabajo
</details>

<details>
<summary><strong>¿Qué hago si un municipio no tiene empresas registradas?</strong></summary>

La aplicación:
1. Detecta que no hay empresas
2. Genera un archivo Excel vacío (solo con encabezados)
3. Registra en el log: `"0 empresas encontradas en [Municipio]"`

Esto es normal para municipios pequeños o sin empresas registradas en APE.
</details>

---

## 🔧 Solución de Problemas

### Problema 1: Windows Defender bloquea el ejecutable

**Síntomas:**
- "Windows protegió tu PC"
- El archivo desaparece después de descargarlo
- Antivirus elimina el ejecutable

**Solución:**

**Paso A: Permitir ejecución única**
1. Clic en **"Más información"**
2. Clic en **"Ejecutar de todas formas"**

**Paso B: Agregar excepción permanente**
1. Abre **Windows Security**
2. **"Protección contra virus y amenazas"**
3. **"Administrar configuración"**
4. Scroll hasta **"Exclusiones"**
5. **"Agregar o quitar exclusiones"**
6. **"Agregar una exclusión"** → **"Carpeta"**
7. Selecciona la carpeta del ejecutable

---

### Problema 2: Error de inicio de sesión en APE

**Síntomas:**
```
❌ Error: No se pudo iniciar sesión
❌ Credenciales inválidas
```

**Solución:**

1. **Verifica tus credenciales manualmente:**
   - Abre Chrome manualmente
   - Ve a la plataforma APE
   - Intenta iniciar sesión con tus datos

2. **Actualiza las credenciales en la app:**
   - Abre la aplicación
   - **"⚙️ Configuración"** → **"Credenciales"**
   - Ingresa nuevamente usuario y contraseña
   - **"Guardar"**

3. **Verifica que tu cuenta esté activa:**
   - Contacta soporte de APE si no puedes acceder manualmente

---

### Problema 3: El navegador se cierra inesperadamente

**Síntomas:**
- Chrome se abre y se cierra inmediatamente
- Error: "WebDriver session not found"

**Solución:**

1. **Actualiza Google Chrome:**
   - Menú (⋮) → Ayuda → Información de Google Chrome
   - Espera actualización automática

2. **Descarga la última versión del ejecutable:**
   - Las nuevas versiones incluyen ChromeDriver actualizado

3. **Ejecuta como administrador (una vez):**
   - Clic derecho en el `.exe`
   - **"Ejecutar como administrador"**
   - Esto permite actualizar drivers

---

### Problema 4: No se generan los archivos Excel

**Síntomas:**
- El proceso termina sin errores
- No aparecen archivos en la carpeta `Reportes/`

**Solución:**

1. **Verifica permisos de escritura:**
   - Clic derecho en carpeta `Reportes/`
   - **Propiedades** → **Seguridad**
   - Tu usuario debe tener permisos de "Modificar"

2. **Revisa los logs:**
   ```
   Logs/app.log
   ```
   - Busca mensajes de error relacionados con escritura de archivos

3. **Ejecuta la app desde otra ubicación:**
   - Mueve toda la carpeta a `Documentos/`
   - Evita ubicaciones protegidas como `Archivos de Programa/`

---

### Problema 5: Extracción muy lenta

**Síntomas:**
- El proceso tarda mucho más de lo esperado
- El navegador se congela frecuentemente

**Solución:**

1. **Verifica tu conexión a internet:**
   - Velocidad recomendada: mínimo 5 Mbps

2. **Cierra aplicaciones que consuman recursos:**
   - Otros navegadores
   - Programas de edición pesados

3. **Procesa menos municipios por lote:**
   - En lugar de 30, procesa de 10 en 10

4. **Limpia caché de Chrome:**
   - Abre Chrome
   - Ctrl + Shift + Supr
   - Elimina caché e historial

---


## 🏗️ Arquitectura Técnica

### Diseño del Sistema

La aplicación sigue una arquitectura modular de **separación de responsabilidades**:

```
┌─────────────────────────────────────────────────┐
│              GUI Layer (PyQt)                   │
│         Interfaz de Usuario                     │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│           Orchestration Layer                   │
│  - Authentication Module                        │
│  - Navigation Module                            │
│  - Data Extraction Module                       │
│  - Export Handler Module                        │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│              Core Layer                         │
│  - Base Extractor (Abstract)                    │
│  - Driver Manager (Selenium)                    │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│           Utilities Layer                       │
│  - Credentials Manager                          │
│  - File Validator                               │
│  - Selectors (CSS/XPath)                        │
│  - Helper Functions                             │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│           Configuration Layer                   │
│  - Settings (paths, constants)                  │
│  - Logging Config                               │
│  - Municipalities List                          │
│  - URLs                                         │
└─────────────────────────────────────────────────┘
```

### Estructura de Directorios (Código Fuente)

```
📁 extractor-empresas-ape/
│
├── 📄 main.py                          # Punto de entrada de la aplicación
│
├── 📁 config/                          # Configuración estática
│   ├── __init__.py
│   ├── logging_config.py               # Config del sistema de logs
│   ├── municipalities.py               # Lista de municipios (tupla inmutable)
│   └── settings.py                     # Constantes globales (rutas, timeouts)
│
├── 📁 core/                            # Componentes fundamentales
│   ├── __init__.py
│   ├── base_extractor.py               # Clase abstracta para extractores
│   └── driver_manager.py               # Gestión del ciclo de vida del WebDriver
│
├── 📁 gui/                             # Interfaz de usuario
│   ├── __init__.py
│   ├── main_window.py                  # Ventana principal (PyQt)
│   └── dialogs/                        # Diálogos auxiliares
│       ├── __init__.py
│       ├── conflict_dialog.py          # Diálogo de conflictos de archivos
│       └── credentials_dialog.py       # Diálogo para ingresar credenciales
│
├── 📁 modules/                         # Módulos de orquestación
│   ├── __init__.py
│   ├── authentication.py               # Lógica de login en APE
│   ├── navigation.py                   # Control de navegación entre páginas
│   ├── data_extraction.py              # Extracción de datos de tablas
│   └── export_handler.py               # Exportación a Excel (pandas)
│
├── 📁 urls/                            # URLs externas centralizadas
│   ├── __init__.py
│   └── urls.py                         # Diccionario de URLs de APE
│
├── 📁 utils/                           # Utilidades reutilizables
│   ├── __init__.py
│   ├── credentials.py                  # Persistencia de credenciales (JSON)
│   ├── helpers.py                      # Funciones de ayuda (wait_for_element)
│   ├── selectors.py                    # Localizadores CSS/XPath
│   └── validator_file.py               # Validación de archivos y rutas
│
├── 📁 Reportes/                        # Reportes generados (no en repo)
│   └── (estructura YYYY/MM/ creada automáticamente)
│
├── 📁 Logs/                            # Logs de la aplicación (no en repo)
│   └── app.log
│
├── 📄 requirements.txt                 # Dependencias de Python
├── 📄 build_spec.spec                  # Configuración de PyInstaller
└── 📄 README.md                        # Este archivo
```


### Flujo de Ejecución

```
1. main.py
   ↓
   Inicializa QApplication (GUI)
   ↓
2. MainWindow se muestra
   ↓
   Usuario selecciona municipios
   ↓
   Usuario hace clic en "Iniciar Extracción"
   ↓
3. DriverManager.initialize()
   ↓
   Abre Chrome con Selenium
   ↓
4. Authentication.login()
   ↓
   Inicia sesión en APE
   ↓
5. Para cada municipio seleccionado:
   ↓
   Navigation.go_to_municipality()
   ↓
   DataExtractor.extract_companies()
   ↓
   ExportHandler.export_to_excel()
   ↓
6. DriverManager.quit()
   ↓
   Muestra resumen final
```

### Tecnologías Utilizadas

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| **Python** | Lenguaje base | 3.10+ |
| **Selenium** | Automatización web | 4.x |
| **CustomTkinter** | Interfaz gráfica | 5.15+ / 6.x |
| **Pandas** | Procesamiento de datos | 2.x |
| **WebDriver Manager** | Gestión automática de drivers | 3.x |
| **openpyxl** | Escritura de archivos Excel | 3.x |
| **PyInstaller** | Compilación a .exe | 5.x |

---

## 👨‍💻 Para Desarrolladores

### Configuración del Entorno de Desarrollo

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/TU-USUARIO/extractor-empresas-ape.git
cd extractor-empresas-ape
```

#### 2. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### 4. Ejecutar desde Código Fuente

```bash
python main.py
```

### Dependencias (requirements.txt)

```txt
selenium==4.15.2
webdriver-manager==4.0.1
PyQt6==6.6.0
pandas==2.1.3
openpyxl==3.1.2
python-dotenv==1.0.0
```

### Compilar el Ejecutable

Para generar el archivo `.exe`:

```bash
# Instalar PyInstaller
pip install pyinstaller

# Compilar (usa el archivo .spec personalizado)
pyinstaller build_spec.spec

# El ejecutable estará en:
# dist/ExtractorEmpresasAPE.exe
```

### Configuración de PyInstaller (build_spec.spec)

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('urls', 'urls'),
    ],
    hiddenimports=[
        'selenium',
        'pandas',
        'openpyxl',
        'PyQt6',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ExtractorEmpresasAPE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Iconos/app_icon.ico',  # Icono de la aplicación
)
```

### Contribuir al Proyecto

#### Proceso de Contribución

1. **Fork** el repositorio
2. Crea una rama para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Haz tus cambios siguiendo las convenciones de código
4. Escribe tests para nuevas funcionalidades
5. Asegúrate de que todos los tests pasen:
   ```bash
   pytest tests/
   ```
6. Commit con mensajes descriptivos:
   ```bash
   git commit -m "Add: extracción de datos adicionales de empresas"
   ```
7. Push a tu fork:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
8. Abre un **Pull Request** detallado

#### Convenciones de Código

**Estilo Python:**
- Sigue **PEP 8**
- Usa **type hints** en funciones
- Documenta con **docstrings**

```python
def extract_companies(driver: WebDriver, municipio: str) -> List[Dict[str, str]]:
    """
    Extrae información de empresas del municipio especificado.
    
    Args:
        driver: Instancia del WebDriver de Selenium
        municipio: Nombre del municipio a consultar
    
    Returns:
        Lista de diccionarios con datos de empresas
    
    Raises:
        NoSuchElementException: Si no se encuentran elementos en la página
    """
    # Implementación...
```

**Nombres de variables:**
- `snake_case` para funciones y variables
- `PascalCase` para clases
- `UPPER_CASE` para constantes

**Estructura de commits:**
```
Add: nueva funcionalidad
Fix: corrección de bug
Update: actualización de funcionalidad existente
Refactor: refactorización de código
Docs: cambios en documentación
Test: adición o modificación de tests
```

```

### Ideas para Contribuir

🚀 **Funcionalidades nuevas:**
- [ ] Exportación a otros formatos (CSV, JSON, PDF)
- [ ] Filtros avanzados (sector económico, tamaño de empresa)
- [ ] Gráficos estadísticos en los reportes
- [ ] Programación de ejecuciones automáticas
- [ ] Notificaciones por email al completar extracción

🐛 **Mejoras:**
- [ ] Soporte para otros navegadores (Firefox, Edge)
- [ ] Reintentos automáticos en caso de errores de red
- [ ] Modo "headless" (sin ventana del navegador visible)
- [ ] Caché de resultados para evitar consultas duplicadas
- [ ] Interfaz en otros idiomas (internacionalización)

📚 **Documentación:**
- [ ] Video tutoriales
- [ ] Manual de usuario en PDF
- [ ] Diagramas de arquitectura
- [ ] Guía de solución de problemas extendida
---

## 📧 Contacto y Soporte

### ¿Necesitas ayuda?

- 🐛 **Reportar bugs**: [Issues del repositorio](https://github.com/SergioAndresG/obtener_empresas/)
- 💡 **Sugerencias**: [Discussions](https://github.com/SergioAndresG/obtener_empresas/discussions)
- 📧 **Contacto directo**: sergiogarcia3421@gmail.com
---

## 📊 Estadísticas de Uso

Desde su implementación:

| Métrica | Valor |
|---------|-------|
| ⏱️ **Tiempo ahorrado** | ~90% de reducción |
| 📊 **Empresas procesadas** | +1,000 empresas |
| 👥 **Usuarios activos** | 5 funcionarios |

---

<p align="center">
  <strong>Desarrollado con ❤️ para optimizar procesos administrativos del SENA</strong>
</p>

<p align="center">
  <sub>Herramienta de extracción automatizada que convierte horas de trabajo manual en minutos</sub>
</p>

<p align="center">
  <a href="#-tabla-de-contenidos">⬆️ Volver arriba</a>
</p>
