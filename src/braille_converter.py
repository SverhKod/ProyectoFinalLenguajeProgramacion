# ================================
# Clase BrailleConverter - OOP
# Lógica para convertir texto <-> Braille
# ================================

BRAILLE_DICT = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵",
    " ": " ",
    ".": "⠲", ",": "⠂", ";": "⠆", ":": "⠒", "-": "⠤", "?": "⠦", "!": "⠖"
}
REVERSE_BRAILLE_DICT = {v: k for k, v in BRAILLE_DICT.items()}

class BrailleConverter:
    """Clase OOP para conversión entre texto y Braille Unicode."""
    def text_to_braille(self, text):
        """
        Convierte texto plano a Braille unicode.
        Caracteres desconocidos se marcan con '?'.
        """
        return ''.join([BRAILLE_DICT.get(char.lower(), '?') for char in text])

    def braille_to_text(self, braille):
        """
        Convierte Braille unicode a texto plano.
        """
        return ''.join([REVERSE_BRAILLE_DICT.get(char, '?') for char in braille])
