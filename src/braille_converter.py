# src/braille_converter.py

BRAILLE_DICT = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵",
    " ": " ",
    # Puedes ampliar el diccionario
}
REVERSE_BRAILLE_DICT = {v: k for k, v in BRAILLE_DICT.items()}

class BrailleConverter:
    def __init__(self):
        pass

    def text_to_braille(self, text):
        return ''.join([BRAILLE_DICT.get(char.lower(), '?') for char in text])

    def braille_to_text(self, braille):
        return ''.join([REVERSE_BRAILLE_DICT.get(char, '?') for char in braille])
