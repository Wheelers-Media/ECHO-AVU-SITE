import os
import re

search_dir = r"g:\Echo AVU Website Build"
form_files = [
    'services-car-audio.html', 'services-car-starters.html', 'services-marine.html',
    'car-audio.html', 'car-starters.html', 'marine-audio.html',
    'index.html', 'services-residential.html', 'home-audio.html', 'tv-video.html',
    'services-office.html', 'services-retail.html', 'services-surveillance.html',
    'surveillance.html', 'contact.html', 'financing.html'
]

# We will inject the new hidden inputs immediately after the access_key input
replacement = r'\1\n    <input type="hidden" name="from_name" value="Echo AVU Lead System">\n    <input type="hidden" name="System_Alert" value="New Website Consultation Request">'

for filename in form_files:
    filepath = os.path.join(search_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content
    # Find the access key input, capture it in group 1, and append the new inputs
    content = re.sub(r'(<input type="hidden" name="access_key" value="406fd432-5017-4119-8ed0-3bed3ab84800">)', replacement, content)
    
    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
