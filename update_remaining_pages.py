#!/usr/bin/env python3
"""
Update remaining HTML files to use global components
This script will:
1. Find and remove old header/footer HTML
2. Add header-placeholder and footer-placeholder divs
3. Add global-loader.js script tag
"""

import re
import os

# Files that need updating (from the check script)
files_to_update = [
    'brands.html',
    'home-audio.html',
    'index.html',
    'privacy-statement.html',
    'protection-plan.html',
    'return-policy.html',
    'services-marine.html',
    'services-office.html',
    'services-residential.html',
    'services-retail.html',
    'services.html',
    'team.html'
]

def update_html_file(filename):
    """Update a single HTML file to use global components"""
    
    print(f"\n📝 Processing: {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_length = len(content)
    
    # Pattern 1: Remove old <nav> block (everything from <nav to </nav>)
    # This handles both single-line and multi-line nav tags
    content = re.sub(
        r'<nav\s+class[^>]*>.*?</nav>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Remove mobile menu overlay div
    content = re.sub(
        r'<div\s+id="mobile-menu-overlay"[^>]*>.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 3: Remove old footer (everything from <footer to </footer>)
    content = re.sub(
        r'<footer\s+class[^>]*>.*?</footer>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Step 2: Add header placeholder right after <body> tag
    if '<div id="header-placeholder"></div>' not in content:
        content = re.sub(
            r'(<body[^>]*>)',
            r'\1\n    <!-- ⭐ HEADER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="header-placeholder"></div>\n',
            content
        )
        print("  ✅ Added header placeholder")
    
    # Step 3: Add footer placeholder before closing </body> tag
    if '<div id="footer-placeholder"></div>' not in content:
        # Find where to insert footer placeholder (before main.js or before </body>)
        footer_placeholder = '    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="footer-placeholder"></div>\n'
        
        if '<script type="module" src="/main.js"></script>' in content:
            # Insert before main.js
            content = content.replace(
                '<script type="module" src="/main.js"></script>',
                footer_placeholder + '    <!-- MAIN JS (Global logic + Scroll Effects) -->\n    <script type="module" src="/main.js"></script>'
            )
        else:
            # Insert before </body>
            content = content.replace(
                '</body>',
                footer_placeholder + '</body>'
            )
        print("  ✅ Added footer placeholder")
    
    # Step 4: Add global-loader.js script if not present
    if 'global-loader.js' not in content:
        # Add before </body>
        content = content.replace(
            '</body>',
            '    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->\n    <script src="global-loader.js"></script>\n</body>'
        )
        print("  ✅ Added global-loader.js script")
    
    # Write the updated content back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_length = len(content)
    reduction = original_length - new_length
    print(f"  📊 File size: {original_length:,} → {new_length:,} bytes (reduced by {reduction:,} bytes)")
    
    return True

# Main execution
print("🚀 Starting global component migration for 12 files...\n")
print("=" * 60)

success_count = 0
error_count = 0

for filename in files_to_update:
    try:
        if os.path.exists(filename):
            update_html_file(filename)
            success_count += 1
        else:
            print(f"\n⚠️  File not found: {filename}")
            error_count += 1
    except Exception as e:
        print(f"\n❌ Error processing {filename}: {str(e)}")
        error_count += 1

print("\n" + "=" * 60)
print(f"\n✅ MIGRATION COMPLETE!")
print(f"   Successfully updated: {success_count} files")
if error_count > 0:
    print(f"   Errors: {error_count} files")

print(f"\n📋 All {success_count} files now use global header and footer!")
print("   - Header: <div id=\"header-placeholder\"></div>")
print("   - Footer: <div id=\"footer-placeholder\"></div>")
print("   - Loader: global-loader.js")
