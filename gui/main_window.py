import customtkinter as ctk
from tkinter import messagebox
import threading
from core.base_extractor import ExtractorDatosEmpresa
from urls.urls import URL_LOGIN
from config.logging_config import configurar_logging
from config.municipalities import municipios_cobertura


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuración de la Ventana Principal ---
        self.title("Extractor de Empresas - SENA")
        self.geometry("800x600")
        
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

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

    def iniciar_busqueda(self):
        """Inicia el proceso de extracción en un thread separado"""
        municipios_seleccionados = self.obtener_municipios_seleccionados()
        
        # Validar que haya al menos uno seleccionado
        if not municipios_seleccionados:
            messagebox.showwarning(
                "Sin selección",
                "Debes seleccionar al menos un municipio"
            )
            return
        
        # Deshabilitar botón durante la ejecución
        self.boton_buscar.configure(state="disabled", text="⏳ Procesando...")
        self.log(f"\n{'='*60}")
        self.log(f"Iniciando extracción de {len(municipios_seleccionados)} municipio(s)")
        self.log(f"{'='*60}\n")
        
        # Ejecutar en thread separado para no congelar la UI
        thread = threading.Thread(
            target=self._ejecutar_extraccion,
            args=(municipios_seleccionados,),
            daemon=True
        )
        thread.start()

    def _ejecutar_extraccion(self, municipios):
        """Ejecuta la extracción en background"""
        try:
            configurar_logging()
            
            # Crear extractor y ejecutar
            extractor = ExtractorDatosEmpresa()
            exito = extractor.ejecutar_proceso_completo(municipios, URL_LOGIN)
            
            # Mostrar resultado final
            if exito:
                self.log(f"\nProceso completado exitosamente")
                messagebox.showinfo(
                    "Éxito", 
                    f"Extracción completada para {len(municipios)} municipio(s)"
                )
            else:
                self.log(f"\nEl proceso finalizó con errores")
                messagebox.showerror(
                    "Error", 
                    "Hubo errores durante la extracción. Revisa los logs."
                )
                
        except Exception as e:
            self.log(f"\nError crítico: {str(e)}")
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
            
        finally:
            # Re-habilitar botón
            self.boton_buscar.configure(state="normal", text="🚀 Iniciar Extracción")


if __name__ == "__main__":
    app = App()
    app.mainloop()