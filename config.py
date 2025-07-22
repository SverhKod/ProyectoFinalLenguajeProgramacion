import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_insegura')
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
    # Configuración BD
    DB_CONFIG = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', ''),
        'charset': 'utf8mb4'
    }
