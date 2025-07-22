# models.py
class Usuario:
    """
    Paradigma usado: Orientado a objetos.
    Modela a un usuario y su progreso en la plataforma.
    """
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.progreso = []

    def registrar_progreso(self, avance):
        """
        Paradigma usado: Orientado a objetos.
        Registra el avance del usuario.
        """
        self.progreso.append(avance)
