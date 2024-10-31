function addCantidadLoteFields() {
    const contenedorAdicional = document.getElementById('campos-adicionales');

    // Crear un nuevo div contenedor para los nuevos campos
    const nuevoDiv = document.createElement('div');
    nuevoDiv.classList.add('form-group');
    nuevoDiv.style.display = 'flex';
    nuevoDiv.style.gap = '10px';
    nuevoDiv.style.alignItems = 'center';
    nuevoDiv.style.marginTop = '10px';

    // Crear el nuevo campo de Biológico
    const nuevoBiologicoDiv = document.createElement('div');
    nuevoBiologicoDiv.style.flex = '1';
    const nuevoBiologicoLabel = document.createElement('label');
    nuevoBiologicoLabel.textContent = 'Biológico:';
    const nuevoBiologicoSelect = document.createElement('select');
    nuevoBiologicoSelect.classList.add('form-control');
    nuevoBiologicoSelect.name = 'biologico[]'; // Array de "tipo_pago" para múltiples valores
    nuevoBiologicoSelect.required = true; // Hacer que sea obligatorio

    // Opciones del select
    const opciones = ['Aftosa', 'Cepa19', 'Rabia'];
    opciones.forEach(opcion => {
        const optionElement = document.createElement('option');
        optionElement.value = opcion;
        optionElement.textContent = opcion;
        nuevoBiologicoSelect.appendChild(optionElement);
    });

    // Agregar el label y el select de biológico al div de biológico
    nuevoBiologicoDiv.appendChild(nuevoBiologicoLabel);
    nuevoBiologicoDiv.appendChild(nuevoBiologicoSelect);

    // Crear el nuevo campo de Cantidad
    const nuevaCantidadDiv = document.createElement('div');
    nuevaCantidadDiv.style.flex = '1';
    const nuevaCantidadLabel = document.createElement('label');
    nuevaCantidadLabel.textContent = 'Cantidad:';
    const nuevaCantidadInput = document.createElement('input');
    nuevaCantidadInput.type = 'number';
    nuevaCantidadInput.classList.add('form-control');
    nuevaCantidadInput.name = 'cantidad[]'; // Array de "cantidad" para múltiples valores
    nuevaCantidadInput.maxLength = 20;
    
    // Agregar el label y el input de cantidad al div de cantidad
    nuevaCantidadDiv.appendChild(nuevaCantidadLabel);
    nuevaCantidadDiv.appendChild(nuevaCantidadInput);

    // Crear el nuevo campo de Lote
    const nuevoLoteDiv = document.createElement('div');
    nuevoLoteDiv.style.flex = '1';
    const nuevoLoteLabel = document.createElement('label');
    nuevoLoteLabel.textContent = 'Lote:';
    const nuevoLoteInput = document.createElement('input');
    nuevoLoteInput.type = 'text';
    nuevoLoteInput.classList.add('form-control');
    nuevoLoteInput.name = 'lote[]'; // Array de "lote" para múltiples valores
    nuevoLoteInput.maxLength = 20;
    
    // Agregar el label y el input de lote al div de lote
    nuevoLoteDiv.appendChild(nuevoLoteLabel);
    nuevoLoteDiv.appendChild(nuevoLoteInput);
    
    // Agregar los divs de biológico, cantidad y lote al nuevo div contenedor
    nuevoDiv.appendChild(nuevoBiologicoDiv);
    nuevoDiv.appendChild(nuevaCantidadDiv);
    nuevoDiv.appendChild(nuevoLoteDiv);
    
    // Agregar el nuevo div al contenedor de campos adicionales
    contenedorAdicional.appendChild(nuevoDiv);
}

