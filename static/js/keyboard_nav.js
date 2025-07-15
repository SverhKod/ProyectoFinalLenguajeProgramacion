// Atajos: Ctrl+Enter para convertir
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
        document.getElementById('convertBtn').click();
    }
});
