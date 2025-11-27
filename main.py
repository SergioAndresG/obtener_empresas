from gui.main_window import App
from config import settings
from utils.credentials import CredentialsManager

def run_app():
    app = App()
    app.mainloop()
    # Configurar credentials manager ANTES de crear la app
    credentials_manager = CredentialsManager()
    settings.set_credentials_manager(credentials_manager)

if __name__ == "__main__":
    run_app()