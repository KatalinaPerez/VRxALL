document.addEventListener("DOMContentLoaded", () => {
    const mainImg = document.getElementById("main-img");
    const thumbnails = Array.from(document.querySelectorAll(".thumb"));
    let currentIndex = 0;

    function updateThumbnails(startIndex) {
        thumbnails.forEach((thumb, i) => {
            thumb.style.display = "none"; // ocultamos todas
        });
        // mostramos las 4 miniaturas empezando desde startIndex
        for (let i = 0; i < 4; i++) {
            const index = (startIndex + i + 1) % thumbnails.length; // +1 porque la principal no se muestra abajo
            thumbnails[index].style.display = "block";
        }
    }

    // inicializar miniaturas
    updateThumbnails(currentIndex);

    thumbnails.forEach((thumb, i) => {
        thumb.addEventListener("click", () => {
            mainImg.src = thumb.src;        // cambiar imagen grande
            currentIndex = i;               // nueva principal
            updateThumbnails(currentIndex); // rotar miniaturas
        });
    });
});