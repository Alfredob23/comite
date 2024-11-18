function updateTotal() {
    let total = 0;
    const biologicos = document.getElementsByName("biologico[]");
    const cantidades = document.getElementsByName("cantidad[]");

    for (let i = 0; i < biologicos.length; i++) {
        const nombreBiologico = biologicos[i].value;
        const cantidad = parseInt(cantidades[i].value) || 0;

        fetch(`/obtener_precio_biologico/?biologico=${nombreBiologico}`)
            .then(response => response.json())
            .then(data => {
                if (data.precio) {
                    total += data.precio * cantidad;
                }
                document.getElementById("total").value = total.toFixed(2);
            })
            .catch(error => {
                console.error("Hubo un problema con la solicitud AJAX:", error);
            });
    }
}