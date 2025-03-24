document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Validar que el usuario sea 'admin' y la contraseña sea 'admin123'
    if (username === "admin" && password === "admin123") {
        // Si el usuario y la contraseña son correctos, redirigir al index
        sessionStorage.setItem("loggedIn", "true");  // Guardamos el estado de login
        window.location.href = "index.html";  // Redirige a la página principal
    } else {
        alert("Usuario o contraseña incorrectos. Inténtalo de nuevo.");
    }
});
