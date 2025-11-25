import customtkinter as ctk
from tkinter import messagebox
from core.base_extractor import ExtractorDatosEmpresa
from urls.urls import URL_LOGIN
from config.logging_config import configurar_logging
from config.municipalities import municipios_cobertura


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuración de la Ventana Principal ---
        self.title("Extractor de Empresas")
        self.geometry("700x500")

        # --- Creación de Widgets (Componentes Visuales) ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Botón para iniciar la búsqueda
        self.boton_buscar = ctk.CTkButton(self, text="Iniciar Búsqueda", command=self.iniciar_busqueda)
        self.boton_buscar.grid(row=1, column=1, padx=20, pady=5)

        # Caja de texto para mostrar resultados y logs
        self.textbox_resultados = ctk.CTkTextbox(self, state="disabled")
        self.textbox_resultados.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="nsew")

    def log(self, mensaje):
        """Función para añadir mensajes a la caja de texto de resultados."""
        self.textbox_resultados.configure(state="normal")
        self.textbox_resultados.insert("end", mensaje + "\n")
        self.textbox_resultados.configure(state="disabled")
        self.textbox_resultados.see("end") # Auto-scroll hacia el final

    def iniciar_busqueda(self):
        """
        Esta es la función puente. Se ejecuta cuando el usuario pulsa el botón.
        Desde aquí, llamamos a la lógica de negocio en los otros módulos.
        """
        # Configurar logging
        configurar_logging()
        
        print("Iniciando el proceso de extracción de datos de empresas...")
        
        # Crear instancia del extractor
        extractor = ExtractorDatosEmpresa()
        
        # Ejecutar proceso completo
        extractor.ejecutar_proceso_completo(municipios_cobertura, URL_LOGIN)

if __name__ == "__main__":
    # Esto permite ejecutar este archivo directamente para probar la GUI
    app = App()
    app.mainloop()