window.onload = function() {
    if (!localStorage.getItem('tourDone')) {
        const tour = new Shepherd.Tour({
            defaultStepOptions: { scrollTo: true, cancelIcon: {enabled: true} }
        });
        tour.addStep({
            title: 'Bienvenido',
            text: '¡Este es el conversor Braille inclusivo!',
            attachTo: {element: '.converter-card', on: 'bottom'},
            buttons: [{ text: 'Siguiente', action: tour.next }]
        });
        tour.addStep({
            title: 'Entrada',
            text: 'Escribe aquí tu texto o Braille.',
            attachTo: {element: '#text', on: 'right'},
            buttons: [{ text: 'Siguiente', action: tour.next }]
        });
        tour.addStep({
            title: 'Botón convertir',
            text: 'Haz clic para convertir, o usa Ctrl+Enter.',
            attachTo: {element: '#convertBtn', on: 'right'},
            buttons: [{ text: 'Finalizar', action: tour.complete }]
        });
        tour.on('complete', () => localStorage.setItem('tourDone', 'yes'));
        tour.start();
    }
};
