def convertir_a_braille(texto):
    """Paradigma: Funcional. Convierte cada letra a Braille."""
    braille_dict = {
        "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
        "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
        "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
        "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
        "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
        "z": "⠵", " ": " ", "\n": "\n"
    }
    return ''.join([braille_dict.get(letra.lower(), '?') for letra in texto])
