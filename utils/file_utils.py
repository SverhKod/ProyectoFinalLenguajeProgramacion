# Paradigma: Estructurado
def guardar_archivo(texto, ruta):
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)
        return True
    except Exception as e:
        print(f"Error guardando archivo: {e}")
        return False
