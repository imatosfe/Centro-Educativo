let index = 0;

function showSlide(n) {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    index = (n + totalSlides) % totalSlides; // Asegurarse de que index esté en rango
    slides.style.transform = `translateX(-${index * 100}%)`;
}

document.getElementById('prevBtn').addEventListener('click', () => showSlide(index - 1));
document.getElementById('nextBtn').addEventListener('click', () => showSlide(index + 1));

// Auto-slide cada 5 segundos
setInterval(() => showSlide(index + 1), 5000);