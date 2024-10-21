
    function abrirPopup(event, url, nombre, ancho, alto) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        const left = (screen.width / 2) - (ancho / 2);
        const top = (screen.height / 6) - (alto / 6);
        
        // Abrir la ventana emergente
        const ventanaEmergente = window.open(url, nombre, `width=${ancho},height=${alto},top=${top},left=${left}`);
        
        // Esperar a que la ventana se cargue y luego imprimir
        ventanaEmergente.onload = function() {
            ventanaEmergente.print(); // Iniciar impresión
        };
    }
