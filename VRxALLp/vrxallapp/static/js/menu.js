// Contenido para tu archivo /static/js/menu.js

document.addEventListener('DOMContentLoaded', function() {
    
    // Selecciona el contenedor principal del menú
    var userMenu = document.querySelector('.user-menu');

    // Si el menú no existe en esta página, no hagas nada.
    if (!userMenu) {
        return;
    }
    
    // 1. Función para "prender" o "apagar" el menú
    function toggleMenu(event) {
        // Evita que el clic se propague (necesario para el paso 2)
        event.stopPropagation(); 
        
        // Añade o quita la clase 'active' al contenedor
        userMenu.classList.toggle('active');
    }

    // 2. Cierra el menú si se hace clic en cualquier otra parte de la página
    function closeMenuOnClickOutside(event) {
        // Si el menú está activo (visible) Y el clic fue FUERA del menú...
        if (userMenu.classList.contains('active') && !userMenu.contains(event.target)) {
            // ...ciérralo
            userMenu.classList.remove('active');
        }
    }

    // 3. Asigna los "oyentes" de eventos
    //    - Cuando se haga clic en el menú, ejecuta la función toggleMenu
    userMenu.addEventListener('click', toggleMenu);
    
    //    - Cuando se haga clic en cualquier parte del documento, 
    //      ejecuta la función para cerrar si se hizo clic fuera
    document.addEventListener('click', closeMenuOnClickOutside);
});