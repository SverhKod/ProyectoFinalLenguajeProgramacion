// Simulación de historial (puedes conectar esto con backend después)
let history = [];

function renderHistory(filtered = history) {
    const tbody = document.getElementById('historyBody');
    tbody.innerHTML = '';
    filtered.forEach(h => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${h.input}</td><td>${h.output}</td><td>${h.mode}</td><td>${h.date}</td>`;
        tbody.appendChild(tr);
    });
}

// Buscar en historial
document.getElementById('historySearch').oninput = function() {
    const query = this.value.toLowerCase();
    const filtered = history.filter(h =>
        h.input.toLowerCase().includes(query) ||
        h.output.toLowerCase().includes(query) ||
        h.mode.toLowerCase().includes(query)
    );
    renderHistory(filtered);
};

// Simula cargar historial al iniciar
window.onload = function() {
    // Aquí puedes cargar el historial real
    history = [
        {input:"hola", output:"⠓⠕⠇⠁", mode:"Texto → Braille", date:"2025-07-15"},
        {input:"⠃⠥⠇⠁", output:"bula", mode:"Braille → Texto", date:"2025-07-14"},
    ];
    renderHistory();
};
