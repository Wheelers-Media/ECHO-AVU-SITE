import os
import re

# List of HTML files to update (exclude dream-home.html itself, if needed)
html_files = [
    "about.html",
    "brands.html",
    "car-audio.html",
    "car-starters.html",
    "contact.html",
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

dream_home_link = '''                        <li><a href="/dream-home.html"
                                class="text-gray-400 hover:text-echoRed transition-colors duration-200">Rotary Dream
                                Home</a>
                        </li>'''

dream_home_link_mobile = '''                    <a href="/dream-home.html"
                        class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">Rotary
                        Dream Home</a>'''

for filename in html_files:
    filepath = os.path.join("G:\\Echo AVU Website Build", filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # CHANGE 1: Footer - Column 5 (Visit Us)
    # Look for the pattern: About Echo AVU link, then we insert the Dream Home link, then Contact Support
    footer_pattern = re.compile(
        r'(<li><a href="/about\.html"[^>]*>About Echo\s+AVU</a>\s*</li>)',
        re.DOTALL
    )
    
    if footer_pattern.search(content):
        # Insert Dream Home link after "About Echo AVU"
        content = footer_pattern.sub(r'\1\n' + dream_home_link, content)
        changes_made.append("Footer Column 5")
    
    # CHANGE 2: Mobile Menu - Bottom Section (Visit Us)
    # Look for pattern: About Echo AVU link in mobile menu, then insert Dream Home, then Contact Support
    mobile_pattern = re.compile(
        r'(<a href="/about\.html"\s+class="block text-xl font-heading font-bold text-white hover:text-echoRed transition-colors">About\s+Echo AVU</a>)',
        re.DOTALL
    )
    
    if mobile_pattern.search(content):
        # Insert Dream Home link after "About Echo AVU" in mobile menu
        content = mobile_pattern.sub(r'\1\n' + dream_home_link_mobile, content)
        changes_made.append("Mobile Menu")
    
    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {filename} - Added link to: {', '.join(changes_made)}")
    else:
        print(f"⚠️  {filename} - No matching patterns found (might already have the link or different structure)")

print("\n✨ Script complete! All files have been processed.")
