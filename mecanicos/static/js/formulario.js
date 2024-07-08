function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var correo = document.getElementById("correo").value;
    var contraseña = document.getElementById("contraseña").value;
    var numero = document.getElementById("numero").value;
    var ciudad = document.getElementById("ciudad").value;

    // Validar campo Nombre
    if (nombre.trim() == "") {
        mostrarError("error-nombre", "Por favor, ingresa tu nombre.");
        return false;
    } else {
        ocultarError("error-nombre");
    }

    // Validar campo Apellido
    if (apellido.trim() == "") {
        mostrarError("error-apellido", "Por favor, ingresa tu apellido.");
        return false;
    } else {
        ocultarError("error-apellido");
    }

    // Validar campo Correo Electrónico
    if (correo.trim() == "") {
        mostrarError("error-correo", "Por favor, ingresa tu correo electrónico.");
        return false;
    } else if (!correo.includes("@")) {
        mostrarError("error-correo", "Por favor, ingresa un correo electrónico válido.");
        return false;
    } else {
        ocultarError("error-correo");
    }

    // Validar campo Contraseña
    if (contraseña.trim() == "") {
        mostrarError("error-contraseña", "Por favor, ingresa tu contraseña.");
        return false;
    } else {
        ocultarError("error-contraseña");
    }

    // Validar campo Número
    if (numero.trim() == "") {
        mostrarError("error-numero", "Por favor, ingresa tu número.");
        return false;
    } else {
        ocultarError("error-numero");
    }

    // Validar campo Ciudad
    if (ciudad.trim() == "") {
        mostrarError("error-ciudad", "Por favor, ingresa tu ciudad.");
        return false;
    } else {
        ocultarError("error-ciudad");
    }

    return true; // Si llega aquí, el formulario es válido
}

function mostrarError(id, mensaje) {
    var errorElement = document.getElementById(id);
    errorElement.textContent = mensaje;
    error
}