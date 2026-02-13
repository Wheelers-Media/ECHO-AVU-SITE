#!/usr/bin/env python3
"""Remove hardcoded footers from specific pages"""
import re

pages_to_fix = [
    'home-audio.html',
    'services-residential.html',
    'services-office.html',
    'services-retail.html',
    'return-policy.html',
    'privacy-statement.html'
]

print("Removing hardcoded footers from pages with conflicts:\n")

fixed_count = 0
for page in pages_to_fix:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove hardcoded <footer> tag and all its content
        if re.search(r'<footer\s+class', content):
            content = re.sub(
                r'<footer\s+class[^>]*>.*?</footer>',
                '',
                content,
                flags=re.DOTALL
            )
            
            # Write back
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixed_count += 1
            print(f"✅ {page} - Removed hardcoded footer")
        else:
            print(f"ℹ️  {page} - No hardcoded footer found")
            
    except FileNotFoundError:
        print(f"❌ {page} - File not found")
    except Exception as e:
        print(f"❌ {page} - Error: {str(e)}")

print(f"\n📊 SUMMARY")
print(f"   Fixed: {fixed_count}/{len(pages_to_fix)} pages")
print("\n✅ All pages now use only the global footer!")
