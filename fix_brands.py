#!/usr/bin/env python3
"""Fix brands.html to use global components"""
import re

with open('brands.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add header placeholder after <body>
if 'header-placeholder' not in content:
    content = re.sub(
        r'(<body[^>]*>)',
        r'\1\n    <!-- ⭐ HEADER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="header-placeholder"></div>\n',
        content
    )
    print("✅ Added header placeholder")

# Remove old footer
content = re.sub(
    r'<footer\s+class[^>]*>.*?</footer>',
    '',
    content,
    flags=re.DOTALL
)
print("✅ Removed old footer")

# Add footer placeholder
if 'footer-placeholder' not in content:
    content = content.replace(
        '</body>',
        '    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="footer-placeholder"></div>\n</body>'
    )
    print("✅ Added footer placeholder")

with open('brands.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("✅ brands.html now uses global components!")
