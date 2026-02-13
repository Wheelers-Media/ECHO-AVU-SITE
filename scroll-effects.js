/**
 * Scroll Effects (Vanilla JS)
 * Replicating the Framer Motion "WhileInView" logic for mobile devices.
 * 
 * Logic:
 * - Observer monitors elements with [data-scroll-spotlight]
 * - When element enters the "Hot Zone" (Middle 60% of viewport), add class 'in-view'
 * - CSS/Tailwind selects this class to apply specific styles (grayscale-0, scale, etc.)
 * - Auto-disables on desktop viewports (≥1024px) and re-enables when resizing back to mobile
 */

let observer = null;
let isObserverActive = false;

function initializeScrollEffects() {
    // Check if we're on mobile/tablet (viewport < 1024px)
    const isMobile = window.matchMedia('(max-width: 1023px)').matches;

    if (isMobile && !isObserverActive) {
        // Mobile: Enable scroll effects
        const observerOptions = {
            root: null,
            rootMargin: '-20% 0px -20% 0px', // Matches wider "Hot Zone" (Middle 60%)
            threshold: 0
        };

        observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                } else {
                    entry.target.classList.remove('in-view');
                }
            });
        }, observerOptions);

        // Target specific elements
        const targets = document.querySelectorAll('[data-scroll-spotlight]');
        targets.forEach(target => observer.observe(target));
        isObserverActive = true;

    } else if (!isMobile && isObserverActive) {
        // Desktop: Disable scroll effects and clean up
        if (observer) {
            observer.disconnect();
            observer = null;
        }
        // Remove all .in-view classes on desktop
        document.querySelectorAll('.in-view').forEach(el => el.classList.remove('in-view'));
        isObserverActive = false;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initializeScrollEffects);

// Re-initialize when viewport size changes
window.addEventListener('resize', initializeScrollEffects);
