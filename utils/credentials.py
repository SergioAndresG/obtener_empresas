import json
import base64
from pathlib import Path
import os


class CredentialsManager:
    """Maneja credenciales de forma local"""
    
    def __init__(self):
        # Directorio en home del usuario
        self.config_dir = Path.home() / ".ExtractorEmpresas"
        self.credentials_file = self.config_dir / "credentials.json"
        self._ensure_config_dir()
    
    def _ensure_config_dir(self):
        """Crea el directorio de configuración si no existe"""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            print(f"Directorio de configuración: {self.config_dir}")
            
            # En Windows, intentar ocultar la carpeta
            if os.name == 'nt':
                try:
                    import ctypes
                    FILE_ATTRIBUTE_HIDDEN = 0x02
                    ctypes.windll.kernel32.SetFileAttributesW(
                        str(self.config_dir), 
                        FILE_ATTRIBUTE_HIDDEN
                    )
                except:
                    pass  # No crítico si falla
                    
        except Exception as e:
            print(f"Error creando directorio: {e}")
    
    def save_credentials(self, username, password):
        """
        Guarda credenciales con ofuscación básica
        
        Args:
            username: Usuario
            password: Contraseña
            
        Returns:
            bool: True si se guardó exitosamente
        """
        try:
            # Ofuscación básica con base64
            encoded_password = base64.b64encode(password.encode()).decode()
            
            data = {
                "username": username,
                "password": encoded_password
            }
            
            with open(self.credentials_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f" Credenciales guardadas")
            return True
            
        except Exception as e:
            print(f" Error guardando credenciales: {e}")
            return False
    
    def load_credentials(self):
        """
        Carga credenciales
        
        Returns:
            tuple: (username, password) o (None, None) si no existen
        """
        if not self.credentials_file.exists():
            print("ℹNo hay credenciales guardadas")
            return None, None
        
        try:
            with open(self.credentials_file, 'r') as f:
                data = json.load(f)
            
            username = data.get("username")
            encoded_password = data.get("password")
            
            if not username or not encoded_password:
                return None, None
            
            # Decodificar contraseña
            password = base64.b64decode(encoded_password.encode()).decode()
            
            print(f"Credenciales cargadas para: {username}")
            return username, password
            
        except Exception as e:
            print(f"Error cargando credenciales: {e}")
            return None, None
    
    def credentials_exist(self):
        """Verifica si existen credenciales guardadas"""
        exists = self.credentials_file.exists()
        print(f"¿Credenciales existen? {exists}")
        return exists
    
    def delete_credentials(self):
        """Elimina las credenciales guardadas"""
        try:
            if self.credentials_file.exists():
                self.credentials_file.unlink()
                print("Credenciales eliminadas")
            return True
        except Exception as e:
            print(f"Error eliminando credenciales: {e}")
            return False
    
    def validate_credentials(self):
        """Valida que las credenciales sean válidas"""
        username, password = self.load_credentials()
        is_valid = (username is not None and 
                   password is not None and 
                   len(username) > 0 and 
                   len(password) > 0)
        print(f"✔️ Credenciales válidas: {is_valid}")
        return is_valid