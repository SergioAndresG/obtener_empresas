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
        # GUI - CustomTkinter
        'customtkinter',
        'tkinter',
        '_tkinter',
        
        # Selenium
        'selenium',
        'selenium.webdriver',
        'selenium.webdriver.chrome.service',
        'selenium.webdriver.chrome.options',
        'selenium.webdriver.common.by',
        'selenium.webdriver.support',
        'selenium.webdriver.support.ui',
        'selenium.webdriver.support.expected_conditions',
        'selenium.common.exceptions',
        
        # HTTP
        'httpcore',
        
        # ✅ NUMPY - Pandas lo necesita
        'numpy',
        'numpy.core',
        'numpy.core._multiarray_umath',
        
        # Excel y Pandas
        'pandas',
        'pandas._libs',
        'pandas._libs.tslibs',
        'openpyxl',
        'openpyxl.styles',
        'openpyxl.utils',
        'openpyxl.workbook',
        'openpyxl.worksheet',
        
        # Módulos del proyecto
        'core',
        'core.driver_manager',
        'core.base_extractor',
        'modules',
        'modules.authentication',
        'modules.navigation',
        'modules.data_extraction',
        'modules.export_handler',
        'utils',
        'utils.selectors',
        'utils.helpers',
        'utils.file_validator',
        'utils.credentials_manager',
        'gui',
        'gui.main_window',
        'gui.dialogs',
        'gui.dialogs.conflict_dialog',
        'gui.dialogs.credentials_dialog',
        
        # Sistema
        'json',
        'base64',
        'logging',
        'datetime',
        'os',
        'traceback',
        'threading',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'scipy',
        'PIL',
        'test',
        'unittest',
        'pytest',
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ExtractorEmpresas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # False = No muestra ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='icon.ico',  # Descomenta si tienes un icono
)