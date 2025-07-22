class User:
    """Paradigma OO. Representa un usuario y su historial."""
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.historial = []

    def registrar_conversion(self, texto_original, texto_braille):
        self.historial.append((texto_original, texto_braille))
