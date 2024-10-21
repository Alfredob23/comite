document.getElementById('concepto').addEventListener('change', function() {
    var otroConceptoDiv = document.getElementById('otro-concepto');
    if (this.value === 'Otro') {
        otroConceptoDiv.style.display = 'block'; // Muestra el campo si selecciona "Otro"
    } else {
        otroConceptoDiv.style.display = 'none';  // Oculta el campo en caso contrario
    }
});