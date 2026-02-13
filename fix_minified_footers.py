#!/usr/bin/env python3
"""Remove hardcoded footers from minified HTML files"""
import re

pages_to_fix = [
    'home-audio.html',
    'services-residential.html',
    'services-office.html',
    'services-retail.html',
    'return-policy.html',
    'privacy-statement.html'
]

print("Removing hardcoded footers from minified HTML:\n")

fixed_count = 0
for page in pages_to_fix:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Find and remove the hardcoded footer
        # Look for: <footer class="...">...</footer> 
        # But handle the fact that it might be on one line with other content
        pattern = r'<footer\s+class="[^"]*">.*?</footer>'
        
        matches = list(re.finditer(pattern, content, re.DOTALL))
        
        if matches:
            print(f"📄 {page}")
            print(f"   Found {len(matches)} hardcoded footer(s)")
            
            # Remove all matches
            content = re.sub(pattern, '', content, flags=re.DOTALL)
            
            # Write back
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            
            new_length = len(content)
            removed_chars = original_length - new_length
            
            fixed_count += 1
            print(f"   ✅ Removed {removed_chars} characters")
            print(f"   Footer-placeholder still present: {'✅ Yes' if 'footer-placeholder' in content else '❌ No'}\n")
        else:
            print(f"ℹ️  {page} - No hardcoded footer pattern found\n")
            
    except FileNotFoundError:
        print(f"❌ {page} - File not found\n")
    except Exception as e:
        print(f"❌ {page} - Error: {str(e)}\n")

print(f"📊 SUMMARY")
print(f"   Fixed: {fixed_count}/{len(pages_to_fix)} pages")

if fixed_count > 0:
    print("\n✅ Hardcoded footers removed! Pages now use global footer only.")
else:
    print("\n⚠️  No changes made. Footers may already be removed or pattern didn't match.")
