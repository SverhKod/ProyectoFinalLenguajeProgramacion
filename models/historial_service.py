from datetime import datetime
from models.database_manager import DatabaseManager

class HistorialService:
    """
    Servicio para manejo del historial de conversiones.
    Paradigma: Orientado a Objetos y Servicios.
    """

    @staticmethod
    def guardar_conversion(usuario_id, texto_original, texto_braille):
        """Guardar una conversión en el historial."""
        query = """
        INSERT INTO historial (usuario_id, texto_original, texto_braille, fecha)
        VALUES (%s, %s, %s, %s)
        """
        fecha_actual = datetime.now()
        result = DatabaseManager.ejecutar_consulta(
            query,
            (usuario_id, texto_original, texto_braille, fecha_actual)
        )
        return result is not None

    @staticmethod
    def obtener_historial_usuario(usuario_id, limite=10):
        """Obtener el historial de un usuario."""
        query = """
        SELECT * FROM historial
        WHERE usuario_id = %s
        ORDER BY fecha DESC
        LIMIT %s
        """
        return DatabaseManager.ejecutar_consulta(query, (usuario_id, limite), fetch=True) or []

    @staticmethod
    def obtener_estadisticas():
        """Obtener estadísticas generales del historial."""
        query = """
        SELECT
            COUNT(*) as total_conversiones,
            COUNT(DISTINCT usuario_id) as usuarios_activos,
            DATE(fecha) as fecha_conversion
        FROM historial
        GROUP BY DATE(fecha)
        ORDER BY fecha_conversion DESC
        LIMIT 7
        """
        return DatabaseManager.ejecutar_consulta(query, fetch=True) or []
