# 🟦 PROYECTOF1N4L_LP – Conversor y Academia de Braille

## Descripción

Aplicación web en Python + Flask para convertir archivos de texto a Braille, practicar ejercicios, consultar un diccionario visual e interactuar con materiales de aprendizaje. Permite registro, inicio de sesión y seguimiento de progreso.

---

## Instalación y Uso

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/SverhKod/ProyectoFinalLenguajeProgramacion.git
   cd PROYECTOF1N4L_LP

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt

## Funcionalidades

- Conversión de archivos `.txt`, `.pdf` y `.docx` a Braille
- Academia interactiva con ejercicios autocorregidos
- Seguimiento de progreso personal
- Diccionario visual de letras y símbolos Braille
- Registro, login y gestión de usuario
- Recursos y materiales recomendados sobre Braille

## ¿Cómo usar la aplicación?

1. **Regístrate** o inicia sesión desde la barra de navegación.
2. **Convierte** archivos de texto a Braille desde "Conversión".
3. **Practica** en la "Academia" y recibe feedback automático.
4. **Consulta** el diccionario visual siempre que lo necesites.
5. **Revisa tu progreso** y continúa aprendiendo.

## Paradigmas de Programación

Este proyecto utiliza tres paradigmas para mayor robustez y claridad:

- **Estructurado:** Control del flujo con funciones y rutas de Flask.
- **Orientado a objetos:** Clases para usuarios, ejercicios, conversión y progreso.
- **Funcional:** Funciones puras para validaciones, conversiones y correcciones automáticas.

## Seguridad y Privacidad

- Los archivos subidos solo se usan temporalmente.
- Las contraseñas y datos críticos se mantienen seguros en variables de entorno (`.env`).
- Nunca subas tu archivo `.env` al repositorio.
