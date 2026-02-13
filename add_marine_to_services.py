"""
Add Marine & Powersports link to ALL Services dropdowns (desktop + mobile)
"""
import re
import os

files_to_update = [
    'about.html', 'brands.html', 'car-audio.html', 'car-starters.html',
    'contact.html', 'dream-home.html', 'financing.html', 'home-audio.html',
    'index.html', 'marine-audio.html', 'protection-plan.html', 
    'services-office.html', 'services-residential.html', 'services-retail.html',
    'services-car-audio.html', 'surveillance.html', 'team.html', 'tv-video.html',
    'return-policy.html', 'privacy-statement.html'
]

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"? {filename}: File not found, skipping")
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # DESKTOP: Add Marine & Powersports link after Retail / Restaurants
        # Pattern: Find the Services dropdown menu and add the link before Car Audio or after last item
        desktop_pattern = r'(<a href="/services-retail\.html"[^>]*>Retail\s*/\s*Restaurants</a>)'
        desktop_replacement = r'\1\n                                <a href="/services-marine.html" class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Marine & Powersports</a>'
        
        if re.search(desktop_pattern, content):
            content = re.sub(desktop_pattern, desktop_replacement, content)
            changes_made.append("desktop dropdown")
        
        # MOBILE: Add Marine & Powersports link after Retail / Restaurants in mobile accordion
        mobile_pattern = r'(<a href="/services-retail\.html"\s+class="block text-gray-400[^"]*"[^>]*>Retail\s*&\s*Hospitality</a>)'
        mobile_replacement = r'\1\n                    <a href="/services-marine.html" class="block text-gray-400 hover:text-white transition-colors py-1">Marine & Powersports</a>'
        
        if re.search(mobile_pattern, content):
            content = re.sub(mobile_pattern, mobile_replacement, content)
            changes_made.append("mobile accordion")
        
        # FOOTER: Add to Services column in footer
        footer_pattern = r'(<a href="/services-retail\.html"\s+class="block text-gray-400[^"]*"[^>]*>Retail\s*&\s*Hospitality</a>)'
        footer_replacement = r'\1\n                        <a href="/services-marine.html" class="block text-gray-400 hover:text-white transition-colors py-1">Marine & Powersports</a>'
        
        if re.search(footer_pattern, content) and "mobile accordion" not in changes_made:
            content = re.sub(footer_pattern, footer_replacement, content)
            changes_made.append("footer")
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filename}: Added Marine & Powersports to {', '.join(changes_made)}")
        else:
            print(f"- {filename}: No Services dropdown found or already has Marine link")
    
    except Exception as e:
        print(f"✗ {filename}: Error - {e}")

print("\n✅ All files processed!")
