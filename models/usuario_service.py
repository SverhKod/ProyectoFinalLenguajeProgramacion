from models.database_manager import DatabaseManager

class UsuarioService:
    """
    Servicio para manejo de usuarios.
    Paradigma: Orientado a Objetos y Servicios.
    """

    @staticmethod
    def crear_usuario(nombre, email):
        """Crear un nuevo usuario."""
        query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        result = DatabaseManager.ejecutar_consulta(query, (nombre, email))
        return result is not None

    @staticmethod
    def obtener_usuario_por_email(email):
        """Obtener un usuario por su email."""
        query = "SELECT * FROM usuarios WHERE email = %s"
        usuarios = DatabaseManager.ejecutar_consulta(query, (email,), fetch=True)
        return usuarios[0] if usuarios else None

    @staticmethod
    def obtener_todos_usuarios():
        """Obtener todos los usuarios."""
        query = "SELECT * FROM usuarios ORDER BY nombre"
        return DatabaseManager.ejecutar_consulta(query, fetch=True) or []
