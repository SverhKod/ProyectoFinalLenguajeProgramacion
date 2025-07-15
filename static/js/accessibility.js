// Enfoca el primer campo de formulario al cargar
window.addEventListener('DOMContentLoaded', function() {
    const first = document.querySelector('input, textarea, select, button');
    if (first) first.focus();
});

// Navegación completa con Tab y flechas
document.addEventListener('keydown', function(e) {
    if (e.key === 'F1') { // Ayuda contextual
        e.preventDefault();
        document.getElementById('helpBtn').click();
    }
    if (e.key === 'F2') { // Leer resultado
        e.preventDefault();
        document.getElementById('ttsBtn').click();
    }
});