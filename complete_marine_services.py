"""
Complete services-marine.html footer and update navigation across all files
"""
import re

# Step 1: Add footer and mobile menu to services-marine.html
footer_and_scripts = '''
    <footer class="bg-void border-t border-white/10 py-16 font-body text-sm">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 mb-16">
                <!-- COLUMN 1: BRAND IDENTITY -->
                <div class="space-y-6">
                    <a href="/index.html" class="block">
                        <img src="/Echo-Avu-White.png" alt="Echo AVU"
                            class="h-12 w-auto object-contain opacity-90 hover:opacity-100 transition-opacity">
                    </a>
                    <p class="text-gray-500 text-xs tracking-wider uppercase">Audio. Video. Unlimited.</p>
                    <div class="flex gap-4">
                        <a href="https://www.facebook.com/EchoAVUGP" target="_blank"
                            class="text-gray-400 hover:text-echoRed transition-colors" aria-label="Facebook">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                <path
                                    d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                            </svg>
                        </a>
                        <a href="https://www.instagram.com/echoaudiovideounlimited/" target="_blank"
                            class="text-gray-400 hover:text-echoRed transition-colors" aria-label="Instagram">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                <path
                                    d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z" />
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- COLUMN 2: DEPARTMENTS -->
                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Departments</h4>
                    <ul class="space-y-3">
                        <li><a href="/car-audio.html"
                                class="text-gray-400 hover:text-echoRed transition-colors duration-200">Car Audio</a>
                        <a href="/marine-audio.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Marine & Powersports</a>
                        <a href="/home-audio.html" class="block text-gray-400 hover:text-white transition-colors py-1">Home
                            Audio & Hi-Fi</a>
                        <a href="/tv-video.html" class="block text-gray-400 hover:text-white transition-colors py-1">TV &
                            Cinema</a>
                        <a href="/surveillance.html" class="block text-gray-400 hover:text-white transition-colors py-1">Surveillance</a>
                        <a href="/brands.html" class="block text-gray-400 hover:text-white transition-colors py-1">Our
                            Brands</a>
                    </ul>
                </div>

                <!-- COLUMN 3: SERVICES -->
                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Services</h4>
                    <ul class="space-y-3">
                        <a href="/services-residential.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Residential Integration</a>
                        <a href="/services-office.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Office & Boardroom</a>
                        <a href="/services-retail.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Retail & Hospitality</a>
                        <a href="/services-marine.html"
                            class="block text-white font-medium">Marine & Powersports</a>
                        <a href="/services-car-audio.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Vehicle Installations</a>
                    </ul>
                </div>

                <!-- COLUMN 4: SUPPORT -->
                <div>
                    <h4 class="text-white font-bold uppercase tracking-wider mb-6">Support</h4>
                    <ul class="space-y-3">
                        <a href="/financing.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Financing Application</a>
                        <a href="/protection-plan.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Guaranteed Protection</a>
                        <a href="/return-policy.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Return Policy</a>
                        <a href="/privacy-statement.html"
                            class="block text-gray-400 hover:text-white transition-colors py-1">Privacy Statement</a>
                    </ul>
                </div>

                <!-- COLUMN 5: CONTACT -->
                <div class="space-y-6">
                    <div class="space-y-3">
                        <a href="/about.html"
                            class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">About
                            Echo AVU</a>
                        <a href="/contact.html"
                            class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">Contact
                            Support</a>
                    </div>
                    <div class="space-y-4 border-t border-white/5 pt-4">
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

            <!-- COPYRIGHT -->
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-gray-500 text-xs">© 2025 Echo Audio Video Unlimited. All rights reserved.</p>
                <div class="flex gap-6">
                    <a href="/privacy-statement.html"
                        class="text-xs text-gray-500 hover:text-echoRed transition-colors">Privacy</a>
                    <a href="/return-policy.html"
                        class="text-xs text-gray-500 hover:text-echoRed transition-colors">Returns</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- MOBILE MENU OVERLAY -->
    <div id="mobile-menu-overlay"
        class="fixed inset-0 bg-black/95 backdrop-blur-md z-40 translate-x-full transition-transform duration-300">
        <div class="flex flex-col h-full px-6 pt-24 pb-6">
            <nav class="flex flex-col gap-6">
                <a href="/car-audio.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Car Audio</a>
                <a href="/car-starters.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Remote Starters</a>
                <a href="/marine-audio.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Marine Audio</a>
                <a href="/tv-video.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">TV / Video</a>
                <a href="/home-audio.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Home Audio</a>
                <a href="/surveillance.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Surveillance</a>
                <a href="/brands.html"
                    class="text-lg font-medium text-gray-400 hover:text-white transition-colors">Brands</a>

                <!-- Services Accordion -->
                <div class="border-t border-white/10 pt-6">
                    <button id="mobile-services-toggle"
                        class="flex items-center justify-between w-full text-lg font-medium text-gray-400 hover:text-white transition-colors">
                        <span>Services</span>
                        <svg class="w-5 h-5 transition-transform duration-300" fill="none" stroke="currentColor"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>
                    <div id="mobile-services-menu" class="hidden flex-col gap-4 mt-4 ml-4">
                        <a href="/services-residential.html"
                            class="text-base text-gray-400 hover:text-white transition-colors">Residential</a>
                        <a href="/services-office.html"
                            class="text-base text-gray-400 hover:text-white transition-colors">Office / Boardroom</a>
                        <a href="/services-retail.html"
                            class="text-base text-gray-400 hover:text-white transition-colors">Retail / Restaurants</a>
                        <a href="/services-marine.html"
                            class="text-base text-white font-medium">Marine & Powersports</a>
                        <a href="/services-car-audio.html"
                            class="text-base text-gray-400 hover:text-white transition-colors">Car Audio</a>
                    </div>
                </div>
            </nav>
        </div>
    </div>

    <script>
        // Mobile Menu Toggle
        const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileServicesToggle = document.getElementById('mobile-services-toggle');
        const mobileServicesMenu = document.getElementById('mobile-services-menu');

        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuOverlay.classList.toggle('translate-x-full');
        });

        mobileServicesToggle.addEventListener('click', () => {
            mobileServicesMenu.classList.toggle('hidden');
            mobileServicesMenu.classList.toggle('flex');
            mobileServicesToggle.querySelector('svg').classList.toggle('rotate-180');
        });
    </script>

    <!-- MAIN JS (Global logic + Scroll Effects) -->
    <script type="module" src="/main.js"></script>
</body>
</html>'''

with open('services-marine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add footer after the closing section tag
content = content.replace('<!-- FOOTER -->', footer_and_scripts)

with open('services-marine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ services-marine.html: Added footer and mobile menu")

# Step 2: Update navigation across all HTML files to link to services-marine.html instead of marine-audio.html
files_to_update = [
    'index.html', 'about.html', 'brands.html', 'car-audio.html', 'car-starters.html',
    'contact.html', 'dream-home.html', 'financing.html', 'home-audio.html',
    'marine-audio.html', 'protection-plan.html', 'services-office.html',
    'services-residential.html', 'services-retail.html', 'services-car-audio.html',
    'surveillance.html', 'team.html', 'tv-video.html'
]

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update desktop Services dropdown to link to services-marine.html
        content = re.sub(
            r'<a href="/marine-audio\.html"\s+class="block px-4 py-2 text-sm([^"]*)"[^>]*>Marine\s*&\s*Powersports</a>',
            r'<a href="/services-marine.html" class="block px-4 py-2 text-sm\1">Marine & Powersports</a>',
            content
        )
        
        # Update mobile Services accordion to link to services-marine.html
        content = re.sub(
            r'<a href="/marine-audio\.html"\s+class="text-base([^"]*)"[^>]*>Marine\s*&\s*Powersports</a>',
            r'<a href="/services-marine.html" class="text-base\1">Marine & Powersports</a>',
            content
        )
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filename}: Updated Services links to services-marine.html")
        else:
            print(f"- {filename}: No navigation changes needed")
    
    except FileNotFoundError:
        print(f"? {filename}: File not found, skipping")
    except Exception as e:
        print(f"✗ {filename}: Error - {e}")

print("\n✅ All updates complete!")
