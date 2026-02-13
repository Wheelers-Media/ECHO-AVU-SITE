"""
Fix marine-audio.html Services navigation link
"""
import re

with open('marine-audio.html', 'r', encoding='utf-8') as f:
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
    with open('marine-audio.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ marine-audio.html: Updated Services links to services-marine.html")
else:
    print("- marine-audio.html: No changes needed")
