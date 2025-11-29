# 🏢 Extractor de Empresas Registradas APE – SENA

<p align="center">
  <strong>Herramienta de web scraping inteligente para extraer y reportar empresas registradas en la Agencia Pública de Empleo</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Version-1.0_CBA-orange" alt="Versión" />
</p>

> ⚠️ **Versión Actual:** Configurada para el **Centro de Biotecnología Agropecuaria (CBA) - Mosquera, Cundinamarca**

---

## 📋 Tabla de Contenidos

- [¿Qué es esta herramienta?](#-qué-es-esta-herramienta)
- [Alcance Actual de la Aplicación](#-alcance-actual-de-la-aplicación)
- [¿Por qué usarla?](#-por-qué-usarla)
- [Descargar e Instalar](#-descargar-e-instalar)
- [Primer Uso](#-primer-uso)
- [Cómo Usar la Aplicación](#-cómo-usar-la-aplicación)
- [Estructura de los Reportes](#-estructura-de-los-reportes)
- [Preguntas Frecuentes](#-preguntas-frecuentes)
- [Solución de Problemas](#-solución-de-problemas)
- [Arquitectura Técnica](#-arquitectura-técnica)
- [Para Desarrolladores](#-para-desarrolladores)
- [Roadmap y Versiones Futuras](#-roadmap-y-versiones-futuras)

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

## 🗺️ Alcance Actual de la Aplicación

### Versión 1.0 - Centro de Biotecnología Agropecuaria (CBA)

Esta primera versión está diseñada y configurada exclusivamente para:

<table>
<tr>
<td align="center" width="33%">

### 🏛️ Centro SENA
**Centro de Biotecnología Agropecuaria**  
Mosquera, Cundinamarca

</td>
<td align="center" width="33%">

### 📍 Cobertura
**Municipios de Cundinamarca**  
Asignados al CBA - APE

</td>
<td align="center" width="33%">

### 👥 Usuarios
**Funcionarios del CBA**  
Con acceso a APE

</td>
</tr>
</table>

### ¿Por qué solo un centro?

La aplicación necesita conocer **qué municipios están asignados a cada centro SENA** para mostrarlos correctamente. Actualmente:

✅ **Tenemos mapeados:** Municipios del Centro de Biotecnología Agropecuaria (CBA)  
❌ **Pendiente de mapeo:** Municipios de otros centros SENA de Colombia

### ¿Eres de otro centro SENA?

Si trabajas en un **centro diferente al CBA** y necesitas esta herramienta:

1. 📧 **Contáctanos**: sergiogarcia3421@gmail.com
2. 📋 **Proporciona**: Lista de municipios que cubre tu centro
3. 🎁 **Recibe**: Versión personalizada para tu centro
4. 🚀 **Contribuye**: Ayúdanos a expandir la cobertura nacional

---

## 🔮 Roadmap y Versiones Futuras

### Versión 1.5 (Próximamente)

**Selector de Centro SENA**

La próxima versión incluirá:

```
╔════════════════════════════════════════════════════╗
║  🏛️ Selección de Centro SENA                      ║
╠════════════════════════════════════════════════════╣
║                                                    ║
║  Selecciona tu centro:                             ║
║  ┌──────────────────────────────────────────┐    ║
║  │ ○ Centro de Biotecnología Agropecuaria   │    ║
║  │ ○ Centro de Servicios Financieros        │    ║
║  │ ○ Centro de Electricidad y Automatización│    ║
║  │ ○ [Más centros...]                       │    ║
║  └──────────────────────────────────────────┘    ║
║                                                    ║
║  📍 Municipios disponibles: 15                    ║
╚════════════════════════════════════════════════════╝
```

**Funcionalidades planeadas:**
- ✨ Selector de centro SENA en la interfaz
- 📍 Carga dinámica de municipios según el centro seleccionado
- 🗂️ Base de datos de centros y municipios de toda Colombia
- 💾 Recordar el centro seleccionado para futuras ejecuciones
- 🔄 Actualización automática de lista de centros

### Versión 2.0 (Visión a futuro)

**Expansión Nacional**

- 🇨🇴 Todos los centros SENA de Colombia
- 🌐 API para sincronización automática de municipios
- 📊 Reportes consolidados multi-centro
- 👥 Sistema de permisos por centro
- 📱 Versión web multiplataforma

### ¿Cómo puedes ayudar?

Si quieres que tu centro esté incluido en la versión 1.5:

**Información requerida:**
```
📋 Formato de información del centro:

Nombre del Centro: _______________________________
Ciudad/Municipio: _________________________________
Regional: _________________________________________

Municipios de Cobertura APE:
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________
[... continuar lista completa]
```

Envía esta información a: **sergiogarcia3421@gmail.com**

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

**Descarga directa desde Releases:**
1. Ve a la sección [**📦 Releases**](https://github.com/SergioAndresG/obtener_empresas/releases/latest)
2. Descarga el archivo: `Extractor_Empresas_APE_CBA_vX.X.X.zip`
3. Extrae el contenido en una carpeta de tu preferencia

> 📌 **Nota:** El nombre del archivo incluye "CBA" indicando que es la versión para el Centro de Biotecnología Agropecuaria.

#### 2️⃣ Contenido del Paquete

Después de extraer el `.zip`, encontrarás:

```
📁 Extractor_Empresas_APE_CBA/
├── 📄 ExtractorEmpresasAPE.exe        ← Archivo principal (ejecutar este)
├── 📁 Reportes/                       ← Los reportes se guardan aquí
├── 📁 Logs/                           ← Registros de actividad
└── 📄 README.md                       ← Este archivo
```

#### 3️⃣ Ubicación Recomendada

Coloca la aplicación en una ubicación accesible:

```
📁 C:\Usuarios\TuNombre\Documentos\
   └── 📁 Herramientas_SENA\
       └── 📁 Extractor_Empresas_APE_CBA\
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
- Usuario (Número de documento registrado en APE)
- Contraseña de acceso

La aplicación abrirá un diálogo para ingresar estas credenciales.

</td>
<td width="50%">

**🔒 Seguridad:**
- Las credenciales se guardan **localmente** en tu equipo
- Ubicación segura en archivos del sistema
- **Nunca** se envían a servidores externos
- Solo se usan para iniciar sesión en APE

</td>
</tr>
</table>

#### 2️⃣ Selección de Municipios

> 📍 **Municipios disponibles:** Solo los asignados al Centro de Biotecnología Agropecuaria (CBA) - Mosquera

La aplicación muestra únicamente los municipios de Cundinamarca que están bajo la cobertura del APE del CBA.

**Características:**
- ✅ Lista precargada y actualizada
- ✅ Selección múltiple
- ✅ Botón "Seleccionar todos"
- ✅ Contador de municipios seleccionados

**Si necesitas municipios de otro centro:**  
Esta versión no incluye municipios fuera de la cobertura del CBA. Consulta la sección [Roadmap y Versiones Futuras](#-roadmap-y-versiones-futuras) para más información.

---

## 📖 Cómo Usar la Aplicación

### Interfaz Principal

Al abrir la aplicación, verás una interfaz gráfica como esta:

<p align="center">
  <img src="https://i.ibb.co/Gv5M7DMQ/image.png" alt="Interfaz principal" width="500">
</p>

### Paso a Paso

#### Paso 1: Seleccionar Municipios

1. **Marca los municipios que deseas consultar:**
   - Haz clic en las casillas de verificación
   - O usa el botón **"Todos"** para seleccionar todos

2. **Verificar selección:**
   - El contador mostrará: `"X municipios seleccionados"`

> 💡 **Tip:** Si es tu primera vez, te recomendamos empezar con 2-3 municipios para familiarizarte con el proceso.

#### Paso 2: Verificar Credenciales

1. **Primera vez:**
   - Aparecerá una ventana emergente
   - Ingresa tu número de documento (usuario)
   - Ingresa tu contraseña de APE
   - Clic en **"Guardar"**

2. **Ya configuradas:**
   - Verás un recuadro con tus credenciales
   - Puedes editarlas si es necesario
   - No necesitas hacer nada más si son correctas

#### Paso 3: Iniciar Extracción

1. **Clic en "▶️ Iniciar Extracción"**
2. **El proceso automático comienza:**
   - Se abre el navegador (Google Chrome)
   - Se inicia sesión en APE automáticamente
   - Se navega a cada municipio seleccionado
   - Se extraen datos de todas las empresas
   - Se genera un archivo Excel por municipio

3. **⚠️ IMPORTANTE - NO INTERACTÚES CON EL NAVEGADOR:**
   - Deja que la aplicación trabaje sola
   - Puedes minimizar la ventana del navegador
   - **No cierres el navegador manualmente**
   - **No hagas clic en la ventana del navegador**

#### Paso 4: Monitorear el Progreso

Durante la extracción verás en la interfaz:

```
┌────────────────────────────────────────────────────┐
│  🔄 Proceso en Ejecución                           │
├────────────────────────────────────────────────────┤
│                                                    │
│  📍 Municipio actual: Mosquera (2/5)              │
│  🏢 Empresas extraídas: 47                         │
│                                                    │
│  📊 Estado: Extrayendo datos...                    │
│  ⏱️ Tiempo transcurrido: 1:23                      │
│                                                    │
└────────────────────────────────────────────────────┘
```

#### Paso 5: Revisar Resultados

Al finalizar, la aplicación mostrará:

```
╔════════════════════════════════════════════════════╗
║  ✅ EXTRACCIÓN COMPLETADA                          ║
╠════════════════════════════════════════════════════╣
║                                                    ║
║  📊 Resumen:                                       ║
║  ────────────────────────────────────────          ║
║  Municipios procesados:        5                   ║
║  Empresas totales extraídas:   247                 ║
║  Archivos generados:           5                   ║
║  Tiempo total:                 6 min 15 seg        ║
║                                                    ║
║  📁 Ubicación de reportes:                         ║
║  Reportes/REPORTE_EMPRESAS - 2024-11/             ║
║                                                    ║
║  [📂 Abrir Carpeta] [✓ Cerrar]                    ║
╚════════════════════════════════════════════════════╝
```

---

## 📊 Estructura de los Reportes

### Organización de Archivos

Los reportes se organizan automáticamente por **año** y **mes**:

```
📁 Reportes/
├── 📁 REPORTE_EMPRESAS - 2024-10/
│   ├── 📄 Mosquera_2024-10-15.xlsx
│   ├── 📄 Funza_2024-10-15.xlsx
│   └── 📄 Madrid_2024-10-15.xlsx
│
├── 📁 REPORTE_EMPRESAS - 2024-11/
│   ├── 📄 Mosquera_2024-11-26.xlsx
│   ├── 📄 Facatativa_2024-11-26.xlsx
│   └── 📄 Chia_2024-11-26.xlsx
│
└── 📁 REPORTE_EMPRESAS - 2025-01/
    └── 📄 Mosquera_2025-01-10.xlsx
```

### Contenido de los Archivos Excel

Cada archivo Excel contiene las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| **Tipo ID** | Tipo de identificación | NIT |
| **Identificación** | Número de identificación tributaria | 900123456-7 |
| **Actividad Económica** | Sector al que se dedica | Comercio al por menor |
| **Fecha de Inscripción** | Día de registro en APE | 2009-04-27 |
| **Estado** | Estado actual de la empresa | Activa / Temporalmente Inactiva / Extinta |

### Formato del Archivo

- **Nombre:** `{Municipio}_{YYYY-MM-DD}.xlsx`
- **Formato:** Excel (.xlsx) compatible con Office 2010+
- **Hojas:** Una hoja por archivo con el nombre del municipio
- **Encabezados:** Primera fila con nombres de columnas en negrita

### Características Adicionales

✅ **Sin duplicados**: La aplicación elimina empresas repetidas  
✅ **Validación de datos**: Verifica campos críticos antes de exportar  
✅ **Formato de fecha**: YYYY-MM-DD para ordenamiento automático  
✅ **Autoajuste de columnas**: Anchos optimizados para lectura

---

## ❓ Preguntas Frecuentes

<details>
<summary><strong>¿Esta versión funciona para mi centro SENA?</strong></summary>

**Solo si eres del Centro de Biotecnología Agropecuaria (CBA) de Mosquera, Cundinamarca.**

Si eres de otro centro:
1. Consulta la sección [Roadmap y Versiones Futuras](#-roadmap-y-versiones-futuras)
2. Contáctanos para solicitar una versión para tu centro
3. Proporciona la lista de municipios que cubre tu centro

Estamos trabajando en una versión multi-centro que incluirá selector de centro SENA.
</details>

<details>
<summary><strong>¿Puedo agregar municipios que no están en la lista?</strong></summary>

**No en esta versión.**

La lista de municipios está predefinida y corresponde a los asignados al CBA. Si un municipio que necesitas no aparece:
- Verifica que esté dentro de la cobertura del CBA
- Si es de otro centro, espera la versión multi-centro
- Contáctanos para reportar municipios faltantes del CBA
</details>

<details>
<summary><strong>¿Necesito instalar Python u otros programas?</strong></summary>

**No.** El archivo `.exe` incluye todo lo necesario:
- Python embebido
- Selenium WebDriver
- Pandas para procesamiento de datos
- CustomTkinter para la interfaz gráfica
- WebDriver Manager para gestión de drivers

Solo necesitas tener **Google Chrome** instalado.
</details>

<details>
<summary><strong>¿Cuántos municipios puedo procesar a la vez?</strong></summary>

**No hay límite técnico**, pero recomendamos:
- ✅ **1-10 municipios**: Proceso rápido (3-10 minutos)
- ⚠️ **10-20 municipios**: Proceso medio (10-25 minutos)
- ❌ **+20 municipios**: Dividir en lotes para facilitar seguimiento

El CBA tiene aproximadamente 15-20 municipios asignados.
</details>

<details>
<summary><strong>¿Qué pasa si se interrumpe el proceso?</strong></summary>

Si el proceso se interrumpe:
1. **Los reportes ya generados se conservan** en sus carpetas
2. Puedes **reiniciar** seleccionando solo los municipios faltantes
3. La aplicación **no sobreescribe archivos** del mismo día
4. Revisa los logs para ver el último municipio procesado
</details>

<details>
<summary><strong>¿Los datos extraídos son exactos?</strong></summary>

**Sí.** La aplicación extrae datos exactamente como aparecen en APE. Sin embargo:
- La calidad depende de los datos originales en APE
- Algunas empresas pueden tener campos vacíos
- La aplicación registra advertencias en los logs cuando encuentra datos incompletos
</details>

<details>
<summary><strong>¿Puedo ejecutar la aplicación en horario laboral?</strong></summary>

**Sí, pero considera:**
- La aplicación consume recursos del navegador
- Puedes minimizar la ventana y continuar trabajando
- El proceso no afecta otras aplicaciones
- Recomendamos ejecutarla en tiempos de menor carga
</details>

<details>
<summary><strong>¿Qué hago si un municipio no tiene empresas registradas?</strong></summary>

La aplicación:
1. Detecta que no hay empresas
2. Genera un archivo Excel vacío (solo encabezados)
3. Registra en el log: `"0 empresas encontradas en [Municipio]"`

Esto es normal para municipios pequeños o sin empresas registradas.
</details>

<details>
<summary><strong>¿Cuándo estará disponible la versión multi-centro?</strong></summary>

La versión 1.5 con selector de centros está planeada para el **Q1 2025**.

Para acelerar el desarrollo, necesitamos que otros centros SENA nos proporcionen su lista de municipios. ¡Contáctanos si quieres contribuir!
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
   - Abre Chrome
   - Ve a la plataforma APE
   - Intenta iniciar sesión con tus datos

2. **Actualiza las credenciales en la app:**
   - Edita el campo de credenciales
   - Ingresa nuevamente usuario (número de documento)
   - Ingresa contraseña
   - Guarda cambios

3. **Verifica que tu cuenta esté activa:**
   - Contacta soporte de APE si no puedes acceder

---

### Problema 3: El navegador se cierra inesperadamente

**Síntomas:**
- Chrome se abre y se cierra inmediatamente
- Error: "WebDriver session not found"

**Solución:**

1. **Actualiza Google Chrome:**
   - Menú (⋮) → Ayuda → Información de Google Chrome
   - Espera actualización automática
   - Reinicia Chrome

2. **Descarga la última versión del ejecutable:**
   - Las nuevas versiones incluyen ChromeDriver actualizado
   - Verifica en Releases la última versión

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
   - Clic derecho en carpeta de la aplicación
   - **Propiedades** → **Seguridad**
   - Tu usuario debe tener permisos de "Modificar"

2. **Revisa los logs:**
   ```
   Logs/app.log
   ```
   - Busca mensajes de error

3. **Ejecuta desde otra ubicación:**
   - Mueve toda la carpeta a `Documentos/`
   - Evita `Archivos de Programa/`

---

### Problema 5: Extracción muy lenta

**Síntomas:**
- El proceso tarda más de lo esperado
- El navegador se congela

**Solución:**

1. **Verifica conexión a internet:**
   - Velocidad recomendada: mínimo 5 Mbps
   - Ping estable a APE

2. **Cierra aplicaciones pesadas:**
   - Otros navegadores
   - Programas de edición

3. **Procesa menos municipios:**
   - En lugar de 15, procesa de 5 en 5

4. **Limpia caché de Chrome:**
   - Ctrl + Shift + Supr
   - Elimina caché e historial

---

### Problema 6: "Mi municipio no aparece en la lista"

**Síntomas:**
- El municipio que necesitas no está disponible
- Lista de municipios incompleta

**Posibles causas y soluciones:**

**Causa 1: El municipio no pertenece al CBA**
- Verifica que el municipio esté en la cobertura del CBA - Mosquera
- Si es de otro centro, espera la versión multi-centro

**Causa 2: Error en la configuración**
- Reporta el municipio faltante a: sergiogarcia3421@gmail.com
- Proporciona el nombre exacto del municipio
- Confirma que es de Cundinamarca

**Causa 3: Municipio agregado recientemente**
- Descarga la última versión del ejecutable
- Verifica el changelog de la versión

---

## 🏗️ Arquitectura Técnica

### Diseño del Sistema

La aplicación sigue una arquitectura modular de **separación de responsabilidades**:

```
┌─────────────────────────────────────────────────┐
│       GUI Layer (CustomTkinter)                 │
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
│  - Municipalities List (CBA only)               │
│  - URLs                                         │
└─────────────────────────────────────────────────┘
```

### Estructura de Directorios (Código Fuente)

```
📁 extractor-empresas-ape/
│
├── 📄 main.py                          # Punto de entrada
│
├── 📁 config/                          # Configuración
│   ├── __init__.py
│   ├── logging_config.py               # Sistema de logs
│   ├── municipalities.py               # Lista CBA (editable)
│   └── settings.py                     # Constantes globales
│
├── 📁 core/                            # Componentes fundamentales
│   ├── __init__.py
│   ├── base_extractor.py               # Clase abstracta
│   └── driver_manager.py               # Gestión de WebDriver
│
├── 📁 gui/                             # Interfaz de usuario
│   ├── __init__.py
│   ├── main_window.py                  # Ventana principal
│   └── dialogs/
│       ├── __init__.py
│       ├── conflict_dialog.py
│       └── credentials_dialog.py
│
├── 📁 modules/                         # Módulos de orquestación
│   ├── __init__.py
│   ├── authentication.py               # Login en APE
│   ├── navigation.py                   # Navegación
│   ├── data_extraction.py              # Extracción de datos
│   └── export_handler.py               # Exportación a Excel
│
├── 📁 urls/                            # URLs centralizadas
│   ├── __init__.py
│   └── urls.py
│
├── 📁 utils/                           # Utilidades
│   ├── __init__.py
│   ├── credentials.py
│   ├── helpers.py
│   ├── selectors.py
│   └── validator_file.py
│
├── 📁 Reportes/                        # Reportes generados
├── 📁 Logs/                            # Logs de aplicación
│
├── 📄 requirements.txt
├── 📄 build_spec.spec
└── 📄 README.md
```

### Flujo de Ejecución

```
1. main.py
   ↓
2. Inicializa GUI (CustomTkinter)
   ↓
3. Usuario selecciona municipios (lista CBA)
   ↓
4. Usuario inicia extracción
   ↓
5. DriverManager.initialize()
   ↓
6. Authentication.login()
   ↓
7. Para cada municipio:
   ├─ Navigation.go_to_municipality()
   ├─ DataExtractor.extract_companies()
   └─ ExportHandler.export_to_excel()
   ↓
8. DriverManager.quit()
   ↓
9. Muestra resumen final
```

### Tecnologías Utilizadas

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| **Python** | Lenguaje base | 3.10+ |
| **Selenium** | Automatización web | 4.x |
| **CustomTkinter** | Interfaz gráfica moderna | 5.2+ |
| **Pandas** | Procesamiento de datos | 2.x |
| **WebDriver Manager** | Gestión de drivers | 3.x |
| **openpyxl** | Escritura Excel | 3.x |
| **PyInstaller** | Compilación a .exe | 5.x |

---

## 👨‍💻 Para Desarrolladores

### Configuración del Entorno de Desarrollo

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/SergioAndresG/obtener_empresas.git
cd obtener_empresas
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

### Agregar Municipios

Para agregar municipios del CBA, edita:

```python
# config/municipalities.py

LIST_MUNICIPALITIES = (
    "Mosquera",
    "Funza",
    "Madrid",
    "Facatativá",
    # Agrega aquí nuevos municipios del CBA
    "Nuevo Municipio",
)
```

### Compilar el Ejecutable

```bash
# Instalar PyInstaller
pip install pyinstaller

# Compilar
pyinstaller build_spec.spec

# El ejecutable estará en:
# dist/ExtractorEmpresasAPE.exe
```

### Contribuir al Proyecto

#### Proceso de Contribución

1. **Fork** el repositorio
2. Crea una rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Haz tus cambios
4. Commit con mensajes descriptivos:
   ```bash
   git commit -m "Add: municipios faltantes del CBA"
   ```
5. Push a tu fork:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
6. Abre un **Pull Request**

#### Convenciones de Código

**Estilo Python:**
- Sigue **PEP 8**
- Usa **type hints**
- Documenta con **docstrings**

**Estructura de commits:**
```
Add: nueva funcionalidad
Fix: corrección de bug
Update: actualización de funcionalidad
Refactor: refactorización
Docs: cambios en documentación
```

---

## 📧 Contacto y Soporte

### ¿Necesitas ayuda?

- 🐛 **Reportar bugs**: [Issues del repositorio](https://github.com/SergioAndresG/obtener_empresas/issues)
- 💡 **Sugerencias**: [Discussions](https://github.com/SergioAndresG/obtener_empresas/discussions)
- 📧 **Contacto directo**: sergiogarcia3421@gmail.com

### Para Otros Centros SENA

Si eres de otro centro y quieres esta herramienta:

**Envía un correo con:**
```
Asunto: Solicitud Extractor Empresas APE - [Nombre de tu Centro]

Información:
- Nombre del Centro: _______________________________
- Ciudad: _________________________________________
- Regional: _______________________________________
- Municipios de cobertura APE: (lista completa)
```

---

## 📊 Estadísticas de Uso

### Centro de Biotecnología Agropecuaria

| Métrica | Valor |
|---------|-------|
| ⏱️ **Tiempo ahorrado** | ~90% de reducción |
| 📊 **Empresas procesadas** | +1,000 empresas |
| 🗺️ **Municipios cubiertos** | 15 municipios |
| 👥 **Usuarios activos** | 5 funcionarios |
| 📅 **Reportes generados** | 80+ archivos |

---

<p align="center">
  <strong>Desarrollado con ❤️ para optimizar procesos administrativos del SENA</strong>
</p>

<p align="center">
  <sub>Versión 1.0 - Centro de Biotecnología Agropecuaria (CBA) - Mosquera, Cundinamarca</sub>
</p>

<p align="center">
  <sub>Herramienta de extracción automatizada que convierte horas de trabajo manual en minutos</sub>
</p>

<p align="center">
  <a href="#-tabla-de-contenidos">⬆️ Volver arriba</a>
</p>
