$(document).ready(function(){
    $('#cedula').on('blur', function() {
        var cedula = $(this).val();
        
        if (cedula) {
            $.ajax({
                url: verificarCedulaUrl, // Usamos la variable que definimos en el HTML
                type: "GET",
                data: {'cedula': cedula},
                success: function(response) {
                    if (response.usuario) {
                        // Llenar los campos con los datos del usuario si existe
                        $('#nombre_completo').val(response.usuario.nombre_completo);
                        $('#direccion').val(response.usuario.direccion);
                    } else {
                        // Limpiar los campos si no hay coincidencia
                        $('#nombre_completo').val('');
                        $('#direccion').val('');
                    }
                }
            });
        }
    });
});