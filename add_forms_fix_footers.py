import re

# Consultation form HTML for car-starters
consultation_form_starters = """
    <!-- CONSULTATION SECTION -->
    <section id="consultation" class="bg-carbon py-24 px-6 border-t border-edge">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <!-- LEFT COLUMN: Text Content -->
                <div>
                    <h2 class="font-heading font-bold text-3xl md:text-4xl text-white mb-6">
                        Ready to Start Warm?
                    </h2>
                    <p class="font-body text-gray-400 text-lg mb-10 leading-relaxed font-light">
                        Visit our Grande Prairie showroom to see our full lineup of remote start systems. We'll recommend the perfect solution for your vehicle and climate needs.
                    </p>
                    <div class="p-6 bg-edge rounded-lg border-l-4 border-echoRed">
                        <p class="text-white italic">"Best investment I've made for my truck. The 3-mile range means I can start it from my desk at work."</p>
                        <p class="text-gray-500 text-sm mt-4 font-bold">- Michael T., Grande Prairie</p>
                    </div>
                </div>
                <!-- RIGHT COLUMN: The Form -->
                <div class="w-full lg:w-1/2 bg-void p-8 md:p-10 rounded-xl border border-edge shadow-2xl">
                    <form class="space-y-6">
                        <!-- Vehicle Info -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Vehicle Type</label>
                            <div class="relative">
                                <select class="w-full bg-edge border-none rounded px-4 py-3 text-white appearance-none focus:ring-1 focus:ring-echoRed focus:outline-none">
                                    <option>Truck / SUV</option>
                                    <option>Car / Sedan</option>
                                    <option>Luxury Vehicle</option>
                                    <option>Other</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                    <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- Interests -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">I'm Interested In</label>
                            <div class="grid grid-cols-2 gap-3">
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Remote Start</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Smartphone App</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Security System</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Quote Only</span>
                                </label>
                            </div>
                        </div>
                        <!-- Contact Info -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Name</label>
                                <input type="text" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Email</label>
                                <input type="email" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Phone</label>
                                <input type="tel" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                        </div>
                        <!-- Preferred Time -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Preferred Install Time</label>
                            <div class="relative">
                                <select class="w-full bg-edge border-none rounded px-4 py-3 text-white appearance-none focus:ring-1 focus:ring-echoRed focus:outline-none">
                                    <option>Weekdays after 5pm</option>
                                    <option>Weekdays 9am - 5pm</option>
                                    <option>Saturday Morning</option>
                                    <option>Saturday Afternoon</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                    <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- Submit Button -->
                        <button type="submit" class="w-full bg-echoRed hover:bg-red-700 text-white font-bold py-4 rounded transition-transform active:scale-95 uppercase tracking-wide text-sm mt-4">
                            Book Installation
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

# Consultation form HTML for surveillance
consultation_form_surveillance = """
    <!-- CONSULTATION SECTION -->
    <section id="consultation" class="bg-carbon py-24 px-6 border-t border-edge">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <!-- LEFT COLUMN: Text Content -->
                <div>
                    <h2 class="font-heading font-bold text-3xl md:text-4xl text-white mb-6">
                        Secure Your Peace of Mind
                    </h2>
                    <p class="font-body text-gray-400 text-lg mb-10 leading-relaxed font-light">
                        Our Grande Prairie team will assess your property, recommend camera placements, and design a system that covers every critical angle.
                    </p>
                    <div class="p-6 bg-edge rounded-lg border-l-4 border-echoRed">
                        <p class="text-white italic">"The app notifications are instant. I caught someone trying my door handles and had the footage to Grande Prairie RCMP within minutes."</p>
                        <p class="text-gray-500 text-sm mt-4 font-bold">- David L., Grande Prairie</p>
                    </div>
                </div>
                <!-- RIGHT COLUMN: The Form -->
                <div class="w-full lg:w-1/2 bg-void p-8 md:p-10 rounded-xl border border-edge shadow-2xl">
                    <form class="space-y-6">
                        <!-- Property Type -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Property Type</label>
                            <div class="relative">
                                <select class="w-full bg-edge border-none rounded px-4 py-3 text-white appearance-none focus:ring-1 focus:ring-echoRed focus:outline-none">
                                    <option>Residential Home</option>
                                    <option>Commercial Business</option>
                                    <option>Multi-Unit Property</option>
                                    <option>Acreage / Rural</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                    <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- Interests -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Coverage Needed</label>
                            <div class="grid grid-cols-2 gap-3">
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Front Entrance</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Backyard</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Driveway</span>
                                </label>
                                <label class="flex items-center gap-3 bg-edge rounded px-4 py-3 cursor-pointer hover:bg-white/5 transition-colors group">
                                    <input type="checkbox" class="w-4 h-4 rounded border-gray-600 text-echoRed focus:ring-echoRed bg-gray-800">
                                    <span class="text-sm text-gray-300 group-hover:text-white">Full Perimeter</span>
                                </label>
                            </div>
                        </div>
                        <!-- Contact Info -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Name</label>
                                <input type="text" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Email</label>
                                <input type="email" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Phone</label>
                                <input type="tel" class="w-full bg-edge border-none rounded px-4 py-3 text-white placeholder-gray-600 focus:ring-1 focus:ring-echoRed focus:outline-none">
                            </div>
                        </div>
                        <!-- Preferred Time -->
                        <div>
                            <label class="block text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Preferred Consultation Time</label>
                            <div class="relative">
                                <select class="w-full bg-edge border-none rounded px-4 py-3 text-white appearance-none focus:ring-1 focus:ring-echoRed focus:outline-none">
                                    <option>Weekdays after 5pm</option>
                                    <option>Weekdays 9am - 5pm</option>
                                    <option>Saturday Morning</option>
                                    <option>Saturday Afternoon</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                                    <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                        <!-- Submit Button -->
                        <button type="submit" class="w-full bg-echoRed hover:bg-red-700 text-white font-bold py-4 rounded transition-transform active:scale-95 uppercase tracking-wide text-sm mt-4">
                            Schedule Site Assessment
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

# Update car-starters.html
print("Updating car-starters.html...")
with open('car-starters.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert consultation form before footer
content = re.sub(
    r'(\s*<!-- FOOTER -->)',
    consultation_form_starters + r'\n\1',
    content,
    count=1
)

with open('car-starters.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ Added consultation form to car-starters.html")

# Update surveillance.html - add form AND fix footer
print("\nUpdating surveillance.html...")
with open('surveillance.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the broken footer completely (from <!-- FOOTER --> to </footer>)
content = re.sub(
    r'<!-- FOOTER -->[\s\S]*?</footer>',
    '',
    content,
    count=1
)

# Insert consultation form + proper footer before mobile menu
insert_point = r'(\s*<!-- MOBILE MENU OVERLAY -->)'

# Get standard footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()
    footer_match = re.search(r'(<!-- FOOTER -->[\s\S]*?</footer>)', index_content)
    if footer_match:
        standard_footer = footer_match.group(1)
    else:
        print("ERROR: Could not find standard footer in index.html")
        exit(1)

content = re.sub(
    insert_point,
    consultation_form_surveillance + '\n\n    ' + standard_footer + '\n\n\1',
    content,
    count=1
)

with open('surveillance.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ Added consultation form to surveillance.html")
print("✓ Fixed footer on surveillance.html")

print("\n✅ All updates complete!")
