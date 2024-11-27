let index = 0;

function mostrarImagen() {
    const imagenes = document.querySelectorAll('.carrusel-imagenes img');
    index = (index + 1) % imagenes.length; // Ciclar entre las imágenes
    const desplazamiento = -index * 100; // Calcular el desplazamiento
    document.querySelector('.carrusel-imagenes').style.transform = `translateX(${desplazamiento}%)`;
}

// Cambia la imagen cada 5 segundos (5000 milisegundos)
setInterval(mostrarImagen, 10000);
