#!/usr/bin/env python3
"""Remove hardcoded footer from index.html"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Fixing index.html footer...")

# The footer HTML is embedded in the minified content
# We need to remove everything from <footer to </footer> 
original_len = len(content)

# Remove the hardcoded footer tag and all its content
content = re.sub(
    r'<footer\s+class[^>]*>.*?</footer>',
    '',
    content,
    flags=re.DOTALL
)

new_len = len(content)
removed = original_len - new_len

if removed > 0:
    print(f"  ✅ Removed hardcoded footer ({removed:,} bytes)")
else:
    print("  ⚠️  No hardcoded footer found")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ index.html footer has been fixed!")
print("   Now using global footer from global-loader.js")
