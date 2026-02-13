import re

# Read the minified file
with open('home-audio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Elipson with the new brands
# Find the Elipson img tag and replace it with Wiim, Polk Audio, and SVS
content = re.sub(
    r'<img src="/assets/brands/elipson\.png" alt="Elipson" class="h-10 md:h-12 w-auto object-contain">',
    '<img src="/assets/brands/wiim.png" alt="Wiim" class="h-10 md:h-12 w-auto object-contain">'
    '<img src="/assets/brands/Polk_Audio_logo.png" alt="Polk Audio" class="h-10 md:h-12 w-auto object-contain">'
    '<img src="/assets/brands/svs.png" alt="SVS" class="h-10 md:h-12 w-auto object-contain">',
    content
)

# Write back
with open('home-audio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated home-audio.html brands")
