#!/usr/bin/env python3
"""Update index.html hero section with video and modified layout"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🎬 Updating hero section with video...")

# Find and replace the hero section
# The current hero has gradient backgrounds and heading text
# We need to replace it with:
# 1. Video background
# 2. No heading/description text  
# 3. CTA button positioned lower

old_hero = r'<!-- HERO SECTION -->.*?<section class="relative h-screen flex items-center justify-center overflow-hidden bg-void">.*?</section>'

new_hero = '''<!-- HERO SECTION -->
    <section class="relative h-screen flex items-end justify-center overflow-hidden bg-void pb-32">
      <!-- Video Background -->
      <video 
        autoplay 
        muted 
        loop 
        playsinline 
        class="absolute inset-0 w-full h-full object-cover"
      >
        <source src="/hero-video.mp4" type="video/mp4">
      </video>
      
      <!-- Dark Overlay for better button visibility -->
      <div class="absolute inset-0 bg-black/20"></div>
      
      <!-- CTA Button positioned low to avoid subtitle overlap -->
      <div class="relative z-10 text-center px-6">
        <a href="/services.html"
          class="inline-block bg-white hover:bg-gray-200 text-black font-bold py-4 px-10 rounded transition-transform active:scale-95 uppercase tracking-wide text-sm shadow-[0_0_20px_rgba(255,255,255,0.3)]">
          View Our Services
        </a>
      </div>
    </section>'''

# Replace the hero section
if '<!-- HERO SECTION -->' in content:
    content = re.sub(old_hero, new_hero, content, flags=re.DOTALL)
    print("  ✅ Replaced hero section with video background")
    print("  ✅ Removed heading and description text")
    print("  ✅ Repositioned CTA button to bottom (pb-32)")
else:
    print("  ❌ Could not find HERO SECTION comment")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Hero section updated successfully!")
print("   - Video: hero-video.mp4 as background")
print("   - Text: Removed heading and description")
print("   - CTA: Positioned low (items-end pb-32)")
