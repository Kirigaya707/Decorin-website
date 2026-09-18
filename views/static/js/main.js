document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.hero-slide');
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    let currentSlide = 0;

    if (slides.length > 1) {
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 5000);
    }

    toggle?.addEventListener('click', () => links?.classList.toggle('open'));
});