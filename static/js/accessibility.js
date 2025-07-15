// Enfoca el primer campo de formulario al cargar
window.addEventListener('DOMContentLoaded', function() {
    const first = document.querySelector('input, textarea, select, button');
    if (first) first.focus();
});

// Navegación rápida con atajos de teclado
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'h') {
        window.location.href = '/history';
    }
    if (e.ctrlKey && e.key === 'l') {
        const text = document.getElementById('text');
        if (text) text.value = '';
    }
});
