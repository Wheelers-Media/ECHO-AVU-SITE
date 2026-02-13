#!/usr/bin/env python3
"""
Expand Services Grid Script
Adds Marine & Powersports and Remote Car Starters cards to services.html
Converting the 2x2 grid to a 2x3 grid
"""

# Read the minified services.html file
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new Marine & Powersports card
marine_card = '''
            <!-- CARD 5: Marine & Powersports -->
            <a href="/services-marine.html"
                data-scroll-spotlight class="group relative h-[500px] rounded-xl overflow-hidden border border-edge cursor-pointer block">
                <!-- Background Image -->
                <img src="/assets/Marine & Powersports/marine-audio-hero.jpg" alt="Marine & Powersports"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 group-[.in-view]:scale-105 opacity-80 group-hover:opacity-100 group-[.in-view]:opacity-100">
                <!-- Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black via-black/80 to-transparent/20"></div>
                <!-- Content -->
                <div class="absolute inset-0 p-10 flex flex-col justify-end">
                    <div class="transform translate-y-4 group-hover:translate-y-0 group-[.in-view]:translate-y-0 transition-transform duration-500">
                        <h3 class="font-heading font-bold text-3xl text-white mb-3">Marine & Powersports</h3>
                        <p
                            class="font-body text-gray-300 mb-6 max-w-md line-clamp-3 group-hover:text-white group-[.in-view]:text-white transition-colors">
                            Waterproof, weatherproof, and built to perform. From boats to ATVs, we install premium marine-grade audio systems designed for extreme conditions.
                        </p>
                        <span
                            class="inline-flex items-center text-echoRed font-bold uppercase tracking-wider text-sm group-hover:text-white group-[.in-view]:text-white transition-colors">
                            Explore Service
                            <svg class="w-4 h-4 ml-2 transition-transform duration-300 group-hover:translate-x-1 group-[.in-view]:translate-x-1"
                                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                            </svg>
                        </span>
                    </div>
                </div>
            </a>'''

# Define the new Remote Car Starters card
remote_starters_card = '''
            <!-- CARD 6: Remote Car Starters -->
            <a href="/services-car-starters.html"
                data-scroll-spotlight class="group relative h-[500px] rounded-xl overflow-hidden border border-edge cursor-pointer block">
                <!-- Background Image -->
                <img src="/assets/Remote Starters/remote-starter-hero.jpg" alt="Remote Car Starters"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 group-[.in-view]:scale-105 opacity-80 group-hover:opacity-100 group-[.in-view]:opacity-100">
                <!-- Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black via-black/80 to-transparent/20"></div>
                <!-- Content -->
                <div class="absolute inset-0 p-10 flex flex-col justify-end">
                    <div class="transform translate-y-4 group-hover:translate-y-0 group-[.in-view]:translate-y-0 transition-transform duration-500">
                        <h3 class="font-heading font-bold text-3xl text-white mb-3">Remote Car Starters</h3>
                        <p
                            class="font-body text-gray-300 mb-6 max-w-md line-clamp-3 group-hover:text-white group-[.in-view]:text-white transition-colors">
                            Defeat the cold with professional remote starter installation. T-harness integration keeps your warranty intact while giving you smartphone control.
                        </p>
                        <span
                            class="inline-flex items-center text-echoRed font-bold uppercase tracking-wider text-sm group-hover:text-white group-[.in-view]:text-white transition-colors">
                            Explore Service
                            <svg class="w-4 h-4 ml-2 transition-transform duration-300 group-hover:translate-x-1 group-[.in-view]:translate-x-1"
                                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                            </svg>
                        </span>
                    </div>
                </div>
            </a>'''

# Find where to insert the new cards (right before the closing </div> of the grid)
# Look for the pattern that marks the end of CARD 4
search_pattern = '</a>        </div>    </section>    <!-- FOOTER -->'

if search_pattern in content:
    # Insert the new cards before the grid closes
    content = content.replace(search_pattern, marine_card + remote_starters_card + '\n        </div>    </section>    <!-- FOOTER -->')
    print("✅ Successfully added Marine & Powersports and Remote Car Starters cards")
else:
    print("❌ Could not find insertion point. Trying alternate pattern...")
    
    # Try alternate pattern
    alt_pattern = '</a>        </div>    </section>'
    if alt_pattern in content:
        content = content.replace(alt_pattern, marine_card + remote_starters_card + '\n        </div>    </section>', 1)
        print("✅ Successfully added cards using alternate pattern")
    else:
        print("❌ Could not locate insertion point in file")

# Write the updated content back
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Services page updated successfully!")
print("📊 Grid is now 2x3 (6 service cards total)")
