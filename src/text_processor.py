# src/text_processor.py

def clean_text(text):
    return text.strip()

def validate_text(text):
    # Solo acepta letras y espacios, puedes mejorar la validación
    return all(c.isalpha() or c.isspace() for c in text)
