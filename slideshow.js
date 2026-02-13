// Slideshow functionality for car-audio.html and marine-audio.html
function initSlideshows() {
    // Car Audio slideshows
    initSlideshow('.f250-slideshow', '.slideshow-image', 3000);
    initSlideshow('.f150-slideshow', '.slideshow-image', 3000);

    // Marine Audio slideshows
    initSlideshow('.brattjett-slideshow', '.marine-slideshow-image', 3000);
    initSlideshow('.canam-slideshow', '.marine-slideshow-image', 3000);
}

function initSlideshow(containerSelector, imageSelector, interval = 3000) {
    const container = document.querySelector(containerSelector);
    if (!container) return;

    const images = container.querySelectorAll(imageSelector);
    if (images.length <= 1) return; // No need for slideshow if only 1 image

    let currentIndex = 0;

    function showNextImage() {
        // Remove active class from current image
        images[currentIndex].classList.remove('active');

        // Move to next image
        currentIndex = (currentIndex + 1) % images.length;

        // Add active class to new current image
        images[currentIndex].classList.add('active');
    }

    // Start the slideshow
    setInterval(showNextImage, interval);
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSlideshows);
} else {
    initSlideshows();
}
