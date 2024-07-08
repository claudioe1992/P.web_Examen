function InicioSesion() {
    let user = document.getElementById("Usuario").value;
    let pass = document.getElementById("Contraseña").value;

    if (user === 'martinjara123@gmail.com' && pass === '1234') {
        // Si las credenciales son correctas, redirecciona al usuario al spinner después de 2 segundos
        setTimeout(function() {
            window.location.href = "cargar.html"; // Cambia esto por la ruta correcta de tu página del spinner
        }) // 2000 milisegundos = 2 segundos
    } else {
        // Si las credenciales son incorrectas, muestra un mensaje de alerta
        alert("Datos Incorrectos! Intentelo de nuevo");
    }
}