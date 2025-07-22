from models.database_manager import DatabaseManager
from datetime import datetime

class ProgresoService:
    @staticmethod
    def guardar_progreso(usuario_id, ejercicio, puntaje):
        query = """
        INSERT INTO progreso (usuario_id, ejercicio, puntaje, fecha)
        VALUES (%s, %s, %s, %s)
        """
        fecha_actual = datetime.now()
        result = DatabaseManager.ejecutar_consulta(
            query, (usuario_id, ejercicio, puntaje, fecha_actual)
        )
        return result is not None

    @staticmethod
    def obtener_progreso(usuario_id, limite=10):
        query = """
        SELECT * FROM progreso
        WHERE usuario_id = %s
        ORDER BY fecha DESC
        LIMIT %s
        """
        return DatabaseManager.ejecutar_consulta(query, (usuario_id, limite), fetch=True) or []
