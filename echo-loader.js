// ========================================
// ECHO AVU - GLOBAL HEADER & FOOTER LOADER
// ========================================
// This file provides ONE source of truth for the site's navigation and footer.
// All HTML pages load these components dynamically via JavaScript injection.

/**
 * LOAD HEADER
 * Injects the navigation bar and mobile menu into the DOM
 */
function loadHeader() {
  const headerHTML = `
    <!-- NAVBAR -->
    <nav class="fixed top-0 w-full z-50 transition-all duration-300 bg-black/80 backdrop-blur-md border-b border-white/5">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <a href="/index.html" class="block group">
          <img src="/Echo-Avu-White.png" alt="Echo AVU"
            class="h-10 w-auto object-contain opacity-90 group-hover:opacity-100 transition-opacity">
        </a>
        <div class="hidden lg:flex items-center gap-8">
          <a href="/car-audio.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Car Audio</a>
          <a href="/car-starters.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Remote Starters</a>
          <a href="/marine-audio.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Marine</a>
          <a href="/home-audio.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Home Audio</a>
          <a href="/tv-video.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">TV &amp; Video</a>
          <a href="/surveillance.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Surveillance</a>
          <a href="/brands.html"
            class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Brands</a>
          <!-- Services Dropdown -->
          <div class="relative group">
            <a href="/services.html"
              class="flex items-center gap-1 text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300 focus:outline-none">
              Services
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:rotate-180" fill="none"
                stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </a>
            <!-- Dropdown Menu -->
            <div class="absolute right-0 mt-2 w-56 bg-carbon border border-edge rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform origin-top-right z-50">
              <div class="py-2">
                <a href="/services-residential.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Residential Integration</a>
                <a href="/services-office.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Office &amp; Boardroom</a>
                <a href="/services-retail.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Retail &amp; Hospitality</a>
                <a href="/services-surveillance.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Surveillance &amp; Security</a>
                <a href="/services-car-audio.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Vehicle Installations</a>
                <a href="/services-car-starters.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Remote Car Starters</a>
                <a href="/services-marine.html"
                  class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Marine &amp; Powersports</a>
              </div>
            </div>
          </div>
          <!-- Contact CTA Button -->
          <a href="/contact.html" id="nav-contact-cta"
             style="padding:8px 20px;font-size:0.875rem;font-weight:700;color:#D60000;border:1px solid #D60000;border-radius:4px;text-transform:uppercase;letter-spacing:0.05em;text-decoration:none;white-space:nowrap;display:inline-block;">
             Contact
          </a>
        </div>
        <button id="mobile-menu-toggle" class="lg:hidden text-white p-2">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </button>
      </div>
    </nav>

    <!-- MOBILE MENU OVERLAY -->
    <div id="mobile-menu-overlay"
      class="fixed inset-0 z-40 bg-void transform translate-x-full transition-transform duration-500 ease-out flex flex-col h-[100dvh]">
      <div class="flex flex-col h-full">
        <!-- Close Button -->
        <div class="flex justify-end p-6">
          <button id="mobile-menu-close" class="text-white p-2">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Scrollable Menu Content -->
        <div class="flex-1 overflow-y-auto px-6 pb-6">
          <nav class="space-y-8">
            <div class="space-y-4">
              <!-- ACCORDION 1: DEPARTMENTS -->
              <details class="group/accordion border-b border-white/10 pb-4">
                <summary
                  class="flex justify-between items-center font-heading font-bold text-xl text-white cursor-pointer list-none select-none">
                  Departments
                  <svg class="w-5 h-5 text-echoRed transition-transform duration-300 group-open/accordion:rotate-180"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div class="mt-4 space-y-3 pl-4 border-l border-white/10 ml-1">
                  <a href="/car-audio.html" class="block text-gray-400 hover:text-white transition-colors py-1">Car Audio</a>
                  <a href="/car-starters.html" class="block text-gray-400 hover:text-white transition-colors py-1">Remote Car Starters</a>
                  <a href="/marine-audio.html" class="block text-gray-400 hover:text-white transition-colors py-1">Marine &amp; Powersports</a>
                  <a href="/home-audio.html" class="block text-gray-400 hover:text-white transition-colors py-1">Home Audio &amp; Hi-Fi</a>
                  <a href="/tv-video.html" class="block text-gray-400 hover:text-white transition-colors py-1">TV &amp; Cinema</a>
                  <a href="/surveillance.html" class="block text-gray-400 hover:text-white transition-colors py-1">Surveillance</a>
                </div>
              </details>

              <!-- ACCORDION 2: SERVICES -->
              <details class="group/accordion border-b border-white/10 pb-4">
                <summary
                  class="flex justify-between items-center font-heading font-bold text-xl text-white cursor-pointer list-none select-none">
                  Services
                  <svg class="w-5 h-5 text-echoRed transition-transform duration-300 group-open/accordion:rotate-180"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div class="mt-4 space-y-3 pl-4 border-l border-white/10 ml-1">
                  <a href="/services-residential.html" class="block text-gray-400 hover:text-white transition-colors py-1">Residential Integration</a>
                  <a href="/services-office.html" class="block text-gray-400 hover:text-white transition-colors py-1">Office &amp; Boardroom</a>
                  <a href="/services-retail.html" class="block text-gray-400 hover:text-white transition-colors py-1">Retail &amp; Hospitality</a>
                  <a href="/services-surveillance.html" class="block text-gray-400 hover:text-white transition-colors py-1">Surveillance &amp; Security</a>
                  <a href="/services-car-audio.html" class="block text-gray-400 hover:text-white transition-colors py-1">Vehicle Installations</a>
                  <a href="/services-car-starters.html" class="block text-gray-400 hover:text-white transition-colors py-1">Remote Car Starters</a>
                  <a href="/services-marine.html" class="block text-gray-400 hover:text-white transition-colors py-1">Marine &amp; Powersports</a>
                </div>
              </details>

              <!-- ACCORDION 3: SUPPORT -->
              <details class="group/accordion border-b border-white/10 pb-4">
                <summary
                  class="flex justify-between items-center font-heading font-bold text-xl text-white cursor-pointer list-none select-none">
                  Support
                  <svg class="w-5 h-5 text-echoRed transition-transform duration-300 group-open/accordion:rotate-180"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </summary>
                <div class="mt-4 space-y-3 pl-4 border-l border-white/10 ml-1">
                  <a href="/financing.html" class="block text-gray-400 hover:text-white transition-colors py-1">Financing Application</a>
                  <a href="/protection-plan.html" class="block text-gray-400 hover:text-white transition-colors py-1">Guaranteed Protection</a>
                  <a href="/return-policy.html" class="block text-gray-400 hover:text-white transition-colors py-1">Return Policy</a>
                  <a href="/privacy-statement.html" class="block text-gray-400 hover:text-white transition-colors py-1">Privacy Statement</a>
                  <a href="/brands.html" class="block text-gray-400 hover:text-white transition-colors py-1">Our Brands</a>
                </div>
              </details>

              <!-- VISIT US -->
              <div class="space-y-6 pt-2">
                <div class="space-y-3">
                  <a href="/about.html" class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">About Echo AVU</a>
                  <a href="/dream-home.html" class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">Rotary Dream Home</a>
                  <a href="/contact.html" class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">Contact Support</a>
                </div>
                <div class="space-y-4 pt-4 border-t border-white/5">
                  <div>
                    <p class="text-gray-400 text-sm">11101 100 St</p>
                    <p class="text-gray-400 text-sm">Grande Prairie, AB T8V 2N2</p>
                    <a href="https://maps.google.com/?q=11101+100+St,+Grande+Prairie,+AB+T8V+2N2" target="_blank"
                      class="inline-block mt-2 text-echoRed font-bold text-sm tracking-wide uppercase hover:text-white transition-colors">
                      Get Directions &rarr;
                    </a>
                  </div>
                  <a href="tel:7805381333"
                    class="block text-3xl font-heading font-bold text-white hover:text-echoRed transition-colors">
                    (780) 538-1333
                  </a>
                </div>
              </div>
            </div>
          </nav>
        </div>
      </div>
    </div>
  `;

  const headerContainer = document.getElementById('header-placeholder');
  if (headerContainer) {
    headerContainer.innerHTML = headerHTML;
  }

  // Hover effect for Contact CTA
  const ctaBtn = document.getElementById('nav-contact-cta');
  if (ctaBtn) {
    ctaBtn.addEventListener('mouseover', function () {
      this.style.backgroundColor = '#D60000';
      this.style.color = '#ffffff';
    });
    ctaBtn.addEventListener('mouseout', function () {
      this.style.backgroundColor = 'transparent';
      this.style.color = '#D60000';
    });
  }

  initializeMobileMenu();
  highlightActivePage();
}

/**
 * INITIALIZE MOBILE MENU
 */
function initializeMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const closeBtn = document.getElementById('mobile-menu-close');
  const overlay = document.getElementById('mobile-menu-overlay');
  const body = document.body;

  function toggleMenu() {
    const isClosed = overlay.classList.contains('translate-x-full');
    if (isClosed) {
      overlay.classList.remove('translate-x-full');
      body.style.overflow = 'hidden';
    } else {
      overlay.classList.add('translate-x-full');
      body.style.overflow = '';
    }
  }

  if (toggleBtn) toggleBtn.addEventListener('click', toggleMenu);
  if (closeBtn) closeBtn.addEventListener('click', toggleMenu);
}

/**
 * LOAD FOOTER
 */
function loadFooter() {
  const footerHTML = `
    <footer style="background:#000000;border-top:1px solid rgba(255,255,255,0.1);padding:4rem 0;font-family:Inter,sans-serif;font-size:0.875rem;">
      <div style="max-width:80rem;margin:0 auto;padding:0 1.5rem;">
        <div style="display:grid;grid-template-columns:repeat(1,1fr);gap:3rem;margin-bottom:4rem;" class="footer-grid">

          <!-- COLUMN 1: BRAND -->
          <div style="display:flex;flex-direction:column;gap:1.5rem;">
            <a href="/index.html">
              <img src="/Echo-Avu-White.png" alt="Echo AVU" style="height:3rem;width:auto;object-fit:contain;opacity:0.9;">
            </a>
            <p style="color:#6B7280;font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;">Audio. Video. Unlimited.</p>
            <div style="display:flex;gap:1rem;">
              <a href="https://www.facebook.com/EchoAVUGP" target="_blank" style="color:#9CA3AF;" aria-label="Facebook">
                <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              </a>
              <a href="https://www.instagram.com/echoaudiovideounlimited/" target="_blank" style="color:#9CA3AF;" aria-label="Instagram">
                <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
              </a>
            </div>
          </div>

          <!-- COLUMN 2: DEPARTMENTS -->
          <div>
            <h4 style="color:#ffffff;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:1.5rem;">Departments</h4>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.75rem;">
              <li><a href="/car-audio.html" style="color:#9CA3AF;text-decoration:none;">Car Audio</a></li>
              <li><a href="/car-starters.html" style="color:#9CA3AF;text-decoration:none;">Remote Car Starters</a></li>
              <li><a href="/marine-audio.html" style="color:#9CA3AF;text-decoration:none;">Marine &amp; Powersports</a></li>
              <li><a href="/home-audio.html" style="color:#9CA3AF;text-decoration:none;">Home Audio &amp; Hi-Fi</a></li>
              <li><a href="/tv-video.html" style="color:#9CA3AF;text-decoration:none;">TV &amp; Cinema</a></li>
              <li><a href="/surveillance.html" style="color:#9CA3AF;text-decoration:none;">Surveillance</a></li>
            </ul>
          </div>

          <!-- COLUMN 3: SERVICES -->
          <div>
            <h4 style="color:#ffffff;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:1.5rem;">Services</h4>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.75rem;">
              <li><a href="/services-residential.html" style="color:#9CA3AF;text-decoration:none;">Residential Integration</a></li>
              <li><a href="/services-office.html" style="color:#9CA3AF;text-decoration:none;">Office &amp; Boardroom</a></li>
              <li><a href="/services-retail.html" style="color:#9CA3AF;text-decoration:none;">Retail &amp; Hospitality</a></li>
              <li><a href="/services-surveillance.html" style="color:#9CA3AF;text-decoration:none;">Surveillance &amp; Security</a></li>
              <li><a href="/services-car-audio.html" style="color:#9CA3AF;text-decoration:none;">Vehicle Installations</a></li>
              <li><a href="/services-car-starters.html" style="color:#9CA3AF;text-decoration:none;">Remote Car Starters</a></li>
              <li><a href="/services-marine.html" style="color:#9CA3AF;text-decoration:none;">Marine &amp; Powersports</a></li>
            </ul>
          </div>

          <!-- COLUMN 4: SUPPORT -->
          <div>
            <h4 style="color:#ffffff;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:1.5rem;">Support</h4>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.75rem;">
              <li><a href="/financing.html" style="color:#9CA3AF;text-decoration:none;">Financing Application</a></li>
              <li><a href="/protection-plan.html" style="color:#9CA3AF;text-decoration:none;">Guaranteed Protection</a></li>
              <li><a href="/return-policy.html" style="color:#9CA3AF;text-decoration:none;">Return Policy</a></li>
              <li><a href="/privacy-statement.html" style="color:#9CA3AF;text-decoration:none;">Privacy Statement</a></li>
              <li><a href="/brands.html" style="color:#9CA3AF;text-decoration:none;">Our Brands</a></li>
            </ul>
          </div>

          <!-- COLUMN 5: VISIT US -->
          <div>
            <h4 style="color:#ffffff;font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:1.5rem;">Visit Us</h4>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.75rem;margin-bottom:1.5rem;">
              <li><a href="/about.html" style="color:#9CA3AF;text-decoration:none;">About Echo AVU</a></li>
              <li><a href="/dream-home.html" style="color:#9CA3AF;text-decoration:none;">Rotary Dream Home</a></li>
              <li><a href="/contact.html" style="color:#9CA3AF;text-decoration:none;">Contact Support</a></li>
            </ul>
            <div style="height:1px;background:rgba(255,255,255,0.1);margin-bottom:1.5rem;"></div>
            <div style="display:flex;flex-direction:column;gap:1rem;">
              <div>
                <p style="color:#D1D5DB;margin:0;">11101 100 St, Grande Prairie, AB T8V 2N2</p>
                <a href="https://maps.google.com/?q=11101+100+St,+Grande+Prairie,+AB+T8V+2N2" target="_blank"
                  style="display:inline-block;margin-top:0.5rem;color:#D60000;font-weight:700;font-size:0.875rem;letter-spacing:0.05em;text-transform:uppercase;text-decoration:none;">
                  Get Directions
                </a>
              </div>
              <a href="tel:7805381333" style="color:#ffffff;font-weight:700;font-size:1.25rem;text-decoration:none;">(780) 538-1333</a>
            </div>
          </div>

        </div>

        <!-- BOTTOM BAR -->
        <div style="border-top:1px solid #1F1F1F;padding-top:2rem;padding-bottom:1rem;">
          <p style="text-align:center;font-size:0.75rem;color:#4B5563;margin:0;">&copy; 2026 Echo Audio Video Unlimited. All rights reserved.</p>
        </div>
      </div>

      <style>
        @media(min-width:768px){.footer-grid{grid-template-columns:repeat(5,1fr)!important;}}
        footer a:hover{color:#D60000!important;}
      </style>
    </footer>
  `;

  const footerContainer = document.getElementById('footer-placeholder');
  if (footerContainer) {
    footerContainer.innerHTML = footerHTML;
  }
}

/**
 * HIGHLIGHT ACTIVE PAGE
 */
function highlightActivePage() {
  const currentPath = window.location.pathname;
  const currentPage = currentPath.split('/').pop() || 'index.html';

  const navLinks = document.querySelectorAll('nav a[href], #mobile-menu-overlay a[href]');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    // Skip the Contact CTA button - it has its own styling
    if (link.id === 'nav-contact-cta') return;

    const linkPage = href.split('/').pop().split('?')[0].split('#')[0];

    if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
      link.classList.remove('text-gray-400', 'text-gray-300');
      link.classList.add('text-echoRed');

      if (link.closest('#mobile-menu-overlay')) {
        link.classList.add('font-bold');
      }
    }
  });
}

// ========================================
// AUTO-INITIALIZE ON PAGE LOAD
// ========================================
document.addEventListener('DOMContentLoaded', () => {
  loadHeader();
  loadFooter();
});
