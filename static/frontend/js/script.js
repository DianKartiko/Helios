// Infinite slider carousel
document.addEventListener('DOMContentLoaded', function () {
    const slideTrack = document.querySelector('.slide-track');
    const slides = document.querySelectorAll('.slide');
    
    // Clone the slides to create the infinite effect
    slides.forEach(slide => {
        const clone = slide.cloneNode(true);
        slideTrack.appendChild(clone);
    });
});

