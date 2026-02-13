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

# Desktop nav link (insert after Car Audio)
starters_link_desktop = '\n                <a href="/car-starters.html"\n                    class="text-sm font-medium text-gray-400 hover:text-white transition-colors duration-300">Remote Starters</a>'

# Mobile menu link (insert after Car Audio & Starters in footer)
starters_link_mobile = '\n                    <a href="/car-starters.html" class="block text-gray-400 hover:text-white transition-colors py-1">Remote Starters</a>'

# For car-starters.html itself, use active state
starters_link_desktop_active = '\n                <a href="/car-starters.html"\n                    class="text-sm font-medium text-echoRed transition-colors duration-300">Remote Starters</a>'
starters_link_mobile_active = '\n                    <a href="/car-starters.html" class="block text-echoRed font-bold hover:text-white transition-colors py-1">Remote Starters</a>'


def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine which links to use
        if 'car-starters.html' in filepath:
            desktop_insert = starters_link_desktop_active
            mobile_insert = starters_link_mobile_active
        else:
            desktop_insert = starters_link_desktop
            mobile_insert = starters_link_mobile

        # 1. Insert Desktop Link: After Car Audio link in header
        # Look for the Car Audio link pattern
        car_audio_pattern = r'(<a href="/car-audio\.html"[^>]*>[\s\S]*?Car\s+Audio</a>)'
        
        if re.search(car_audio_pattern, content):
            # Check if starters link already exists
            if '/car-starters.html' not in content or 'car-starters.html' in filepath:
                content = re.sub(car_audio_pattern, r'\1' + desktop_insert, content, count=1)
        
        # 2. Insert Mobile Link: After "Car Audio & Starters" text in footer
        # The footer has "Car Audio & Starters" text, we need to add link after it
        footer_car_audio_pattern = r'(Car Audio \u0026[\s\S]*?Starters</a>)'
        
        if re.search(footer_car_audio_pattern, content):
            # Only add if not already there
            if content.count('/car-starters.html') < 3:  # Desktop + Footer + Mobile
                content = re.sub(footer_car_audio_pattern, r'\1' + mobile_insert, content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

    except Exception as e:
        print(f"Error updating {filepath}: {e}")

for file in files_to_update:
    if os.path.exists(file):
        update_file(file)
    else:
        print(f"File not found: {file}")
