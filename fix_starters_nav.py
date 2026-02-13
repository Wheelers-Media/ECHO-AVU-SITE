import os
import re

files_to_update = [
    'about.html', 'brands.html', 'car-audio.html', 'contact.html',
    'financing.html', 'home-audio.html', 'index.html', 'marine-audio.html',
    'privacy-statement.html', 'protection-plan.html', 'return-policy.html',
    'services-car-audio.html', 'services-office.html', 'services-residential.html',
    'services-retail.html', 'services.html', 'surveillance.html', 'team.html',
    'tv-video.html', 'car-starters.html'
]

def clean_and_update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # First, remove ALL existing car-starters links (to clean up duplicates)
        content = re.sub(r'\s*<a href="/car-starters\.html"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
        
        # Determine if this is the car-starters page itself
        is_starters_page = 'car-starters.html' in filepath
        
        # 1. INSERT DESKTOP LINK: After Car Audio in header navigation
        if is_starters_page:
            desktop_link = '\n                <a href="/car-starters.html"\n                    class="text-sm font-medium text-echoRed transition-colors duration-300">Remote Starters</a>'
        else:
            desktop_link = '\n                <a href="/car-starters.html"\n                    class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Remote Starters</a>'
        
        # Find Car Audio link in desktop nav and insert after it
        car_audio_desktop = r'(<a href="/car-audio\.html"\s+class="text-sm[^"]*"[^>]*>Car\s+Audio</a>)'
        if re.search(car_audio_desktop, content):
            content = re.sub(car_audio_desktop, r'\1' + desktop_link, content, count=1)
        
        # 2. INSERT FOOTER LINK: In the Departments column footer
        if is_starters_page:
            footer_link = '\n              <li><a href="/car-starters.html" class="text-gray-400 hover:text-echoRed transition-colors duration-200">Remote Starters</a></li>'
        else:
            footer_link = '\n              <li><a href="/car-starters.html" class="text-gray-400 hover:text-echoRed transition-colors duration-200">Remote Starters</a></li>'
        
        # Find the car audio footer link pattern
        footer_car_audio = r'(<li><a href="/car-audio\.html"[^>]*>[\s\S]*?Car Audio[^<]*</a></li>)'
        if re.search(footer_car_audio, content):
            content = re.sub(footer_car_audio, r'\1' + footer_link, content, count=1)
        
        # 3. INSERT MOBILE MENU LINK: In mobile accordion after Car Audio
        if is_starters_page:
            mobile_link = '\n                    <a href="/car-starters.html" class="block text-echoRed font-bold hover:text-white transition-colors py-1">Remote Starters</a>'
        else:
            mobile_link = '\n                    <a href="/car-starters.html" class="block text-gray-400 hover:text-white transition-colors py-1">Remote Starters</a>'
        
        # Find mobile car audio link pattern  
        mobile_car_audio = r'(<a href="/car-audio\.html"\s+class="block[^"]*"[^>]*>Car\s+Audio[^<]*</a>)'
        if re.search(mobile_car_audio, content):
            content = re.sub(mobile_car_audio, r'\1' + mobile_link, content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed {filepath}")

    except Exception as e:
        print(f"✗ Error updating {filepath}: {e}")

for file in files_to_update:
    if os.path.exists(file):
        clean_and_update_file(file)
    else:
        print(f"✗ File not found: {file}")

print("\n✅ All files updated successfully!")
