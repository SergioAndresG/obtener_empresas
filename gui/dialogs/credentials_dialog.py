"""
Diálogo para gestión de credenciales
"""
import customtkinter as ctk
from tkinter import messagebox


class CredentialsDialog(ctk.CTkToplevel):
    """Ventana emergente para configurar credenciales"""
    
    def __init__(self, parent, credentials_manager):
        super().__init__(parent)
        self.credentials_manager = credentials_manager
        self.result = None
        
        self._setup_window()
        self._create_widgets()
        self._load_existing_credentials()
        self._center_window(parent)
    
    def _setup_window(self):
        """Configura la ventana"""
        self.title("Gestión de Acceso")
        self.geometry("420x400")
        self.resizable(False, False)
        self.configure(fg_color="#2B2B2B")
        
        # Hacer modal
        self.transient(self.master)
        self.grab_set()
        self.focus()
    
    def _create_widgets(self):
        """Crea los widgets del diálogo"""
        
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=(25, 15))
        
        ctk.CTkLabel(
            header_frame, 
            text="🔐 Credenciales SENA", 
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack()
        
        ctk.CTkLabel(
            header_frame, 
            text="Tus datos se guardan de forma segura en tu computadora", 
            font=ctk.CTkFont(size=11), 
            text_color="#A0A0A0",
            wraplength=350
        ).pack(pady=(5, 0))

        # Formulario
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=15, padx=35, fill="x")

        # Usuario
        ctk.CTkLabel(
            form_frame, 
            text="Usuario o Correo", 
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w"
        ).pack(anchor="w", pady=(0, 5))
        
        self.username_entry = ctk.CTkEntry(
            form_frame, 
            height=40, 
            placeholder_text="ejemplo@sena.edu.co",
            font=ctk.CTkFont(size=12)
        )
        self.username_entry.pack(fill="x", pady=(0, 20))

        # Contraseña
        ctk.CTkLabel(
            form_frame, 
            text="Contraseña", 
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w"
        ).pack(anchor="w", pady=(0, 5))
        
        self.password_entry = ctk.CTkEntry(
            form_frame, 
            height=40, 
            show="•", 
            placeholder_text="••••••••",
            font=ctk.CTkFont(size=12)
        )
        self.password_entry.pack(fill="x", pady=(0, 10))
        
        # Info adicional
        ctk.CTkLabel(
            form_frame,
            text="ℹ️ Estas credenciales se usan solo para acceder\nal sistema de extracción de datos.",
            font=ctk.CTkFont(size=10),
            text_color="#808080",
            justify="left"
        ).pack(anchor="w", pady=(5, 0))

        # Botones
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)

        ctk.CTkButton(
            btn_frame, 
            text="Cancelar", 
            command=self.cancel, 
            fg_color="transparent", 
            border_width=2, 
            border_color="#CF6679", 
            text_color="#CF6679", 
            width=120,
            height=38,
            font=ctk.CTkFont(size=13)
        ).pack(side="left", padx=8)
        
        ctk.CTkButton(
            btn_frame, 
            text="💾 Guardar", 
            command=self.save_credentials, 
            fg_color="#2CC985",
            hover_color="#25A86B",
            width=140,
            height=38,
            font=ctk.CTkFont(size=13, weight="bold")
        ).pack(side="left", padx=8)
    
    def _load_existing_credentials(self):
        """Carga credenciales existentes si las hay"""
        username, password = self.credentials_manager.load_credentials()
        if username:
            self.username_entry.insert(0, username)
        if password:
            self.password_entry.insert(0, password)
    
    def _center_window(self, parent):
        """Centra la ventana respecto al padre"""
        self.update_idletasks()
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        dialog_width = self.winfo_width()
        dialog_height = self.winfo_height()
        
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)
        
        self.geometry(f"+{x}+{y}")
    
    def save_credentials(self):
        """Guarda las credenciales"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showwarning(
                "Datos Incompletos", 
                "Por favor completa todos los campos.",
                parent=self
            )
            return
        
        # Guardar
        success = self.credentials_manager.save_credentials(username, password)
        
        if success:
            self.result = True
            messagebox.showinfo(
                "Éxito",
                "Credenciales guardadas correctamente.",
                parent=self
            )
            self.destroy()
        else:
            messagebox.showerror(
                "Error",
                "No se pudieron guardar las credenciales.",
                parent=self
            )
    
    def cancel(self):
        """Cancela y cierra el diálogo"""
        self.result = False
        self.destroy()