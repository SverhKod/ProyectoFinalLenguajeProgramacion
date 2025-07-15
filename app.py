from flask import Flask, render_template, request, jsonify
from src.braille_converter import BrailleConverter

app = Flask(__name__)
converter = BrailleConverter()

@app.route('/')
def home():
    return render_template('converter_voice.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form.get('text', '')
    mode = request.form.get('mode', 'to_braille')
    if mode == 'to_braille':
        result = converter.text_to_braille(text)
    else:
        result = converter.braille_to_text(text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
