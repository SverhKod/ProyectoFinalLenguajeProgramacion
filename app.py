# app.py
# ================================
# Braille Accessibility System
# Backend principal en Flask
# ================================
# Descripción: 
#   - Gestiona rutas de la web inclusiva
#   - Usa la clase BrailleConverter para conversión de texto/Braille
#   - Incluye endpoints para páginas adicionales (historial, ayuda)
# ================================

from flask import Flask, render_template, request, jsonify
from src.braille_converter import BrailleConverter

# Instancia de Flask
app = Flask(__name__)

# Instancia del conversor OOP
converter = BrailleConverter()

# -------------------------------
# Página principal del conversor
# -------------------------------
@app.route('/')
def home():
    """
    Ruta principal.
    Renderiza la página del conversor accesible.
    """
    return render_template('converter_voice.html')

# -------------------------------
# Endpoint para conversión AJAX
# -------------------------------
@app.route('/convert', methods=['POST'])
def convert():
    """
    Endpoint POST para convertir texto <-> Braille.
    Recibe: texto y modo (to_braille o to_text)
    Devuelve: resultado en formato JSON
    """
    text = request.form.get('text', '')
    mode = request.form.get('mode', 'to_braille')
    if mode == 'to_braille':
        result = converter.text_to_braille(text)
    else:
        result = converter.braille_to_text(text)
    return jsonify({'result': result})

# -------------------------------
# Página de historial de conversiones
# -------------------------------
@app.route('/history')
def history():
    """
    Página para mostrar historial de conversiones
    (puedes conectar a BD, archivo o usar JS local)
    """
    return render_template('history_smart.html')

# -------------------------------
# Página de ayuda accesible
# -------------------------------
@app.route('/accessibility-help')
def accessibility_help():
    """
    Página con guía y tips de accesibilidad para el usuario.
    """
    return render_template('accessibility_help.html')

# -------------------------------
# Puedes agregar más rutas aquí para nuevos módulos
# Ejemplo: página de estadísticas, perfil de usuario, etc.
# -------------------------------

# ================================
# Arranque de la app
# ================================
if __name__ == '__main__':
    # debug=True: muestra errores detallados (quítalo en producción)
    app.run(debug=True)
