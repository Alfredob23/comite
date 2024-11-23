document.addEventListener('DOMContentLoaded', function () {
    const facturaInput = document.getElementById('factura');
    const cedulaInput = document.getElementById('cedula');
    const nombreCompletoInput = document.getElementById('nombre_completo');
    const direccionInput = document.getElementById('direccion');
    const valorIngresoInput = document.getElementById('valorIngreso');

    facturaInput.addEventListener('change', function () {
        const facturaNumber = facturaInput.value;

        if (facturaNumber) {
            fetch(`/api/get-factura-data/?factura=${facturaNumber}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        cedulaInput.value = data.data.cedula || '';
                        nombreCompletoInput.value = data.data.nombre_completo || '';
                        direccionInput.value = data.data.direccion || '';
                        valorIngresoInput.value = data.data.valorIngreso || '';
                    } else {
                        alert(data.error);
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    });
});