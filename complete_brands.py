#!/usr/bin/env python3
"""Complete brands.html by appending missing footer and closing tags"""

# Read current content
with open('brands.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Content to append after the closing </script> tag
missing_content = """
    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->
    <div id="footer-placeholder"></div>

    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->
    <script src="global-loader.js"></script>
</body>
</html>"""

# Append the missing content
complete_content = content + missing_content

# Write back
with open('brands.html', 'w', encoding='utf-8') as f:
    f.write(complete_content)

print("✅ brands.html is now complete!")
print("   - Added footer placeholder")
print("   - Added global-loader.js script")
print("   - Added closing </body> and </html> tags")
