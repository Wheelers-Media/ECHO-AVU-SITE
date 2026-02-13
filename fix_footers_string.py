#!/usr/bin/env python3
"""Find and remove hardcoded footer using string manipulation instead of regex"""
import re

pages_to_fix = [
    'home-audio.html',
    'services-residential.html',
    'services-office.html',
    'services-retail.html',
    'return-policy.html',
    'privacy-statement.html'
]

print("Removing hardcoded footers using string search:\n")

fixed_count = 0
for page in pages_to_fix:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Find start of footer
        footer_start = content.find('<footer class=')
        
        if footer_start != -1:
            # Find the end of the footer tag
            footer_end = content.find('</footer>', footer_start)
            
            if footer_end != -1:
                footer_end += len('</footer>')
                
                # Extract what we're removing (for logging)
                removed_section = content[footer_start:footer_end]
                removed_length = len(removed_section)
                
                # Remove the footer
                content = content[:footer_start] + content[footer_end:]
                
                # Write back
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                print(f"✅ {page}")
                print(f"   Removed {removed_length} characters")
                print(f"   Footer-placeholder still present: {'✅' if 'footer-placeholder' in content else '❌'}\n")
            else:
                print(f"⚠️  {page} - Found <footer but no closing </footer>\n")
        else:
            print(f"ℹ️  {page} - No <footer tag found\n")
            
    except FileNotFoundError:
        print(f"❌ {page} - File not found\n")
    except Exception as e:
        print(f"❌ {page} - Error: {str(e)}\n")

print(f"📊 SUMMARY")
print(f"   Fixed: {fixed_count}/{len(pages_to_fix)} pages")

if fixed_count > 0:
    print("\n✅ Hardcoded footers successfully removed!")
    print("💡 Refresh your browser to see the changes")
