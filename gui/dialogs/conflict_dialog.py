"""
Diálogo personalizado para manejar conflictos de archivos
"""
import customtkinter as ctk
from tkinter import messagebox


class ConflictDialog(ctk.CTkToplevel):
    """Diálogo para manejar archivos existentes"""
    
    def __init__(self, parent, archivos_existentes, archivos_nuevos):
        super().__init__(parent)
        
        self.archivos_existentes = archivos_existentes
        self.archivos_nuevos = archivos_nuevos
        self.resultado = None  # 'sobrescribir', 'omitir', 'cancelar'
        
        self._setup_window()
        self._create_widgets()
        
        # Hacer la ventana modal
        self.transient(parent)
        self.grab_set()
        self.focus()
        
        # Centrar ventana
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (self.winfo_width() // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
    
    def _setup_window(self):
        """Configura la ventana del diálogo"""
        self.title("⚠️ Archivos Existentes")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
    
    def _create_widgets(self):
        """Crea los widgets del diálogo"""
        
        # Frame superior - Información
        frame_info = ctk.CTkFrame(self, fg_color="transparent")
        frame_info.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        # Mensaje principal
        mensaje = (
            f"Se encontraron {len(self.archivos_existentes)} archivo(s) existente(s)\n"
            f"y {len(self.archivos_nuevos)} archivo(s) nuevo(s)."
        )
        
        ctk.CTkLabel(
            frame_info,
            text=mensaje,
            font=("Arial", 13),
            wraplength=450
        ).pack(pady=(0, 10))
        
        ctk.CTkLabel(
            frame_info,
            text="¿Qué deseas hacer con los archivos existentes?",
            font=("Arial", 12, "bold")
        ).pack()
        
        # Frame medio - Lista de archivos existentes
        frame_lista = ctk.CTkFrame(self)
        frame_lista.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        frame_lista.grid_columnconfigure(0, weight=1)
        frame_lista.grid_rowconfigure(1, weight=1)
        
        ctk.CTkLabel(
            frame_lista,
            text="Archivos existentes:",
            font=("Arial", 12, "bold"),
            anchor="w"
        ).grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        
        # Textbox con lista scrollable
        textbox = ctk.CTkTextbox(
            frame_lista,
            height=150,
            font=("Consolas", 11),
            state="normal"
        )
        textbox.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        
        for municipio in self.archivos_existentes:
            textbox.insert("end", f"  • {municipio}\n")
        
        textbox.configure(state="disabled")
        
        # Frame inferior - Botones
        frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        frame_botones.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")
        frame_botones.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Botón Sobrescribir
        btn_sobrescribir = ctk.CTkButton(
            frame_botones,
            text="🔄 Sobrescribir",
            command=self._sobrescribir,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            height=40,
            font=("Arial", 12, "bold")
        )
        btn_sobrescribir.grid(row=0, column=0, padx=5)
        
        # Botón Omitir
        btn_omitir = ctk.CTkButton(
            frame_botones,
            text="⏭️ Omitir Existentes",
            command=self._omitir,
            fg_color="#f39c12",
            hover_color="#d68910",
            height=40,
            font=("Arial", 12, "bold")
        )
        btn_omitir.grid(row=0, column=1, padx=5)
        
        # Botón Cancelar
        btn_cancelar = ctk.CTkButton(
            frame_botones,
            text="❌ Cancelar Todo",
            command=self._cancelar,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=40,
            font=("Arial", 12, "bold")
        )
        btn_cancelar.grid(row=0, column=2, padx=5)
        
        # Texto explicativo
        ctk.CTkLabel(
            frame_botones,
            text="• Sobrescribir: Elimina archivos existentes y extrae de nuevo\n"
                 "• Omitir: Solo extrae los archivos nuevos\n"
                 "• Cancelar: No extrae nada",
            font=("Arial", 9),
            text_color="gray60",
            justify="left"
        ).grid(row=1, column=0, columnspan=3, pady=(10, 0))
    
    def _sobrescribir(self):
        """Usuario decide sobrescribir archivos existentes"""
        confirmar = messagebox.askyesno(
            "Confirmar Sobrescritura",
            f"¿Estás seguro de que deseas sobrescribir {len(self.archivos_existentes)} archivo(s)?\n\n"
            "Esta acción no se puede deshacer.",
            icon='warning',
            parent=self
        )
        
        if confirmar:
            self.resultado = 'sobrescribir'
            self.destroy()
    
    def _omitir(self):
        """Usuario decide omitir archivos existentes"""
        self.resultado = 'omitir'
        self.destroy()
    
    def _cancelar(self):
        """Usuario cancela la operación"""
        self.resultado = 'cancelar'
        self.destroy()
    
    def get_resultado(self):
        """Retorna el resultado de la decisión del usuario"""
        return self.resultado