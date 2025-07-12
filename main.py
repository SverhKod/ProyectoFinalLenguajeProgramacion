"""
SISTEMA DE TRADUCCIÓN TEXTO-BRAILLE MULTIPARADIGMA
===================================================

Este proyecto implementa un traductor bidireccional entre texto y Braille,
aplicando conceptos de programación multiparadigma:
- Programación Orientada a Objetos: Clases para el traductor y la interfaz
- Programación Funcional: Funciones puras para transformaciones
- Programación Estructurada: Control de flujo y manejo de excepciones

"""

from ui.gui import BrailleGUI

def main():
    app = BrailleGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
