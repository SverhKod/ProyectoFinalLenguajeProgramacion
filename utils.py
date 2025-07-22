# utils.py
def validar_archivo(nombre_archivo):
    """
    Paradigma usado: Estructurado.
    Valida el formato y tamaño del archivo subido por el usuario.
    """
    if not nombre_archivo.endswith('.txt'):
        raise ValueError("Solo se aceptan archivos .txt")
    # Más validaciones aquí...
