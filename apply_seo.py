import os
import re
import json

def get_h1_text(filename):
    h1_map = {
        'index.html': 'Custom Technology Integration in Grande Prairie',
        'about.html': 'Four Decades of Audio Excellence in Grande Prairie',
        'brands.html': 'Premium Technology Brands in the Peace Region',
        'car-audio.html': 'Custom Car Audio & Fabrication in Grande Prairie',
        'car-starters.html': 'Remote Car Starters in Grande Prairie',
        'contact.html': "Let's Connect in Grande Prairie",
        'dream-home.html': 'Building Dreams in the Peace Region',
        'financing.html': 'Financing & Payment Plans for Grande Prairie',
        'home-audio.html': 'Whole-Home Audio in Grande Prairie',
        'marine-audio.html': 'Marine Audio Integration in the Peace Region',
        'privacy-statement.html': 'Privacy Statement',
        'protection-plan.html': 'Protection Plans in Grande Prairie',
        'return-policy.html': 'Return Policy',
        'services-car-audio.html': 'Car Audio & Remote Starters in Grande Prairie',
        'services-car-starters.html': 'Remote Car Starter Installation in Grande Prairie',
        'services-marine.html': 'Marine & Powersports Integration in the Peace Region',
        'services-office.html': 'Commercial AV & Boardroom Integration in Grande Prairie',
        'services-residential.html': 'Residential Integration in Grande Prairie',
        'services-retail.html': 'Retail AV & Digital Signage in the Peace Region',
        'services-surveillance.html': 'Surveillance & Security Systems in Grande Prairie',
        'services.html': 'Audio, Video & Installation Services in Grande Prairie',
        'team.html': 'Meet Our Expert Team in Grande Prairie',
        'tv-video.html': 'Home Theater Installations in Grande Prairie'
    }
    return h1_map.get(filename)

def get_meta_tags(filename):
    service_map = {
        'index.html': 'Custom Technology Integration',
        'about.html': 'About Our Showroom',
        'brands.html': 'Premium Technology Brands',
        'car-audio.html': 'Car Audio Fabrication',
        'car-starters.html': 'Remote Car Starters',
        'contact.html': 'Contact Us',
        'dream-home.html': 'Dream Home Tech',
        'financing.html': 'Financing Options',
        'home-audio.html': 'Whole-Home Audio',
        'marine-audio.html': 'Marine & Boat Audio',
        'privacy-statement.html': 'Privacy Policy',
        'protection-plan.html': 'Protection Plans',
        'return-policy.html': 'Return Policy',
        'services-car-audio.html': 'Car Audio Services',
        'services-car-starters.html': 'Remote Starter Services',
        'services-marine.html': 'Marine Audio Services',
        'services-office.html': 'Commercial AV Integration',
        'services-residential.html': 'Home Theater & Automation',
        'services-retail.html': 'Retail Digital Signage',
        'services-surveillance.html': 'Commercial CCTV Systems',
        'services.html': 'Custom Integration Services',
        'team.html': 'Our Expert Team',
        'tv-video.html': 'Home Theater Installations'
    }
    primary_service = service_map.get(filename, 'Custom AV Solutions')
    
    title = f"{primary_service} | Echo AVU Grande Prairie"
    if len(title) > 60:
         title = title[:56] + "..."
         
    desc = f"Looking for {primary_service.lower()}? Echo AVU delivers premium integration across the Peace Region and Grande Prairie. Contact our design experts today for a quote."
    if len(desc) > 160:
         desc = desc[:156] + "..."
         
    return title, desc

image_replace_map = {
    'subwoofers1.jpg': 'jl-audio-car-subwoofer-installation-grande-prairie.jpg',
    'subwoofers2.jpg': 'custom-car-subwoofer-enclosure-peace-region.jpg',
    'office-boardroom.jpg': 'commercial-av-boardroom-integration-peace-region.jpg',
    'remote-start-hero.jpg': 'compustar-remote-car-starter-installation-grande-prairie.jpg',
    'home-theatre.jpg': 'custom-home-theater-installation-grande-prairie.jpg',
    'cctv-camera.jpg': 'commercial-cctv-surveillance-system-peace-region.jpg',
    'factory-safe-integration.jpg': 'factory-safe-car-audio-integration-grande-prairie.jpg',
    'complete-system-upgrades.jpg': 'complete-car-audio-system-upgrade-peace-region.jpg',
    'custom-car-audio-fabrication.jpg': 'custom-car-audio-fabrication-grande-prairie.jpg',
    'marine-audio-image1 - Copy.jpg': 'marine-audio-boat-stereo-installation-grande-prairie.jpg',
    'marine-audio-hero.jpg': 'custom-marine-audio-system-peace-region.jpg',
    'smart-office-automation.jpg': 'smart-office-automation-control-4-grande-prairie.jpg',
    'distributed-video.jpg': 'commercial-distributed-video-system-peace-region.jpg',
    'distributed-video-1.jpg': 'residential-distributed-video-home-theater-grande-prairie.jpg',
    'distributed-audio.jpg': 'whole-home-distributed-audio-peace-region.jpg',
    'distributed-audio-office.jpg': 'commercial-distributed-audio-office-grande-prairie.jpg',
    'networking.jpg': 'enterprise-networking-wifi-installation-grande-prairie.jpg',
    'home-networking.jpg': 'premium-home-networking-wifi-peace-region.jpg',
    'home-security.jpg': 'luma-home-security-camera-installation-grande-prairie.jpg',
    'home-automation.jpg': 'control4-smart-home-automation-peace-region.jpg',
    'tv-mount.jpg': 'professional-tv-mounting-service-grande-prairie.jpg',
    'tv-video-image.jpg': 'home-entertainment-tv-video-installation-peace-region.jpg',
    'head-units.jpg': 'touchscreen-car-radio-head-unit-grande-prairie.jpg',
    'showroom-theater.jpg': 'echo-avu-home-theater-showroom-grande-prairie.jpg',
    'showroom-floor.jpg': 'echo-avu-technology-showroom-floor-peace-region.jpg',
    'showroom-car.jpg': 'echo-avu-custom-car-audio-bay-grande-prairie.jpg',
    'showroom-hifi.jpg': 'echo-avu-high-fidelity-audio-wall-grande-prairie.jpg',
    'DSC01747.jpg': 'echo-avu-expert-team-grande-prairie.jpg',
    'DSC03712.jpg': 'security-systems-display-showroom-peace-region.jpg',
    'DSC03918.jpg': 'drone-mobile-remote-start-smartphone-control-grande-prairie.jpg',
    'small-scale-projects.jpg': 'small-scale-residential-av-integration-grande-prairie.jpg',
    'commercial-fleet-vehicles - Copy.jpg': 'commercial-fleet-vehicle-audio-installation-peace-region.jpg',
    'f-150.jpg': 'ford-f150-custom-car-audio-grande-prairie.jpg',
    'f150-2.jpg': 'ford-f150-subwoofer-installation-peace-region.jpg',
    'f-250-custom.jpg': 'ford-f250-custom-audio-fabrication-grande-prairie.jpg',
    'can-am-x3.jpg': 'can-am-maverick-x3-powersports-audio-peace-region.jpg',
    'can-am-x3-2.jpg': 'side-by-side-marine-audio-installation-grande-prairie.jpg',
    'Guide-pour-Mettre-en-Place-un-Systeme-Domotique.jpg': 'smart-home-access-control-system-grande-prairie.jpg',
    'download.jpg': 'surveillance-security-systems-grande-prairie.jpg',
    'unnamed.jpg': 'commercial-fleet-installation-peace-region.jpg',
    'unnamed (1).jpg': 'fleet-vehicle-audio-upgrade-grande-prairie.jpg',
    'f-250-custom2.jpg': 'ford-f250-custom-audio-build-peace-region.jpg',
    'f-250-custom3.jpg': 'ford-f250-custom-fabrication-grande-prairie.jpg',
    'f-250-custom4.jpg': 'ford-f250-audio-upgrade-peace-region.jpg',
    '2024-bratt-jett - Copy.jpg': '2024-bratt-jett-marine-audio-installation-grande-prairie.jpg',
    '2024-bratt-jett (2).jpg': 'bratt-jett-boat-audio-upgrade-peace-region.jpg',
    'calibration-tech.jpg': 'audio-calibration-technician-grande-prairie.jpg',
    'calibration-tech2.jpg': 'professional-audio-calibration-peace-region.jpg',
    'dream home.jpg': 'rotary-dream-home-lottery-technology-partner-grande-prairie.jpg',
    'smart-business-automation.jpg': 'commercial-smart-business-automation-peace-region.jpg'
}

schema_json = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ElectronicsStore",
  "name": "Echo Audio Video Unlimited",
  "image": "https://echoavu.ca/Echo-Avu-White.png",
  "url": "https://echoavu.ca",
  "telephone": "780-538-1333",
  "priceRange": "$$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "11101 100 St",
    "addressLocality": "Grande Prairie",
    "addressRegion": "AB",
    "postalCode": "T8V 2N2",
    "addressCountry": "CA"
  },
  "description": "Grande Prairie's premier destination for custom car audio, remote starters, home theater integration, and commercial AV.",
  "areaServed": {
    "@type": "GeoCircle",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": 55.1708,
      "longitude": -118.8027
    },
    "geoRadius": "100000"
  },
  "serviceArea": [
    { "@type": "City", "name": "Grande Prairie" },
    { "@type": "Place", "name": "Peace Region" }
  ]
}
</script>
"""

def generate_alt(filename):
    # Generates a clean alt tag dynamically from the filename + location
    base = filename.rsplit('.', 1)[0]
    base = base.replace('-', ' ')
    
    # Capitalize appropriately
    words = base.split()
    capitalized_words = [w.capitalize() for w in words]
    alt_text = ' '.join(capitalized_words)
    
    # Ensure location is included
    if 'Grande Prairie' not in alt_text and 'Peace Region' not in alt_text:
        alt_text += " in Grande Prairie"
        
    return alt_text

directory = r'g:\Echo AVU Website Build'
assets_dir = os.path.join(directory, 'public', 'assets')

# Step 3: Physically rename files
renamed_list = []
for root, dirs, files in os.walk(assets_dir):
    for file in files:
        if file in image_replace_map:
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, image_replace_map[file])
            if os.path.exists(old_path) and not os.path.exists(new_path):
                os.rename(old_path, new_path)
                renamed_list.append(f"{file} -> {image_replace_map[file]}")

print(f"Total renamed items: {len(renamed_list)}")

html_files = [f for f in os.listdir(directory) if f.endswith('.html') and not f.endswith('.bak')]

for file in html_files:
    filepath = os.path.join(directory, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track if code changed
    original_content = str(content)

    # Step 1: Dynamic Meta Tags
    title, desc = get_meta_tags(file)
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Try replacing description if it exists
    if re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', content, flags=re.IGNORECASE):
        content = re.sub(r'<meta[^>]*name=["\']description["\'][^>]*>', f'<meta name="description" content="{desc}">', content, flags=re.IGNORECASE)
    else:
        # Inject it into head. Find line with </head> and replace 
        content = re.sub(r'</head>', f'  <meta name="description" content="{desc}">\n</head>', content, flags=re.IGNORECASE)
        
    # Step 2: H1 Tags
    new_h1 = get_h1_text(file)
    if new_h1:
        def h1_replacer(match):
            outer_open = match.group(1)
            outer_close = match.group(3)
            # Find and preserve spans, or completely replace the text but keep the tag if simple
            return f'{outer_open}{new_h1}{outer_close}'
        # Regex to capture content in H1 tags. 
        content = re.sub(r'(<h1[^>]*>)(.*?)(</h1>)', h1_replacer, content, flags=re.IGNORECASE | re.DOTALL)
        
    # Step 3: Images update (src and alt)
    def img_replacer(match):
        img_tag = match.group(0)
        
        # Replace filename
        src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, flags=re.IGNORECASE)
        if src_match:
            src = src_match.group(1)
            filename = src.split('/')[-1]
            if filename in image_replace_map:
                new_filename = image_replace_map[filename]
                img_tag = img_tag.replace(filename, new_filename)
                
                # Replace alt text
                new_alt = generate_alt(new_filename)
                if 'alt="' in img_tag or "alt='" in img_tag:
                    img_tag = re.sub(r'alt=["\'].*?["\']', f'alt="{new_alt}"', img_tag, flags=re.IGNORECASE)
                else:
                    img_tag = img_tag.replace('<img ', f'<img alt="{new_alt}" ')
            else:
                # If it's another image, just dynamically update alt context if generic
                new_alt = generate_alt(filename)
                if 'alt="' in img_tag or "alt='" in img_tag:
                    # check if current alt is empty or generic
                    current_alt_match = re.search(r'alt=["\'](.*?)["\']', img_tag, flags=re.IGNORECASE)
                    if current_alt_match:
                        current_alt = current_alt_match.group(1)
                        if not current_alt or current_alt.isspace() or len(current_alt) < 4:
                            img_tag = re.sub(r'alt=["\'].*?["\']', f'alt="{new_alt}"', img_tag, flags=re.IGNORECASE)
                        elif 'Grande Prairie' not in current_alt and 'Peace Region' not in current_alt:
                            img_tag = re.sub(r'alt=["\'].*?["\']', f'alt="{current_alt} in Grande Prairie"', img_tag, flags=re.IGNORECASE)
                        
        return img_tag

    content = re.sub(r'<img[^>]+>', img_replacer, content, flags=re.IGNORECASE)
    
    # Replace references in background-images, css inline, etc.
    for old, new in image_replace_map.items():
        # Safest is just replacing `old` with `new` where old is a complete substring like "subwoofers1.jpg".
        content = content.replace(f'/{old}', f'/{new}')
        content = content.replace(f'"{old}"', f'"{new}"')
        content = content.replace(f"'{old}'", f"'{new}'")

    # Step 4: Schema JSON-LD Injection
    if file in ['index.html', 'contact.html']:
        if 'application/ld+json' not in content:
            content = content.replace('</head>', f'{schema_json}\n</head>')
            
    # Write back to file only if changed
    if original_content != content:
        print(f"Updated HTML file: {file}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"SEO Update Completed! Renamed {len(renamed_list)} images.")
print("Renamed Images List:")
for mapping in renamed_list:
    print(mapping)
