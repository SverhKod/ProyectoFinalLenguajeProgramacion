# app.py
# ===================================
# Github: https://github.com/SverhKod/ProyectoFinalLenguajeProgramacion
# -----------------------------------
# Este backend maneja:
#  - Conversión entre texto y Braille (y viceversa)
#  - Historial real (se guarda en archivo .json)
#  - Páginas accesibles (conversor, historial, ayuda)
# -----------------------------------

from flask import Flask, render_template, request, jsonify
from src.braille_converter import BrailleConverter
import json
from datetime import datetime
import os

app = Flask(__name__)
converter = BrailleConverter()

# Ruta del archivo historial (para persistencia entre reinicios)
HISTORY_FILE = 'history.json'

# ---------- Función auxiliar para manejar historial en archivo ----------
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_history(data):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ---------- Rutas principales ----------
@app.route('/')
def home():
    """
    Página principal: conversor de texto y Braille.
    """
    return render_template('converter_voice.html')

@app.route('/convert', methods=['POST'])
def convert():
    """
    Convierte texto <-> Braille, guarda en historial (persistente).
    """
    text = request.form.get('text', '')
    mode = request.form.get('mode', 'to_braille')
    if mode == 'to_braille':
        result = converter.text_to_braille(text)
        mode_str = "Texto → Braille"
    else:
        result = converter.braille_to_text(text)
        mode_str = "Braille → Texto"
    # Leer historial actual
    history_data = load_history()
    # Guardar nueva conversión
    history_data.append({
        "input": text,
        "output": result,
        "mode": mode_str,
        "date": datetime.now().strftime('%Y-%m-%d %H:%M')
    })
    save_history(history_data)
    return jsonify({'result': result})

@app.route('/history')
def history():
    """
    Página de historial (tabla accesible).
    """
    return render_template('history_smart.html')

@app.route('/history-data')
def history_data_api():
    """
    API: Devuelve el historial actual en JSON.
    """
    return jsonify(load_history())

@app.route('/accessibility-help')
def accessibility_help():
    """
    Página de ayuda y tips de accesibilidad.
    """
    return render_template('accessibility_help.html')

if __name__ == '__main__':
    app.run(debug=True)
