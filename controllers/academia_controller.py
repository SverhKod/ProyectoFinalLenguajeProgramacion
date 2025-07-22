import random
import unicodedata
from flask import Blueprint, render_template, request, session
from models.braille_converter import BrailleConverter
from models.progreso_service import ProgresoService

academia_bp = Blueprint('academia', __name__)

PALABRAS = [
    "casa", "hola", "gato", "familia", "sol",
    "gracias", "programa", "python", "flask", "mundo"
]

@academia_bp.route('/academia', methods=['GET', 'POST'])
def academia():
    palabra = request.args.get('palabra')
    if not palabra or palabra == "aleatorio":
        palabra = random.choice(PALABRAS)
    ejercicio = f'Traduce la palabra: {palabra}'
    resultado = None
    puntaje = None
    if request.method == 'POST':
        respuesta = request.form.get('respuesta', '')
        correcta = BrailleConverter.texto_a_braille(palabra)

        # 🔴 Aquí normalizamos y limpiamos ambos lados:
        respuesta_normalizada = unicodedata.normalize('NFC', respuesta.strip())
        correcta_normalizada = unicodedata.normalize('NFC', correcta.strip())

        if respuesta_normalizada == correcta_normalizada:
            resultado = "¡Correcto!"
            puntaje = 1
        else:
            resultado = f"Incorrecto. La respuesta correcta es: {correcta}"
            puntaje = 0
        if 'usuario_id' in session:
            ProgresoService.guardar_progreso(session['usuario_id'], ejercicio, puntaje)
    return render_template('academia.html', ejercicio=ejercicio, palabra=palabra, resultado=resultado)

