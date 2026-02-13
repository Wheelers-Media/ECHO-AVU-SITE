#!/usr/bin/env python3
"""Remove hardcoded footer from index.html - aggressive approach"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Aggressively removing hardcoded footer from index.html...")
print(f"   Original size: {len(content):,} bytes")
print(f"   Has <footer tag: {'<footer' in content}")

# Find the position of <footer
footer_start = content.find('<footer')
if footer_start != -1:
    print(f"   Found <footer at position: {footer_start:,}")
    
    # Find the position of </footer> that comes after <footer
    footer_end = content.find('</footer>', footer_start)
    if footer_end != -1:
        footer_end += len('</footer>')  # Include the closing tag
        print(f"   Found </footer> at position: {footer_end:,}")
        
        # Remove everything from <footer to </footer>
        before = content[:footer_start]
        after = content[footer_end:]
        content = before + after
        
        removed_bytes = footer_end - footer_start
        print(f"   ✅ Removed {removed_bytes:,} bytes of hardcoded footer HTML")
    else:
        print("   ❌ Could not find closing </footer> tag")
else:
    print("   ✓ No <footer tag found (already clean)")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ New file size: {len(content):,} bytes")
print("   Hardcoded footer has been removed!")
