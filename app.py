from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import os
import logging
from werkzeug.utils import secure_filename
from config import Config

from models.database_manager import DatabaseManager

from models.braille_converter import BrailleConverter
from models.usuario_service import UsuarioService
from models.historial_service import HistorialService


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = Config.ALLOWED_EXTENSIONS

# Crea carpeta uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    try:
        estadisticas = HistorialService.obtener_estadisticas()
        return render_template('index.html', estadisticas=estadisticas)
    except Exception as e:
        logger.error(f"Error en página de inicio: {e}")
        return render_template('index.html', estadisticas=[])

# (Las demás rutas igual que en tu código, solo importa los servicios desde models)

# Ejemplo para una ruta:
@app.route('/convertir-archivo', methods=['GET', 'POST'])
def convertir_archivo():
    if request.method == 'POST':
        try:
            if 'archivo' not in request.files:
                flash('No se seleccionó archivo', 'error')
                return redirect(request.url)
            archivo = request.files['archivo']
            if archivo.filename == '':
                flash('No se seleccionó archivo', 'error')
                return redirect(request.url)
            if archivo and allowed_file(archivo.filename):
                contenido = archivo.read().decode('utf-8')
                contenido_braille = BrailleConverter.procesar_archivo(contenido)
                if 'usuario_id' in session:
                    HistorialService.guardar_conversion(
                        session['usuario_id'],
                        f"Archivo: {archivo.filename}",
                        contenido_braille[:500] + "..." if len(contenido_braille) > 500 else contenido_braille
                    )
                return render_template('resultado.html', {
                    'nombre_archivo': archivo.filename,
                    'contenido_original': contenido,
                    'contenido_braille': contenido_braille,
                    'estadisticas': {
                        'caracteres_originales': len(contenido),
                        'caracteres_braille': len(contenido_braille),
                        'lineas': contenido.count('\n') + 1
                    }
                })
            else:
                flash('Tipo de archivo no permitido', 'error')
        except Exception as e:
            logger.error(f"Error procesando archivo: {e}")
            flash('Error procesando archivo', 'error')
    return render_template('convertir_archivo.html')

# (Resto de tus rutas igual...)

if __name__ == '__main__':
    try:
        connection = DatabaseManager.get_connection()
        if connection:
            logger.info("Conexión a la base de datos exitosa")
            connection.close()
        else:
            logger.error("No se pudo conectar a la base de datos")
    except Exception as e:
        logger.error(f"Error verificando base de datos: {e}")

    app.run(debug=True, host='0.0.0.0', port=5000)
