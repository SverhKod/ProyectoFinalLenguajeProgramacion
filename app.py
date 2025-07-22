# app.py – Aplicación Principal Flask
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import os
import logging
from werkzeug.utils import secure_filename
from config import Config
from PyPDF2 import PdfReader
import docx

# Importar servicios/modelos propios
from models.database_manager import DatabaseManager
from models.braille_converter import BrailleConverter
from models.progreso_service import ProgresoService
from models.historial_service import HistorialService
from services.usuario_service import UsuarioService

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear aplicación Flask y configuración inicial
app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = Config.ALLOWED_EXTENSIONS

# ---- Paradigma OO: Clase para lecciones ----
class LeccionBraille:
    def __init__(self, titulo, contenido, ejercicios):
        self.titulo = titulo
        self.contenido = contenido
        self.ejercicios = ejercicios

# ---- Paradigma funcional: función para corregir respuestas ----
def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario.strip().lower() == respuesta_correcta.strip().lower()

# Crea la carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Verifica si el archivo tiene una extensión permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ----------------- RUTAS PRINCIPALES -----------------

@app.route('/')
def index():
    """Página de inicio con estadísticas generales."""
    try:
        estadisticas = HistorialService.obtener_estadisticas()
        return render_template('index.html', estadisticas=estadisticas)
    except Exception as e:
        logger.error(f"Error en página de inicio: {e}")
        return render_template('index.html', estadisticas=[])


    """Ruta para inicio de sesión sencillo (solo email)."""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        usuario = UsuarioService.obtener_usuario_por_email(email)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nombre'] = usuario['nombre']
            flash(f'¡Bienvenido, {usuario["nombre"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario no encontrado.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Cerrar sesión del usuario."""
    session.clear()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('index'))


@app.route('/convertir-archivo', methods=['GET', 'POST'])
def convertir_archivo():
    """Conversión de archivos de texto a Braille."""
    if request.method == 'POST':
        try:
            if 'archivo' not in request.files:
                flash('No se seleccionó archivo', 'danger')
                return redirect(request.url)
            archivo = request.files['archivo']
            if archivo.filename == '':
                flash('No se seleccionó archivo', 'danger')
                return redirect(request.url)
            if archivo and allowed_file(archivo.filename):
                filename = archivo.filename.lower()
                ext = filename.rsplit('.', 1)[-1]
                contenido = ''
                if ext == 'txt':
                    contenido = archivo.read().decode('utf-8')
                elif ext == 'pdf':
                    reader = PdfReader(archivo)
                    for page in reader.pages:
                        contenido += page.extract_text() or ''
                elif ext == 'docx':
                    doc = docx.Document(archivo)
                    contenido = '\n'.join([p.text for p in doc.paragraphs])
                else:
                    flash('Tipo de archivo no permitido', 'danger')
                    return redirect(request.url)

                if not contenido.strip():
                    flash('El archivo está vacío o no se pudo extraer el texto.', 'danger')
                    return redirect(request.url)

                contenido_braille = BrailleConverter.procesar_archivo(contenido)
                # Guarda conversión en historial si está logueado
                if 'usuario_id' in session:
                    HistorialService.guardar_conversion(
                        session['usuario_id'],
                        f"Archivo: {archivo.filename}",
                        contenido_braille[:500] + "..." if len(contenido_braille) > 500 else contenido_braille
                    )
                return render_template(
    'resultado.html',
    nombre_archivo=archivo.filename,
    contenido_original=contenido,
    contenido_braille=contenido_braille,
    estadisticas={
        'caracteres_originales': len(contenido),
        'caracteres_braille': len(contenido_braille),
        'lineas': contenido.count('\n') + 1
    }
)

            else:
                flash('Tipo de archivo no permitido', 'danger')
        except Exception as e:
            logger.error(f"Error procesando archivo: {e}")
            flash('Error procesando archivo', 'danger')
    return render_template('convertir_archivo.html')


@app.route('/academia', methods=['GET', 'POST'])
def academia():
    """
    Página de academia interactiva: ejercicios de traducción a Braille.
    Aquí el usuario debe traducir la palabra "casa" a Braille.
    """
    ejercicio = 'Traduce la palabra: casa'
    palabra = 'casa'
    resultado = None
    puntaje = None

    if request.method == 'POST':
        respuesta = request.form.get('respuesta', '')
        correcta = BrailleConverter.texto_a_braille(palabra)
        if respuesta.strip() == correcta:
            resultado = "¡Correcto!"
            puntaje = 1
        else:
            resultado = f"Incorrecto. La respuesta correcta es: {correcta}"
            puntaje = 0

        # Guardar progreso en BD si está logueado
        if 'usuario_id' in session:
            ProgresoService.guardar_progreso(session['usuario_id'], ejercicio, puntaje)

    return render_template('academia.html', ejercicio=ejercicio, resultado=resultado)

# ---- Paradigma estructurado: ruta Flask ----
@app.route('/aprende', methods=['GET', 'POST'])
def aprende():
    # Lista de lecciones como objetos OO
    lecciones = [
        LeccionBraille(
            "¿Qué es el Braille?",
            "El Braille es un sistema de lectura y escritura táctil diseñado para personas ciegas.",
            ["¿Quién inventó el Braille?", "¿En qué país se originó?"]
        ),
        LeccionBraille(
            "Cómo se lee el Braille",
            "Cada letra se representa por un patrón de puntos en relieve.",
            ["¿Cuántos puntos tiene una celda Braille?", "¿Cómo se representa la letra 'A'?"]
        )
    ]
    recursos = [
        {"nombre": "Pack de Abecedario ", "url": "https://www.orientacionandujar.es/2024/11/11/pack-abecedario-braille-y-lse-y-juegos-didacticos/"},
        {"nombre": "Braille Bug", "url": "https://braillebug.org"}
    ]
    resultado = None
    # Corrección funcional si el usuario responde al quiz
    if request.method == "POST":
        respuesta = request.form.get("respuesta", "")
        resultado = verificar_respuesta(respuesta, "Louis Braille")
    return render_template("aprende.html", lecciones=lecciones, recursos=recursos, resultado=resultado)


@app.route('/progreso')
def progreso():
    """Página de progreso personal. Solo usuarios logueados pueden verla."""
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión primero', 'warning')
        return redirect(url_for('login'))
    historial = ProgresoService.obtener_progreso(session['usuario_id'], limite=20)
    return render_template('progreso.html', historial=historial)
@app.route('/diccionario')
def diccionario():
    return render_template('diccionario.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    """Ruta para inicio de sesión sencillo (solo email)."""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        usuario = UsuarioService.obtener_usuario_por_email(email)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nombre'] = usuario['nombre']
            flash(f'¡Bienvenido, {usuario["nombre"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario no encontrado.', 'danger')
    return render_template('login.html')


    """Cerrar sesión del usuario."""
    session.clear()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('index'))
    """Ruta para inicio de sesión sencillo (solo email)."""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        usuario = UsuarioService.obtener_usuario_por_email(email)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_nombre'] = usuario['nombre']
            flash(f'¡Bienvenido, {usuario["nombre"]}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario no encontrado.', 'danger')
    return render_template('login.html')


    """Cerrar sesión del usuario."""
    session.clear()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('index'))
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Registro de nuevo usuario."""
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        if not nombre or not email:
            flash('Debes ingresar nombre y correo.', 'danger')
        elif UsuarioService.obtener_usuario_por_email(email):
            flash('Ese correo ya está registrado.', 'danger')
        else:
            UsuarioService.crear_usuario(nombre, email)
            flash('¡Usuario creado! Ahora inicia sesión.', 'success')
            return redirect(url_for('login'))
    return render_template('registro.html')



# ----------------- INICIO DE LA APP -----------------
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
