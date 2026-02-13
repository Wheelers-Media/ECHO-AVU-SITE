#!/usr/bin/env python3
"""Rebuild index.html footer section - remove everything from <footer onwards and rebuild"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Rebuilding index.html footer section...")
print(f"   Original size: {len(content):,} bytes")

# Find where <footer starts
footer_pos = content.find('<footer')

if footer_pos != -1:
    print(f"   Found malformed footer at position: {footer_pos:,}")
    
    # Keep everything BEFORE the footer tag
    content = content[:footer_pos]
    
    # Add the proper footer structure
    proper_ending = """
    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->
    <div id="footer-placeholder"></div>

    <!-- MAIN JS (Global logic + Scroll Effects) -->
    <script type="module" src="/main.js"></script>
    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->
    <script src="global-loader.js"></script>
</body>
</html>"""
    
    content += proper_ending
    
    print("   ✅ Removed malformed footer")
    print("   ✅ Added proper footer-placeholder")
    print("   ✅ Added proper closing tags")
else:
    print("   ✓ No <footer tag found")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ New file size: {len(content):,} bytes")
print("   index.html footer has been properly rebuilt!")
