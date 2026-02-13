"""
Simplified navigation update script
"""
import os

# Simple function to safely update nav files
def update_nav_files():
    nav_files = [
        'car-audio.html',
        'tv-video.html', 
        'marine-audio.html',
        'surveillance.html',
        'car-starters.html',
        'brands.html',
        'about.html',
        'team.html',
        'contact.html',
        'financing.html',
        'services-office.html',
        'services-retail.html'
    ]
    
    marine_link = '''<a href="/marine-audio.html"
                                class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Marine
                                & Powersports</a>
                            '''
    
    for file_path in nav_files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Skip if already has marine link in services dropdown
            if'services-marine' in content or 'Marine &amp; Powersports</a>' in content:
                continue
            
            # Find Car Audio link in Services dropdown and add Marine before it
            car_audio_pattern = '<a href="/services-car-audio.html"'
            
            if car_audio_pattern in content:
                new_content = content.replace(car_audio_pattern, marine_link + '\n                            ' + car_audio_pattern)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Updated {file_path}")
        except Exception as e:
            print(f"! Error with {file_path}: {e}")

if __name__ == "__main__":
    print("Updating Navigation...")
    update_nav_files()
    print("Done!")
