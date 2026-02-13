#!/usr/bin/env python3
"""Remove broken/incomplete footer HTML before footer-placeholder"""

pages_to_fix = [
    'home-audio.html',
    'services-residential.html',
    'services-office.html',
    'services-retail.html',
    'return-policy.html',
    'privacy-statement.html'
]

print("Removing broken footer HTML:\n")

fixed_count = 0
for page in pages_to_fix:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the broken footer start
        footer_start = content.find('<footer class=')
        
        # Find the footer-placeholder (this is where we want to keep content from)
        placeholder_pos = content.find('<!-- ⭐ FOOTER PLACEHOLDER')
        
        if footer_start != -1 and placeholder_pos != -1 and footer_start < placeholder_pos:
            # Remove everything from <footer to right before the placeholder comment
            removed_section = content[footer_start:placeholder_pos]
            removed_length = len(removed_section)
            
            # Keep everything before the broken footer + everything from placeholder onwards
            content = content[:footer_start] + content[placeholder_pos:]
            
            # Write back
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixed_count += 1
            print(f"✅ {page}")
            print(f"   Removed {removed_length} characters of broken HTML")
            print(f"   Footer-placeholder preserved: ✅\n")
        elif footer_start == -1:
            print(f"ℹ️  {page} - No <footer tag found\n")
        elif placeholder_pos == -1:
            print(f"⚠️  {page} - No footer-placeholder found\n")
        else:
            print(f"ℹ️  {page} - Footer is after placeholder (already correct)\n")
            
    except FileNotFoundError:
        print(f"❌ {page} - File not found\n")
    except Exception as e:
        print(f"❌ {page} - Error: {str(e)}\n")

print(f"📊 SUMMARY")
print(f"   Fixed: {fixed_count}/{len(pages_to_fix)} pages")

if fixed_count > 0:
    print("\n✅ Broken footer HTML removed successfully!")
    print("💡 Hard refresh your browser (Ctrl+Shift+R) to see the fix")
