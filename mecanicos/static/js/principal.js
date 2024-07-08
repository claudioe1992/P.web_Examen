$(function () {
    $('[data-toggle="popover"]').popover();
  });

  document.addEventListener("DOMContentLoaded", function(event) {
    // Muestra el spinner cuando se carga completamente el DOM
    document.getElementById("html-spinner").style.display = "block";

    // Después de 4 segundos, redirecciona al usuario a la página principal
    setTimeout(function() {
        window.location.href = "crud.html"; // Cambia esto por la ruta correcta de tu página principal
    }, 4000); // 4000 milisegundos = 4 segundos
});