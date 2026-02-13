"""
Punch List Fixes Script
Handles: Marine hero crop, SI brand swap, text removals, navigation updates
"""
import re

###############################################################################
# 1. FIX MARINE HERO IMAGE - Add object-bottom class
###############################################################################
def fix_marine_hero():
    file_path = "marine-audio.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the hero background image div and add object-bottom class
    old_pattern = r'class="absolute inset-0 bg-\[url\(\'/assets/marine-audio/marine-audio-hero\.jpg\'\)\] bg-cover bg-center opacity-60"'
    new_replacement = 'class="absolute inset-0 bg-[url(\'/assets/marine-audio/marine-audio-hero.jpg\')] bg-cover bg-center bg-bottom opacity-60"'
    
    content = content.replace(old_pattern, new_replacement)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Fixed {file_path} - Added bg-bottom to hero image")

###############################################################################
# 2. SWAP SI BRAND - Replace Screen Innovations with Stewart Filmscreen
###############################################################################
def swap_si_brand():
    file_path = "tv-video.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Screen Innovations logo
    old_si = '''<!-- Screen Innovations --> <img
                    src="/assets/brands/ScreenInnovations.png" alt="Screen Innovations"
                    class="h-8 md:h-10 w-auto object-contain brightness-0 invert">'''
    
    new_stewart = '''<!-- Stewart Filmscreen --> <img
                    src="/assets/brands/stewart.png" alt="Stewart Filmscreen"
                    class="h-8 md:h-10 w-auto object-contain brightness-0 invert">'''
    
    content = content.replace(old_si, new_stewart)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Fixed {file_path} - Swapped SI for Stewart Filmscreen")

###############################################################################
# 3. REMOVE "TURNTABLE CALIBRATION" CARD from home-audio.html
###############################################################################
def remove_turntable_card():
    file_path = "home-audio.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and remove the entire Turntable Calibration card
    pattern = r'<!-- Card 3 -->.*?<div\s+data-scroll-spotlight\s+class="group[^"]*">.*?<h3[^>]*>Turntable Calibration</h3>.*?</div>\s*</div>\s*</div>'
    
    # More precise pattern
    start_marker = '<h3 class="font-heading font-bold text-2xl text-white mb-4">Turntable Calibration</h3>'
    
    # Find the card containing Turntable Calibration
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print(f"! Turntable Calibration not found in {file_path}")
        return
    
    # Backtrack to find the opening div with data-scroll-spotlight
    card_start = content.rfind('<div', 0, start_pos)
    card_start = content.rfind('<div', 0, card_start)  # Back one more to get the main card div
    
    # Find the closing </div> for this card
    depth = 1
    pos = content.find('<div', card_start + 4)
    while depth > 0 and pos < len(content):
        next_open = content.find('<div', pos)
        next_close = content.find('</div>', pos)
        
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + 6
            if depth == 0:
                card_end = pos
                break
    
    # Remove the card
    content = content[:card_start] + content[card_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Fixed {file_path} - Removed Turntable Calibration card")

###############################################################################  
# 4. REMOVE "LIFETIME SUPPORT" GLOBALLY
###############################################################################
def remove_lifetime_support():
    # Main occurrence is in index.html in the "Echo Process" section
    files_to_check = ['index.html', 'about.html', 'temp_menu.txt']
    
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Replace "Lifetime Support" with "Local Support"
            content = content.replace('Lifetime Support', 'Local Support')
            content = content.replace('lifetime support', 'local support')
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Fixed {file_path} - Replaced 'Lifetime Support' with 'Local Support'")
        except FileNotFoundError:
            print(f"- Skipped {file_path} (not found)")

###############################################################################
# 5. UPDATE NAVIGATION - Add "Marine & Powersports" to Services dropdown
###############################################################################
def update_navigation():
    # Files with Services dropdown navigation
    nav_files = [
        'index.html',
        'home-audio.html', 
        'services-residential.html',
        'car-audio.html',
        'tv-video.html',
        'marine-audio.html',
        'surveillance.html',
        'car-starters.html',
        'brands.html',
        'about.html',
        'team.html',
        'contact.html',
        'financing.html'
    ]
    
    for file_path in nav_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if Marine & Powersports already in Services dropdown
            if '/services-marine.html' in content or 'Marine &amp; Powersports' in content:
                continue
            
            # Find the Services dropdown and add Marine & Powersports
            # Look for the pattern with "Car Audio" link in Services dropdown
            services_pattern = r'(<a href="/services-car-audio\.html"[^>]*>Car\s*Audio</a>)'
            
            new_link = r'''  <a href="/marine-audio.html"
                                class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors">Marine
                                & Powersports</a>
                            \1'''
            
            content = re.sub(services_pattern, new_link, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed {file_path} - Added Marine & Powersports to Services dropdown")
        except FileNotFoundError:
            print(f"- Skipped {file_path} (not found)")

###############################################################################
# MAIN EXECUTION
###############################################################################
if __name__ == "__main__":
    print("=" * 60)
    print("PUNCH LIST FIXES")
    print("=" * 60)
    
    fix_marine_hero()
    swap_si_brand()
    remove_turntable_card()
    remove_lifetime_support()
    update_navigation()
    
    print("=" * 60)
    print("ALL FIXES COMPLETE!")
    print("=" * 60)
