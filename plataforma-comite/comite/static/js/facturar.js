let count = 1;
function addCantidadLoteFields() {
    count++;
    const contenedorAdicional = document.getElementById('campos-adicionales');

    const nuevoDiv = document.createElement('div');
    nuevoDiv.classList.add('form-group');
    nuevoDiv.style.display = 'flex';
    nuevoDiv.style.gap = '10px';
    nuevoDiv.style.alignItems = 'center';

    // Crear campo de Biológico
    const nuevoBiologicoDiv = document.createElement('div');
    nuevoBiologicoDiv.style.flex = '1';
    const nuevoBiologicoLabel = document.createElement('label');
    nuevoBiologicoLabel.textContent = 'Biológico:';
    const nuevoBiologicoSelect = document.createElement('select');
    nuevoBiologicoSelect.classList.add('form-control');
    nuevoBiologicoSelect.name = 'biologico[]';
    nuevoBiologicoSelect.id = `biologico${count}`;
    nuevoBiologicoSelect.setAttribute('onchange', 'updateTotal()'); // Asignar evento onchange

    const opciones = ['Aftosa', 'Cepa19', 'Rabia'];
    opciones.forEach(opcion => {
        const optionElement = document.createElement('option');
        optionElement.value = opcion;
        optionElement.textContent = opcion;
        nuevoBiologicoSelect.appendChild(optionElement);
    });

    nuevoBiologicoDiv.appendChild(nuevoBiologicoLabel);
    nuevoBiologicoDiv.appendChild(nuevoBiologicoSelect);

    // Crear campo de Cantidad
    const nuevaCantidadDiv = document.createElement('div');
    nuevaCantidadDiv.style.flex = '1';
    const nuevaCantidadLabel = document.createElement('label');
    nuevaCantidadLabel.textContent = 'Cantidad:';
    const nuevaCantidadInput = document.createElement('input');
    nuevaCantidadInput.type = 'number';
    nuevaCantidadInput.classList.add('form-control');
    nuevaCantidadInput.name = 'cantidad[]';
    nuevaCantidadInput.id = `cantidad${count}`;
    nuevaCantidadInput.setAttribute('oninput', 'updateTotal()'); // Asignar evento oninput

    nuevaCantidadDiv.appendChild(nuevaCantidadLabel);
    nuevaCantidadDiv.appendChild(nuevaCantidadInput);

    // Crear campo de Lote
    const nuevoLoteDiv = document.createElement('div');
    nuevoLoteDiv.style.flex = '1';
    const nuevoLoteLabel = document.createElement('label');
    nuevoLoteLabel.textContent = 'Lote:';
    const nuevoLoteInput = document.createElement('input');
    nuevoLoteInput.type = 'text';
    nuevoLoteInput.classList.add('form-control');
    nuevoLoteInput.name = 'lote[]';
    nuevoLoteInput.id = `lote${count}`;

    nuevoLoteDiv.appendChild(nuevoLoteLabel);
    nuevoLoteDiv.appendChild(nuevoLoteInput);

    // Agregar los divs al contenedor principal
    nuevoDiv.appendChild(nuevoBiologicoDiv);
    nuevoDiv.appendChild(nuevaCantidadDiv);
    nuevoDiv.appendChild(nuevoLoteDiv);

    contenedorAdicional.appendChild(nuevoDiv);
}