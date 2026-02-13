import re

# Read the minified team.html file
with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Create Mason Stirrett's card HTML
mason_card = '''                <!-- SPECIALIST 5: MASON -->
                <article
                    data-scroll-spotlight class="group bg-carbon border border-white/5 rounded-xl overflow-hidden hover:border-echoRed/30 [&.in-view]:border-echoRed/30 transition-colors duration-300">
                    <div class="aspect-[3/2] overflow-hidden">
                        <img src="/assets/team/mason-stirrett.jpg" alt="Mason Stirrett - Specialist"
                            class="w-full h-full object-cover transition-transform duration-700 hover:scale-105 group-[.in-view]:scale-105 filter grayscale hover:grayscale-0 group-[.in-view]:grayscale-0">
                    </div>
                    <div class="p-8">
                        <h3 class="text-2xl font-heading font-bold text-white mb-1">Mason Stirrett</h3>
                        <p class="text-echoRed font-medium mb-1">Specialist</p>
                        <p class="text-xs text-gray-500 font-bold uppercase tracking-wider mb-6">Expertise: Installation</p>
                        <p class="text-gray-400 leading-relaxed text-sm">
                            Mason brings his expertise and dedication to the Echo AVU team, continuing our tradition of exceptional service and technical excellence in the Grande Prairie community.
                        </p>
                    </div>
                </article>'''

# Find the position to insert Mason's card (before the closing </div> of the specialists grid)
# Look for the last specialist card (Jonah) and add Mason after it
pattern = r'(<!-- SPECIALIST 4: JONAH -->.*?</article>)'
replacement = r'\1' + mason_card

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added Mason Stirrett to team.html")
