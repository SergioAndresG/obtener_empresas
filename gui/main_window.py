import json
import customtkinter as ctk
from pathlib import Path
from tkinter import messagebox
import threading
from core.base_extractor import ExtractorDatosEmpresa
from urls.urls import URL_LOGIN
from config.logging_config import configurar_logging
from config.municipalities import municipios_cobertura
from .dialogs.conflict_dialog import ConflictDialog
from utils.validator_file import FileValidator
from config import settings
# ========= LIBRERIAS LOCALES QUE MANEJAN LAS CREDENCIALES ==========
from utils.credentials import CredentialsManager
from .dialogs.credentials_dialog import CredentialsDialog

class App(ctk.CTk):
    def __init__(self, credentials_manager = None):
        super().__init__()

        # --- Configuración de la Ventana Principal ---
        self.title("Extractor de Empresas - SENA")
        self.geometry("800x600")

        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        if credentials_manager:
            self.credentials_manager = credentials_manager
        else:
            self.credentials_manager = CredentialsManager()
            settings.set_credentials_manager(self.credentials_manager)

        # Crear interfaz
        self._crear_interfaz()

        # --- Frame Izquierdo: Selección de Municipios ---
        self.frame_seleccion = ctk.CTkFrame(self)
        self.frame_seleccion.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        # Título
        ctk.CTkLabel(
            self.frame_seleccion, 
            text="Seleccionar Municipios", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Botones de selección rápida
        frame_botones_rapidos = ctk.CTkFrame(self.frame_seleccion)
        frame_botones_rapidos.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            frame_botones_rapidos, 
            text="✓ Todos", 
            command=self.seleccionar_todos,
            width=70
        ).pack(side="left", padx=2)
        
        ctk.CTkButton(
            frame_botones_rapidos, 
            text="✗ Ninguno", 
            command=self.deseleccionar_todos,
            width=70
        ).pack(side="left", padx=2)
        
        # Frame scrollable para checkboxes
        self.scroll_frame = ctk.CTkScrollableFrame(self.frame_seleccion, height=400)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Crear checkboxes para cada municipio
        self.checkboxes = {}
        for municipio in municipios_cobertura:
            var = ctk.BooleanVar(value=True)  # Todos marcados por defecto
            checkbox = ctk.CTkCheckBox(
                self.scroll_frame, 
                text=municipio, 
                variable=var,
                font=("Arial", 12)
            )
            checkbox.pack(anchor="w", pady=2, padx=5)
            self.checkboxes[municipio] = var
        
        # --- Frame Derecho: Controles y Resultados ---
        frame_derecho = ctk.CTkFrame(self)
        frame_derecho.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        frame_derecho.grid_rowconfigure(2, weight=1)
        frame_derecho.grid_columnconfigure(0, weight=1)
        
        # Contador de seleccionados
        self.label_contador = ctk.CTkLabel(
            frame_derecho,
            text=f"Municipios seleccionados: {len(municipios_cobertura)}",
            font=("Arial", 12)
        )
        self.label_contador.grid(row=0, column=0, pady=10, sticky="n")
        
        # Actualizar contador cuando cambie selección
        for var in self.checkboxes.values():
            var.trace_add("write", lambda *args: self.actualizar_contador())
        
        # Botón de inicio
        self.boton_buscar = ctk.CTkButton(
            frame_derecho, 
            text="🚀 Iniciar Extracción",
            command=self.iniciar_busqueda,
            height=40,
            font=("Arial", 14, "bold"),
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.boton_buscar.grid(row=1, column=0, pady=20, padx=20)
        
        # Caja de texto para logs
        self.textbox_resultados = ctk.CTkTextbox(
            frame_derecho, 
            state="disabled",
            font=("Consolas", 10),
            height=100
        )
        self.textbox_resultados.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    def actualizar_contador(self):
        """Actualiza el contador de municipios seleccionados"""
        seleccionados = sum(1 for var in self.checkboxes.values() if var.get())
        self.label_contador.configure(text=f"Municipios seleccionados: {seleccionados}")

    def seleccionar_todos(self):
        """Marca todos los checkboxes"""
        for var in self.checkboxes.values():
            var.set(True)

    def deseleccionar_todos(self):
        """Desmarca todos los checkboxes"""
        for var in self.checkboxes.values():
            var.set(False)

    def obtener_municipios_seleccionados(self):
        """Retorna lista de municipios seleccionados"""
        return [
            municipio 
            for municipio, var in self.checkboxes.items() 
            if var.get()
        ]

    def log(self, mensaje):
        """Función para añadir mensajes a la caja de texto"""
        self.textbox_resultados.configure(state="normal")
        self.textbox_resultados.insert("end", mensaje + "\n")
        self.textbox_resultados.configure(state="disabled")
        self.textbox_resultados.see("end")

    def _verificar_credenciales_iniciales(self):
        """Verifica si existen credenciales al iniciar la app"""
        if not self.credentials_manager.credentials_exist():
            # Primera vez - Solicitar credenciales
            messagebox.showinfo(
                "Bienvenido",
                "Es la primera vez que usas la aplicación.\n\n"
                "Por favor, configura tus credenciales de acceso."
            )
            self._mostrar_dialogo_credenciales()
        else:
            # Validar que las credenciales sean correctas
            if not self.credentials_manager.validate_credentials():
                messagebox.showwarning(
                    "Credenciales Inválidas",
                    "Las credenciales guardadas están corruptas.\n"
                    "Por favor, vuelve a ingresarlas."
                )
                self._mostrar_dialogo_credenciales()
    
    def _mostrar_dialogo_credenciales(self):
        """Muestra el diálogo de credenciales"""
        dialog = CredentialsDialog(self, self.credentials_manager)
        self.wait_window(dialog)
        
        if not dialog.result:
            # Usuario canceló - cerrar aplicación
            respuesta = messagebox.askyesno(
                "Cerrar Aplicación",
                "Sin credenciales no se puede usar la aplicación.\n"
                "¿Deseas cerrar?"
            )
            if respuesta:
                self.destroy()
    
    def _crear_interfaz(self):
        """Crea toda la interfaz gráfica"""
        
        # --- Frame Izquierdo: Selección de Municipios ---
        self.frame_seleccion = ctk.CTkFrame(self)
        self.frame_seleccion.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        # Título
        ctk.CTkLabel(
            self.frame_seleccion, 
            text="Seleccionar Municipios", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Botones de selección rápida
        frame_botones_rapidos = ctk.CTkFrame(self.frame_seleccion)
        frame_botones_rapidos.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(
            frame_botones_rapidos, 
            text="✓ Todos", 
            command=self.seleccionar_todos,
            width=70
        ).pack(side="left", padx=2)
        
        ctk.CTkButton(
            frame_botones_rapidos, 
            text="✗ Ninguno", 
            command=self.deseleccionar_todos,
            width=70
        ).pack(side="left", padx=2)
        
        # Frame scrollable para checkboxes
        self.scroll_frame = ctk.CTkScrollableFrame(self.frame_seleccion, height=400)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Crear checkboxes para cada municipio
        self.checkboxes = {}
        for municipio in municipios_cobertura:
            var = ctk.BooleanVar(value=True)
            checkbox = ctk.CTkCheckBox(
                self.scroll_frame, 
                text=municipio, 
                variable=var,
                font=("Arial", 12)
            )
            checkbox.pack(anchor="w", pady=2, padx=5)
            self.checkboxes[municipio] = var
        
        # --- Frame Derecho: Controles y Resultados ---
        frame_derecho = ctk.CTkFrame(self)
        frame_derecho.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        frame_derecho.grid_rowconfigure(3, weight=1)
        frame_derecho.grid_columnconfigure(0, weight=1)
        
        # Contador de seleccionados
        self.label_contador = ctk.CTkLabel(
            frame_derecho,
            text=f"Municipios seleccionados: {len(municipios_cobertura)}",
            font=("Arial", 12)
        )
        self.label_contador.grid(row=0, column=0, pady=(20, 10), sticky="n")
        
        # Actualizar contador cuando cambie selección
        for var in self.checkboxes.values():
            var.trace_add("write", lambda *args: self.actualizar_contador())
        
        # ✅ Botón de configuración de credenciales
        ctk.CTkButton(
            frame_derecho,
            text="⚙️ Configurar Credenciales",
            command=self._mostrar_dialogo_credenciales,
            fg_color="#5D5D5D",
            hover_color="#4A4A4A",
            height=30,
            width=180
        ).grid(row=1, column=0, pady=(0, 10))
        
        # Botón de inicio
        self.boton_buscar = ctk.CTkButton(
            frame_derecho, 
            text="🚀 Iniciar Extracción",
            command=self.iniciar_busqueda,
            height=40,
            font=("Arial", 14, "bold"),
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.boton_buscar.grid(row=2, column=0, pady=(10, 20), padx=20)
        
        # Caja de texto para logs
        self.textbox_resultados = ctk.CTkTextbox(
            frame_derecho, 
            state="disabled",
            font=("Consolas", 10)
        )
        self.textbox_resultados.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    def iniciar_busqueda(self):
        """Inicia el proceso de extracción con validación previa"""
        municipios_seleccionados = self.obtener_municipios_seleccionados()
        
        # Validar que haya al menos uno seleccionado
        if not municipios_seleccionados:
            messagebox.showwarning(
                "Sin selección",
                "Debes seleccionar al menos un municipio"
            )
            return
        
        # PRE-VALIDACIÓN: Verificar archivos existentes
        self.log(f"\nVerificando archivos existentes...")
        validacion = FileValidator.verificar_archivos_existentes(municipios_seleccionados)
        
        # Si hay archivos existentes, mostrar diálogo
        if validacion['existentes']:
            self._manejar_conflictos(validacion, municipios_seleccionados)
        else:
            # No hay conflictos, proceder directamente
            self.log(f"No hay conflictos. Iniciando extracción...")
            self._iniciar_extraccion(municipios_seleccionados)
    
    def _manejar_conflictos(self, validacion, municipios_seleccionados):
        """
        Maneja los conflictos de archivos existentes
        
        Args:
            validacion: Resultado de FileValidator.verificar_archivos_existentes
            municipios_seleccionados: Lista de municipios a procesar
        """
        # Mostrar diálogo de conflictos
        dialog = ConflictDialog(
            self, 
            validacion['existentes'],
            validacion['nuevos']
        )
        self.wait_window(dialog)  # Esperar a que el usuario decida
        
        resultado = dialog.get_resultado()
        
        if resultado == 'sobrescribir':
            # Eliminar archivos existentes
            self.log(f"\nEliminando {len(validacion['existentes'])} archivo(s) existente(s)...")
            
            eliminacion = FileValidator.eliminar_archivos(validacion['existentes'])
            
            if eliminacion['errores']:
                self.log(f"❌ Errores al eliminar archivos:")
                for error in eliminacion['errores']:
                    self.log(f"   • {error}")
                
                messagebox.showerror(
                    "Error",
                    f"No se pudieron eliminar algunos archivos.\n"
                    f"Verifica que no estén abiertos en otra aplicación."
                )
                return
            
            self.log(f"✅ {eliminacion['eliminados']} archivo(s) eliminado(s)")
            self.log(f"🚀 Iniciando extracción completa...")
            
            # Extraer todos los municipios
            self._iniciar_extraccion(municipios_seleccionados)
            
        elif resultado == 'omitir':
            # Extraer solo los nuevos
            if validacion['nuevos']:
                self.log(f"\n⏭️ Omitiendo {len(validacion['existentes'])} archivo(s) existente(s)")
                self.log(f"Extrayendo {len(validacion['nuevos'])} municipio(s) nuevo(s)...")
                self._iniciar_extraccion(validacion['nuevos'])
            else:
                self.log(f"\nNo hay archivos nuevos para extraer")
                messagebox.showinfo(
                    "Sin Archivos Nuevos",
                    "Todos los archivos ya existen.\n"
                    "No hay nada nuevo que extraer."
                )
        
        elif resultado == 'cancelar':
            self.log(f"\n❌ Extracción cancelada por el usuario")



    def _iniciar_extraccion(self, municipios):
        """
        Prepara y ejecuta la extracción en background
        
        Args:
            municipios: Lista de municipios a procesar
        """
        # Deshabilitar botón durante la ejecución
        self.boton_buscar.configure(state="disabled", text="⏳ Procesando...")
        self.log(f"\n{'='*60}")
        self.log(f"Iniciando extracción de {len(municipios)} municipio(s)")
        self.log(f"{'='*60}\n")
        
        # Ejecutar en thread separado para no congelar la UI
        thread = threading.Thread(
            target=self._ejecutar_extraccion,
            args=(municipios,),
            daemon=True
        )
        thread.start()
    
    def _ejecutar_extraccion(self, municipios):
        """Ejecuta la extracción en background"""
        try:
            configurar_logging()
            
            # Crear extractor y ejecutar
            extractor = ExtractorDatosEmpresa()
            resultado = extractor.ejecutar_proceso_completo(municipios, URL_LOGIN)
            
            # Procesar resultado detallado
            self._mostrar_resultado(resultado, len(municipios))
                
        except Exception as e:
            self.log(f"\nError crítico: {str(e)}")
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
            
        finally:
            # Re-habilitar botón
            self.boton_buscar.configure(state="normal", text="🚀 Iniciar Extracción")
    
    def _mostrar_resultado(self, resultado, total_municipios):
        """
        Muestra un resumen detallado del resultado de la extracción
        
        Args:
            resultado: Diccionario con los resultados
            total_municipios: Total de municipios solicitados
        """
        self.log(f"\n{'='*60}")
        self.log("RESUMEN DE LA EXTRACCIÓN")
        self.log(f"{'='*60}")
        
        # Municipios procesados exitosamente
        procesados = resultado["municipios_procesados"]
        self.log(f"Procesados exitosamente: {procesados}/{total_municipios}")
        
        # Municipios omitidos
        if resultado["municipios_omitidos"]:
            self.log(f"\nMunicipios omitidos/sin datos ({len(resultado['municipios_omitidos'])}):")
            for municipio in resultado["municipios_omitidos"]:
                self.log(f"   • {municipio}")
        
        # Errores
        if resultado["errores"]:
            self.log(f"\nErrores encontrados ({len(resultado['errores'])}):")
            for error in resultado["errores"]:
                self.log(f"   • {error}")
        
        self.log(f"\n{'='*60}")
        
        # Mensaje final
        if resultado["exitoso"] and procesados > 0:
            mensaje = f"Extracción completada exitosamente:\n\n"
            mensaje += f"{procesados} archivo(s) creado(s)\n"
            
            if resultado["municipios_omitidos"]:
                mensaje += f"⚠️ {len(resultado['municipios_omitidos'])} municipio(s) sin datos\n"
            
            messagebox.showinfo("Proceso Completado", mensaje)
        elif procesados == 0:
            messagebox.showwarning(
                "Sin Datos",
                "No se crearon archivos nuevos.\n"
                "Revisa los logs para más detalles."
            )
        else:
            messagebox.showerror(
                "Error en la Extracción",
                f"El proceso finalizó con errores.\n\n"
                f"Revisa los logs para más detalles."
            )

if __name__ == "__main__":
    app = App()
    app.mainloop()