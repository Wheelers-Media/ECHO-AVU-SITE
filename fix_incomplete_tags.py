"""
Fix all HTML files with incomplete closing tags
Adds mobile menu structure and proper closing tags
"""

files_to_fix = [
    'about.html',
    'car-audio.html',
    'car-starters.html',
    'contact.html',
    'dream-home.html',
    'financing.html',
    'protection-plan.html',
    'services-office.html',
    'surveillance.html',
    'team.html',
    'tv-video.html'
]

mobile_menu_template = '''
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
                        <a href="/marine-audio.html"
                            class="text-base text-gray-400 hover:text-white transition-colors">Marine & Powersports</a>
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
</body>
</html>'''

for file in files_to_fix:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file ends with incomplete <div tag
        if content.rstrip().endswith('<div'):
            # Remove the incomplete tag
            content = content.rstrip()[:-4]
            
            # Add mobile menu structure
            content += mobile_menu_template
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed {file}")
        else:
            print(f"- Skipped {file} (already complete)")
            
    except Exception as e:
        print(f"✗ Error with {file}: {e}")

print("\nAll files processed!")
