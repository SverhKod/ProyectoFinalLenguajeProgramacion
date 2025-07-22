import mysql.connector
import logging
from config import Config

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manejo centralizado de la base de datos"""
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(**Config.DB_CONFIG)
            return connection
        except mysql.connector.Error as e:
            logger.error(f"Error conectando a la base de datos: {e}")
            return None

    @staticmethod
    def ejecutar_consulta(query, params=None, fetch=False):
        connection = None
        cursor = None
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return None
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            if fetch:
                return cursor.fetchall()
            else:
                connection.commit()
                return cursor.rowcount
        except mysql.connector.Error as e:
            logger.error(f"Error ejecutando consulta: {e}")
            if connection:
                connection.rollback()
            return None
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
