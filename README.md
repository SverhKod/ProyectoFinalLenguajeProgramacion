# BrailleX

**BrailleX** es una aplicación web inclusiva que permite convertir texto a Braille y viceversa, diseñada para ser accesible para personas con discapacidad visual. El sistema incluye historial de conversiones, guía de accesibilidad y una interfaz optimizada para lectores de pantalla y alto contraste.

---

## Características principales

- **Conversión bidireccional:** Texto a Braille y Braille a texto.
- **Interfaz accesible:** Compatible con lectores de pantalla, navegación por teclado y alto contraste.
- **Historial inteligente:** Consulta y busca conversiones anteriores.
- **Guía de accesibilidad:** Consejos y ayuda para usuarios con discapacidad visual.
- **Tour interactivo:** Guía inicial para nuevos usuarios.

---

## Instalación y ejecución

### Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/SverhKod/ProyectoFinalLenguajeProgramacion.git
   cd ProyectoFinalLenguajeProgramacion
   ```

2. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```sh
   python app.py
   ```

4. **Accede desde tu navegador:**
   ```
   http://localhost:5000
   ```

---

## Uso de la aplicación

1. **Conversión:**  
   Ingresa texto o Braille en el campo principal y selecciona el modo de conversión. Haz clic en "Convertir" o usa `Ctrl+Enter`.

2. **Historial:**  
   Accede a la pestaña "Historial" para ver y buscar conversiones anteriores.

3. **Ayuda:**  
   Consulta la sección "Ayuda" para recomendaciones de accesibilidad y atajos de teclado.

4. **Tour interactivo:**  
   Al primer ingreso, sigue el tour guiado para conocer las funciones principales.

---

## Accesibilidad

- **Navegación por teclado:** Todos los elementos son accesibles mediante `Tab` y atajos.
- **Compatibilidad con lectores de pantalla:** Etiquetas ARIA y roles semánticos incluidos.
- **Alto contraste:** Interfaz optimizada para usuarios con baja visión.
- **Soporte para dispositivos móviles:** Diseño responsive.

---

## Estructura del proyecto

```
ProyectoF1n4l_LP/
│
├── app.py                  # Backend principal 
├── requirements.txt        # Dependencias Python
├── src/
│   └── braille_converter.py
├── templates/
│   ├── base_accessible.html
│   ├── converter_voice.html
│   ├── history_smart.html
│   └── accessibility_help.html
├── static/
│   ├── css/
│   │   └── accessible.css
│   └── js/
│       ├── tour.js
│       └── history.js
└── README.md
```

---

## Contribución

¿Quieres mejorar el proyecto?  
1. Haz un fork  
2. Crea una rama (`git checkout -b feature/nueva-funcion`)  
3. Haz tus cambios y realiza un commit  
4. Envía un Pull Request

---

## Licencia

Proyecto educativo y de acceso abierto.  
© 2025 BrailleX – Todos los derechos reservados.
