"""
SISTEMA DE TRADUCCIÓN TEXTO-BRAILLE MULTIPARADIGMA
===================================================

Este proyecto implementa un traductor bidireccional entre texto y Braille,
aplicando conceptos de programación multiparadigma:
- Programación Orientada a Objetos: Clases para el traductor y la interfaz
- Programación Funcional: Funciones puras para transformaciones
- Programación Estructurada: Control de flujo y manejo de excepciones

"""
# app.py - Sistema de Traducción Texto-Braille Multiparadigma
from flask import Flask, render_template, request, jsonify
from functools import reduce
import re
import json

# ==============================================================================
# PROGRAMACIÓN FUNCIONAL - Funciones puras para transformaciones
# ==============================================================================

# Diccionario de mapeo texto a Braille
TEXTO_A_BRAILLE = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
    ' ': '⠀', '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖',
    ':': '⠒', ';': '⠆', '-': '⠤', '(': '⠶', ')': '⠶',
    'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠬', 'ú': '⠾',
    'ñ': '⠻', 'ü': '⠳'
}

# Diccionario inverso para Braille a texto
BRAILLE_A_TEXTO = {v: k for k, v in TEXTO_A_BRAILLE.items()}

def normalizar_texto(texto: str) -> str:
    """Función pura: normaliza el texto de entrada"""
    return texto.lower().strip()

def es_caracter_valido(caracter: str) -> bool:
    """Función pura: verifica si un caracter es válido para traducción"""
    return caracter in TEXTO_A_BRAILLE

def traducir_caracter_a_braille(caracter: str) -> str:
    """Función pura: traduce un caracter individual a Braille"""
    return TEXTO_A_BRAILLE.get(caracter, '⠦')  # ⠦ para caracteres no reconocidos

def traducir_caracter_a_texto(braille: str) -> str:
    """Función pura: traduce un caracter Braille a texto"""
    return BRAILLE_A_TEXTO.get(braille, '?')

def aplicar_transformacion(texto: str, func_transformacion) -> str:
    """Función de orden superior: aplica una transformación a cada caracter"""
    return ''.join(map(func_transformacion, texto))

def contar_caracteres(texto: str) -> dict:
    """Función pura: cuenta caracteres usando reduce"""
    return reduce(
        lambda acc, char: {**acc, char: acc.get(char, 0) + 1},
        texto,
        {}
    )

# ==============================================================================
# PROGRAMACIÓN ORIENTADA A OBJETOS - Clases para el traductor
# ==============================================================================

class TraductorBraille:
    """Clase principal del traductor con métodos especializados"""
    
    def __init__(self):
        self.historial = []
        self.estadisticas = {
            'traducciones_realizadas': 0,
            'caracteres_procesados': 0,
            'errores': 0
        }
    
    def texto_a_braille(self, texto: str) -> dict:
        """Traduce texto a Braille con manejo de errores"""
        try:
            texto_normalizado = normalizar_texto(texto)
            resultado = aplicar_transformacion(texto_normalizado, traducir_caracter_a_braille)
            
            # Actualizar estadísticas
            self.estadisticas['traducciones_realizadas'] += 1
            self.estadisticas['caracteres_procesados'] += len(texto_normalizado)
            
            # Guardar en historial
            self.historial.append({
                'tipo': 'texto_a_braille',
                'entrada': texto,
                'salida': resultado,
                'timestamp': self._obtener_timestamp()
            })
            
            return {
                'exito': True,
                'resultado': resultado,
                'caracteres_procesados': len(texto_normalizado),
                'caracteres_validos': sum(1 for c in texto_normalizado if es_caracter_valido(c))
            }
            
        except Exception as e:
            self.estadisticas['errores'] += 1
            return {
                'exito': False,
                'error': str(e),
                'resultado': ''
            }
    
    def braille_a_texto(self, braille: str) -> dict:
        """Traduce Braille a texto con manejo de errores"""
        try:
            resultado = aplicar_transformacion(braille, traducir_caracter_a_texto)
            
            # Actualizar estadísticas
            self.estadisticas['traducciones_realizadas'] += 1
            self.estadisticas['caracteres_procesados'] += len(braille)
            
            # Guardar en historial
            self.historial.append({
                'tipo': 'braille_a_texto',
                'entrada': braille,
                'salida': resultado,
                'timestamp': self._obtener_timestamp()
            })
            
            return {
                'exito': True,
                'resultado': resultado,
                'caracteres_procesados': len(braille)
            }
            
        except Exception as e:
            self.estadisticas['errores'] += 1
            return {
                'exito': False,
                'error': str(e),
                'resultado': ''
            }
    
    def obtener_estadisticas(self) -> dict:
        """Retorna las estadísticas del traductor"""
        return self.estadisticas.copy()
    
    def obtener_historial(self, limite: int = 10) -> list:
        """Retorna el historial de traducciones"""
        return self.historial[-limite:] if limite else self.historial
    
    def limpiar_historial(self):
        """Limpia el historial de traducciones"""
        self.historial.clear()
    
    def _obtener_timestamp(self) -> str:
        """Método privado para obtener timestamp actual"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class AnalizadorTexto:
    """Clase para análisis avanzado de texto"""
    
    @staticmethod
    def analizar_texto(texto: str) -> dict:
        """Analiza las características del texto"""
        texto_limpio = normalizar_texto(texto)
        
        return {
            'longitud_total': len(texto),
            'longitud_sin_espacios': len(texto.replace(' ', '')),
            'palabras': len(texto.split()),
            'caracteres_unicos': len(set(texto_limpio)),
            'frecuencia_caracteres': contar_caracteres(texto_limpio),
            'caracteres_especiales': sum(1 for c in texto_limpio if not c.isalnum() and c != ' '),
            'es_solo_numeros': texto_limpio.replace(' ', '').isdigit(),
            'contiene_acentos': any(c in 'áéíóúñü' for c in texto_limpio)
        }

# ==============================================================================
# PROGRAMACIÓN ESTRUCTURADA - Control de flujo y manejo de excepciones
# ==============================================================================

# Instancia global del traductor
traductor = TraductorBraille()
analizador = AnalizadorTexto()

# Configuración de Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'braille_translator_2024'

@app.route('/')
def index():
    """Ruta principal - renderiza la interfaz"""
    return render_template('index.html')

@app.route('/traducir', methods=['POST'])
def traducir():
    """Endpoint para realizar traducciones"""
    try:
        datos = request.get_json()
        
        if not datos or 'texto' not in datos or 'tipo' not in datos:
            return jsonify({
                'exito': False,
                'error': 'Datos incompletos en la solicitud'
            }), 400
        
        texto = datos['texto']
        tipo = datos['tipo']
        
        # Validación de entrada
        if not texto or not texto.strip():
            return jsonify({
                'exito': False,
                'error': 'El texto no puede estar vacío'
            }), 400
        
        # Procesamiento según el tipo
        if tipo == 'texto_a_braille':
            resultado = traductor.texto_a_braille(texto)
            if resultado['exito']:
                resultado['analisis'] = analizador.analizar_texto(texto)
        
        elif tipo == 'braille_a_texto':
            resultado = traductor.braille_a_texto(texto)
        
        else:
            return jsonify({
                'exito': False,
                'error': 'Tipo de traducción no válido'
            }), 400
        
        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({
            'exito': False,
            'error': f'Error interno del servidor: {str(e)}'
        }), 500

@app.route('/estadisticas')
def estadisticas():
    """Endpoint para obtener estadísticas"""
    try:
        stats = traductor.obtener_estadisticas()
        return jsonify({
            'exito': True,
            'estadisticas': stats
        })
    except Exception as e:
        return jsonify({
            'exito': False,
            'error': str(e)
        }), 500

@app.route('/historial')
def historial():
    """Endpoint para obtener historial"""
    try:
        limite = request.args.get('limite', 10, type=int)
        hist = traductor.obtener_historial(limite)
        return jsonify({
            'exito': True,
            'historial': hist
        })
    except Exception as e:
        return jsonify({
            'exito': False,
            'error': str(e)
        }), 500

@app.route('/limpiar-historial', methods=['POST'])
def limpiar_historial():
    """Endpoint para limpiar historial"""
    try:
        traductor.limpiar_historial()
        return jsonify({
            'exito': True,
            'mensaje': 'Historial limpiado exitosamente'
        })
    except Exception as e:
        return jsonify({
            'exito': False,
            'error': str(e)
        }), 500

@app.route('/analizar', methods=['POST'])
def analizar():
    """Endpoint para análisis de texto"""
    try:
        datos = request.get_json()
        
        if not datos or 'texto' not in datos:
            return jsonify({
                'exito': False,
                'error': 'Texto requerido para análisis'
            }), 400
        
        texto = datos['texto']
        
        if not texto.strip():
            return jsonify({
                'exito': False,
                'error': 'El texto no puede estar vacío'
            }), 400
        
        analisis = analizador.analizar_texto(texto)
        
        return jsonify({
            'exito': True,
            'analisis': analisis
        })
    
    except Exception as e:
        return jsonify({
            'exito': False,
            'error': str(e)
        }), 500

# Manejo de errores globales
@app.errorhandler(404)
def no_encontrado(error):
    return jsonify({
        'exito': False,
        'error': 'Endpoint no encontrado'
    }), 404

@app.errorhandler(500)
def error_interno(error):
    return jsonify({
        'exito': False,
        'error': 'Error interno del servidor'
    }), 500

# ==============================================================================
# FUNCIÓN PRINCIPAL - Punto de entrada estructurado
# ==============================================================================

def main():
    """Función principal con manejo estructurado"""
    try:
        print("🔄 Iniciando Sistema de Traducción Texto-Braille Multiparadigma")
        print("📚 Paradigmas implementados:")
        print("   • Programación Orientada a Objetos")
        print("   • Programación Funcional")
        print("   • Programación Estructurada")
        print("🌐 Servidor disponible en: http://localhost:5000")
        print("⚡ Presiona Ctrl+C para detener el servidor")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
    finally:
        print("📊 Estadísticas finales:")
        stats = traductor.obtener_estadisticas()
        for key, value in stats.items():
            print(f"   • {key}: {value}")

if __name__ == '__main__':
    main()