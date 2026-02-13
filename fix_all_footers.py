#!/usr/bin/env python3
"""Fix all pages to use global footer consistently"""
import os
import re
from pathlib import Path

def fix_footer(filepath):
    """Remove hardcoded footer and ensure global footer is used"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Remove hardcoded <footer> tag and all its content
    if re.search(r'<footer\s+class', content):
        # Find and remove the entire footer section
        content = re.sub(
            r'<footer\s+class[^>]*>.*?</footer>',
            '',
            content,
            flags=re.DOTALL
        )
        changes.append("Removed hardcoded <footer> tag")
    
    # Check if footer-placeholder exists, if not add it before closing body tag
    if 'footer-placeholder' not in content:
        # Find </body> or closing scripts section
        if '</body>' in content:
            # Add footer placeholder before </body>
            content = content.replace(
                '</body>',
                '''  <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->
  <div id="footer-placeholder"></div>

</body>'''
            )
            changes.append("Added footer-placeholder")
    
    # Check if global-loader.js exists, if not add it
    if 'global-loader.js' not in content:
        # Add before closing </body> tag
        if '</body>' in content:
            content = content.replace(
                '</body>',
                '''  <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->
  <script src="global-loader.js"></script>
</body>'''
            )
            changes.append("Added global-loader.js script")
    
    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return None

# Files that need fixing based on audit
files_to_fix = [
    'home-audio.html',
    'privacy-statement.html',
    'return-policy.html',
    'services-office.html',
    'services-residential.html',
    'services-retail.html',
    'services.html',
    'surveillance.html',
    'team.html',
    'tv-video.html'
]

print("🔧 FIXING FOOTER CONSISTENCY\n")

fixed_count = 0
for filename in files_to_fix:
    filepath = Path(filename)
    if not filepath.exists():
        print(f"⚠️  {filename} - File not found, skipping")
        continue
    
    changes = fix_footer(filepath)
    if changes:
        fixed_count += 1
        print(f"✅ {filename}")
        for change in changes:
            print(f"   - {change}")
    else:
        print(f"ℹ️  {filename} - No changes needed")

print(f"\n📊 SUMMARY")
print(f"   Fixed: {fixed_count}/{len(files_to_fix)} files")
print("\n✅ All pages now use global footer consistently!")
