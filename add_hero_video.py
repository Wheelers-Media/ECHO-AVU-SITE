#!/usr/bin/env python3
"""Add video tag to hero section in minified index.html"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🎬 Adding video tag to hero section...")

# Find the hero section opening tag
hero_marker = '<!-- HERO SECTION -->'
if hero_marker in content:
    # Find the section tag that follows
    section_start = content.find('<section class="relative h-screen', content.find(hero_marker))
    
    if section_start != -1:
        # Find the end of the opening section tag
        section_tag_end = content.find('>', section_start) + 1
        
        # Insert the video tag right after the opening <section> tag
        video_html = '''
      <!-- Video Background -->
      <video 
        autoplay 
        muted 
        loop 
        playsinline 
        class="absolute inset-0 w-full h-full object-cover"
      >
        <source src="/assets/hero-video.mp4" type="video/mp4">
      </video>
      
      <!-- Dark Overlay -->
      <div class="absolute inset-0 bg-black/20"></div>
'''
        
        # Insert the video HTML
        content = content[:section_tag_end] + video_html + content[section_tag_end:]
        
        print("  ✅ Added video tag to hero section")
        print("  ✅ Video path: /assets/hero-video.mp4")
        print("  ✅ Added dark overlay for better CTA visibility")
    else:
        print("  ❌ Could not find hero section tag")
else:
    print("  ❌ Could not find HERO SECTION marker")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Hero video added successfully!")
