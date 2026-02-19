/**
 * Scroll Effects (Vanilla JS)
 */

if (window._echoScrollListener) {
    window.removeEventListener('scroll', window._echoScrollListener);
}

let isMobile = false;
let scrollTargets = [];

function onScroll() {
    if (!isMobile) return;

    // The screen's exact horizontal center crosshair
    const centerY = window.innerHeight / 2;
    // 22% band (11% above the center line, 11% below)
    const threshold = window.innerHeight * 0.11;

    scrollTargets.forEach(target => {
        const rect = target.getBoundingClientRect();

        // Optimization: skip elements entirely off-screen
        if (rect.bottom < 0 || rect.top > window.innerHeight) {
            target.classList.remove('in-view');
            return;
        }

        // Calculate the physical center of the target element
        const targetCenterY = rect.top + rect.height / 2;
        const distance = Math.abs(centerY - targetCenterY);

        // Does the center of the element fall into our crossing threshold?
        if (distance <= threshold) {
            target.classList.add('in-view');
        } else {
            target.classList.remove('in-view');
        }
    });
}

// Preserve reference for HMR cleanup
window._echoScrollListener = onScroll;

function initializeScrollEffects() {
    isMobile = window.matchMedia('(max-width: 1023px)').matches;
    scrollTargets = Array.from(document.querySelectorAll('[data-scroll-spotlight]'));

    window.removeEventListener('scroll', window._echoScrollListener);

    if (isMobile) {
        window.addEventListener('scroll', window._echoScrollListener, { passive: true });
        window._echoScrollListener(); // Fire once immediately
    } else {
        // Desktop: Clean up any leftover effects
        scrollTargets.forEach(el => el.classList.remove('in-view'));
    }
}

// Initialize on page load or immediate if already loaded (for Vite HMR)
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeScrollEffects);
} else {
    initializeScrollEffects();
}

// Re-initialize when viewport size changes
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(initializeScrollEffects, 100);
});
