#!/usr/bin/env python3
"""Replace hardcoded header and footer with global components in index.html"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Converting index.html to use global components...")

# 1. Remove hardcoded <nav> tag
if '<nav' in content:
    content = re.sub(
        r'<nav\s+class[^>]*>.*?</nav>',
        '',
        content,
        flags=re.DOTALL
    )
    print("  ✅ Removed hardcoded <nav>")

# 2. Remove hardcoded <footer> tag  
if '<footer' in content:
    content = re.sub(
        r'<footer\s+class[^>]*>.*?</footer>',
        '',
        content,
        flags=re.DOTALL
    )
    print("  ✅ Removed hardcoded <footer>")

# 3. Remove mobile menu overlay
if 'mobile-menu-overlay' in content:
    content = re.sub(
        r'<!-- MOBILE MENU OVERLAY.*?<!-- INLINE MOBILE MENU SCRIPT -->.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )
    print("  ✅ Removed mobile menu overlay")

# 4. Add header placeholder after <div id="app">
if 'header-placeholder' not in content:
    content = content.replace(
        '<div id="app">',
        '''<div id="app">
    <!-- ⭐ HEADER PLACEHOLDER - DO NOT EDIT ⭐ -->
    <div id="header-placeholder"></div>'''
    )
    print("  ✅ Added header placeholder")

# 5. Add footer placeholder before closing scripts
if 'footer-placeholder' not in content:
    # Find the main.js script and add footer placeholder before it
    content = content.replace(
        '<!-- MAIN JS (Global logic + Scroll Effects) -->',
        '''<!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->
    <div id="footer-placeholder"></div>

    <!-- MAIN JS (Global logic + Scroll Effects) -->'''
    )
    print("  ✅ Added footer placeholder")

# 6. Add global-loader.js script if missing
if 'global-loader.js' not in content:
    content = content.replace(
        '<script type="module" src="/main.js"></script>',
        '''<script type="module" src="/main.js"></script>
    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->
    <script src="global-loader.js"></script>'''
    )
    print("  ✅ Added global-loader.js script")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ index.html now uses global components!")
print("   - Header from global-loader.js")
print("   - Footer from global-loader.js")
print("   - Mobile menu from global-loader.js")
