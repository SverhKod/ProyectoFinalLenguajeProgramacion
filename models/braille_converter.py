class BrailleConverter:
    # Diccionario Braille extendido con signos comunes y acentos españoles
    BRAILLE_DICT = {
        # Letras minúsculas
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
        'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
        'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
        's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
        'y': '⠽', 'z': '⠵',
        # Números
        '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
        '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
        # Espacio
        ' ': ' ',
        # Signos de puntuación y matemáticos extendidos
        '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '?': '⠦', '!': '⠖',
        '-': '⠤', '—': '⠠⠤', '–': '⠤', '_': '⠠⠤', '(': '⠶', ')': '⠶',
        '"': '⠶', "'": '⠄', '«': '⠦', '»': '⠴', '[': '⠪', ']': '⠻', '{': '⠸⠣', '}': '⠸⠜',
        '/': '⠌', '\\': '⠳', '|': '⠸⠌', '@': '⠈⠁', '#': '⠼', '&': '⠯', '%': '⠨⠴',
        '=': '⠶', '+': '⠖', '*': '⠔', '<': '⠪', '>': '⠕', '$': '⠈⠎', '^': '⠘', '`': '⠈',
        # Acentos y letras especiales del español
        'á': '⠷', 'é': '⠿', 'í': '⠌', 'ó': '⠬', 'ú': '⠾', 'ü': '⠳', 'ñ': '⠻',
        'Á': '⠠⠷', 'É': '⠠⠿', 'Í': '⠠⠌', 'Ó': '⠠⠬', 'Ú': '⠠⠾', 'Ü': '⠠⠳', 'Ñ': '⠠⠻',
        # Otros signos
        '°': '⠚⠚', '¡': '⠖', '¿': '⠦'
    }

    NUMBER_PREFIX = '⠼'
    CAPITAL_PREFIX = '⠠'

    @classmethod
    def texto_a_braille(cls, texto):
        if not texto:
            return ""
        resultado, i, en_numero = [], 0, False
        while i < len(texto):
            char = texto[i]
            if char.isdigit():
                if not en_numero:
                    resultado.append(cls.NUMBER_PREFIX)
                    en_numero = True
                resultado.append(cls.BRAILLE_DICT.get(char, char))
            elif char.isupper():
                resultado.append(cls.CAPITAL_PREFIX)
                resultado.append(cls.BRAILLE_DICT.get(char.lower(), char.lower()))
                en_numero = False
            else:
                if char == ' ': en_numero = False
                resultado.append(cls.BRAILLE_DICT.get(char, cls.BRAILLE_DICT.get(char.lower(), '?')))
                en_numero = False
            i += 1
        return ''.join(resultado)

    @classmethod
    def procesar_archivo(cls, contenido_archivo):
        try:
            lineas = contenido_archivo.split('\n')
            return '\n'.join([cls.texto_a_braille(linea) for linea in lineas])
        except Exception as e:
            raise Exception(f"Error al procesar el archivo: {str(e)}")
