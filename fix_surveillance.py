import re

# Read surveillance.html
with open('surveillance.html', 'r', encoding='utf-8') as f:
    surveillance_content = f.read()

# Read the proper footer from car-audio.html (lines 392-503)
with open('car-audio.html', 'r', encoding='utf-8') as f:
    car_audio_content = f.read()

# Extract footer from car-audio
footer_match = re.search(r'(\s*</section>\s*<!-- FOOTER -->.*?</footer>)', car_audio_content, re.DOTALL)
if not footer_match:
    print("ERROR: Could not find footer in car-audio.html")
    exit(1)

proper_footer = footer_match.group(1)

# Update surveillance footer link to be active
proper_footer = re.sub(
    r'(<li><a href="/surveillance\.html"[^>]*class="[^"]*)(text-gray-400 hover:text-echoRed)([^"]*")',
    r'\1text-gray-400 hover:text-echoRed\3',
    proper_footer
)

# Remove surveillance page's broken footer (from <!-- FOOTER --> to </footer>)
surveillance_content = re.sub(
    r'\s*<!-- FOOTER -->.*?</footer>',
    '',
    surveillance_content,
    flags=re.DOTALL
)

# Consultation form for surveillance
consultation_form = '''    <!-- CONSULTATION SECTION -->
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
                    </div >
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
                        <!-- Coverage Needed -->
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

'''

# Insert consultation form + proper footer before <!-- MOBILE MENU OVERLAY -->
surveillance_content = re.sub(
    r'(\s*<!-- MOBILE MENU OVERLAY -->)',
    consultation_form + proper_footer + r'\n\n\1',
    surveillance_content
)

# Write updated content
with open('surveillance.html', 'w', encoding='utf-8') as f:
    f.write(surveillance_content)

print("✅ Successfully added consultation form and fixed footer on surveillance.html!")
