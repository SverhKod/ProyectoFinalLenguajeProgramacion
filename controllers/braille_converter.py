from flask import render_template, request, send_file, redirect, flash, url_for
from services.braille_service import convertir_a_braille
import os
from werkzeug.utils import secure_filename

# Carpeta donde se guardan archivos subidos y generados (estructurado)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def index():
    """
    Paradigma usado: Estructurado.
    Renderiza la página principal con el formulario de conversión.
    """
    return render_template('index.html')

def convertir():
    """
    Paradigma usado: Estructurado y funcional.
    Procesa la subida del archivo, convierte el texto a braille,
    aplica personalización de fuente y tamaño, y permite descargar el resultado.
    Maneja errores comunes como archivo vacío o faltante.
    """
    # Verifica si el campo archivo está en la petición (estructurado)
    if 'archivo' not in request.files:
        flash("No se envió archivo")
        return redirect(url_for('index'))

    archivo = request.files['archivo']

    # Verifica si se seleccionó un archivo (estructurado)
    if archivo.filename == '':
        flash("No seleccionaste archivo")
        return redirect(url_for('index'))

    # Recupera personalización del formulario
    fuente = request.form['fuente']  # Puede usarse para aplicar formato en la vista
    tamano = request.form['tamano']  # Puede usarse para aplicar formato en la vista

    # Asegura el nombre del archivo (seguridad)
    nombre = secure_filename(archivo.filename)

    # Guarda el archivo subido en la carpeta temporal
    ruta = os.path.join(UPLOAD_FOLDER, nombre)
    archivo.save(ruta)

    # Lee el contenido del archivo de texto (estructurado)
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read()

    # Llama a la función funcional para convertir el texto a braille
    texto_braille = convertir_a_braille(texto)

    # Genera un nuevo archivo con el texto en braille
    salida = os.path.join(UPLOAD_FOLDER, "braille_" + nombre)
    with open(salida, "w", encoding="utf-8") as f:
        f.write(texto_braille)

    # Opcional: aquí podrías borrar archivos antiguos para limpieza (no implementado aún)

    # Envía el archivo resultante como descarga (estructurado)
    return send_file(
        salida,
        as_attachment=True,
        download_name=f"braille_{nombre}"
    )

