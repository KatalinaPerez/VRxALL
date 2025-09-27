const mainImg = document.getElementById('main-img');
const thumbnails = document.querySelectorAll('.thumbnail-row .thumb');

let images = [];
thumbnails.forEach(thumb => images.push(thumb.dataset.src));
images.unshift(mainImg.dataset.src); // agregamos la imagen grande al inicio


let currentIndex = 0;

function rotateCarousel() {
    // Imagen grande
    mainImg.src = images[currentIndex];

    // Miniaturas
    for (let i = 0; i < thumbnails.length; i++) {
        let imgIndex = (currentIndex + i + 1) % images.length;
        thumbnails[i].src = images[imgIndex];
    }

    // Siguiente imagen
    currentIndex = (currentIndex + 1) % images.length;
}

// Rotar cada 3 segundos
setInterval(rotateCarousel, 3000);
