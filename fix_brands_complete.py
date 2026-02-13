#!/usr/bin/env python3
"""Fix brands.html completely - add header, footer placeholders and script tag"""
import re

with open('brands.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Fixing brands.html...")

# 1. Add header placeholder if missing
if 'header-placeholder' not in content:
    content = re.sub(
        r'(<body[^>]*>)',
        r'\1\n    <!-- ⭐ HEADER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="header-placeholder"></div>\n',
        content
    )
    print("  ✅ Added header placeholder")
else:
    print("  ✓ Header placeholder already exists")

# 2. Remove old footer if present
old_footer_removed = False
if '<footer' in content:
    original_len = len(content)
    content = re.sub(
        r'<footer\s+class[^>]*>.*?</footer>',
        '',
        content,
        flags=re.DOTALL
    )
    if len(content) < original_len:
        old_footer_removed = True
        print("  ✅ Removed old footer")

# 3. Add footer placeholder if missing
if 'footer-placeholder' not in content:
    # Insert before the closing </body> tag
    content = content.replace(
        '</body>',
        '    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="footer-placeholder"></div>\n</body>'
    )
    print("  ✅ Added footer placeholder")
else:
    print("  ✓ Footer placeholder already exists")

# 4. Add global-loader.js script if missing
if 'global-loader.js' not in content:
    # Add before </body>
    content = content.replace(
        '</body>',
        '    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->\n    <script src="global-loader.js"></script>\n</body>'
    )
    print("  ✅ Added global-loader.js script")
else:
    print("  ✓ global-loader.js script already exists")

with open('brands.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("\n✅ brands.html is now fully updated with global components!")
