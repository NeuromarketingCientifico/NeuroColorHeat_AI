document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Validar que la contraseña sea la correcta
    if (password === "admin123") {
        // Si la contraseña es correcta, redirigir al index
        window.location.href = "index.html";  // Redirige a la página principal
    } else {
        alert("Contraseña incorrecta. Inténtalo de nuevo.");
    }
});
