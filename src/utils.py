# braille/utils.py

import re

BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
    ' ': '⠀', '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖',
    ';': '⠆', ':': '⠒', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜'
}
TEXT_MAP = {v: k for k, v in BRAILLE_MAP.items()}

def validate_text_input(text: str) -> bool:
    """Valida si el texto contiene solo caracteres soportados."""
    supported_chars = set(BRAILLE_MAP.keys())
    return all(char.lower() in supported_chars for char in text)

def normalize_text(text: str) -> str:
    """Normaliza el texto eliminando caracteres no soportados."""
    if not text:
        return ""
    normalized = ''.join(char.lower() if char.lower() in BRAILLE_MAP else ' '
                         for char in text)
    return re.sub(r'\s+', ' ', normalized.strip())

def calculate_conversion_stats(original: str, converted: str) -> dict:
    """Calcula estadísticas simples de conversión."""
    return {
        'original_length': len(original),
        'converted_length': len(converted),
        'character_count': len([c for c in original if c != ' ']),
        'word_count': len(original.split()) if original else 0
    }
