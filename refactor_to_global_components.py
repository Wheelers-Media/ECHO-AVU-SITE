import os
import re

# List of all HTML files to refactor
html_files = [
    "about.html",
    "brands.html",
    "car-audio.html",
    "car-starters.html",
    "contact.html",
    "dream-home.html",
    "financing.html",
    "home-audio.html",
    "index.html",
    "marine-audio.html",
    "privacy-statement.html",
    "protection-plan.html",
    "return-policy.html",
    "services-car-audio.html",
    "services-marine.html",
    "services-office.html",
    "services-residential.html",
    "services-retail.html",
    "services.html",
    "surveillance.html",
    "team.html",
    "tv-video.html",
]

base_path = r"G:\Echo AVU Website Build"

# Placeholder HTML
header_placeholder = '    <!-- ⭐ HEADER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="header-placeholder"></div>\n'
footer_placeholder = '    <!-- ⭐ FOOTER PLACEHOLDER - DO NOT EDIT ⭐ -->\n    <div id="footer-placeholder"></div>\n'
loader_script = '    <!-- ⭐ GLOBAL COMPONENT LOADER - REQUIRED ⭐ -->\n    <script src="global-loader.js"></script>\n'

def refactor_html_file(filepath):
    """
    Refactors an HTML file to use global components:
    1. Removes the <nav> block
    2. Removes the mobile menu overlay
    3. Removes the <footer> block
    4. Removes inline mobile menu scripts
    5. Adds placeholders
    6. Adds global-loader.js script
    """
    print(f"\n📝 Processing: {os.path.basename(filepath)}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # STEP 1: Remove the NAVBAR
        # Pattern: From <!-- NAVBAR --> to </nav>
        nav_pattern = r'(\s*)<!-- NAVBAR -->.*?</nav>\s*'
        nav_match = re.search(nav_pattern, content, re.DOTALL)
        if nav_match:
            # Get the indentation from the matched content
            indent = nav_match.group(1)
            content = re.sub(nav_pattern, indent + header_placeholder, content, count=1, flags=re.DOTALL)
            changes.append("Replaced navbar with header placeholder")
        
        # STEP 2: Remove the MOBILE MENU OVERLAY
        # Pattern: From <!-- MOBILE MENU OVERLAY --> to </div> (the closing div of the overlay)
        mobile_menu_pattern = r'\s*<!-- MOBILE MENU OVERLAY -->.*?</div>\s*</div>\s*'
        if re.search(mobile_menu_pattern, content, re.DOTALL):
            content = re.sub(mobile_menu_pattern, '\n', content, count=1, flags=re.DOTALL)
            changes.append("Removed mobile menu overlay")
        
        # STEP 3: Remove the FOOTER
        # Pattern: From <!-- FOOTER --> to </footer>
        footer_pattern = r'(\s*)<!-- FOOTER -->.*?</footer>\s*'
        footer_match = re.search(footer_pattern, content, re.DOTALL)
        if footer_match:
            indent = footer_match.group(1)
            content = re.sub(footer_pattern, indent + footer_placeholder, content, count=1, flags=re.DOTALL)
            changes.append("Replaced footer with footer placeholder")
        
        # STEP 4: Remove inline mobile menu scripts
        # Pattern: Scripts that contain mobile menu toggle logic
        inline_script_pattern = r'\s*<!-- INLINE MOBILE MENU SCRIPT -->.*?</script>\s*'
        if re.search(inline_script_pattern, content, re.DOTALL):
            content = re.sub(inline_script_pattern, '\n', content, count=1, flags=re.DOTALL)
            changes.append("Removed inline mobile menu script")
        
        # Alternative pattern for scripts without the comment
        mobile_script_pattern = r'\s*<script>\s*document\.addEventListener\([\'"]DOMContentLoaded[\'"],[^<]*mobile-menu[^<]*</script>\s*'
        if re.search(mobile_script_pattern, content, re.DOTALL):
            content = re.sub(mobile_script_pattern, '\n', content, count=1, flags=re.DOTALL)
            changes.append("Removed mobile menu toggle script")
        
        # STEP 5: Add global-loader.js script before </body>
        # Check if it already exists
        if 'global-loader.js' not in content:
            # Find the </body> tag and insert before it
            body_pattern = r'(\s*)(</body>)'
            content = re.sub(body_pattern, r'\1' + loader_script + r'\1\2', content, count=1)
            changes.append("Added global-loader.js script")
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {', '.join(changes)}")
            return True
        else:
            print(f"⚠️  No changes needed")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {str(e)}")
        return False

# Main execution
print("=" * 60)
print("🔧 GLOBAL COMPONENT REFACTORING SCRIPT")
print("=" * 60)
print(f"Base path: {base_path}")
print(f"Files to process: {len(html_files)}")

updated_count = 0
for filename in html_files:
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        if refactor_html_file(filepath):
            updated_count += 1
    else:
        print(f"\n⚠️  File not found: {filename}")

print("\n" + "=" * 60)
print(f"✨ REFACTORING COMPLETE!")
print(f"📊 Files updated: {updated_count}/{len(html_files)}")
print("=" * 60)
