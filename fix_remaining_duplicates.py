"""
Fix duplication in marine-audio.html and protection-plan.html
"""

def fix_duplicates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find where the duplication starts
    # Look for the second occurrence of </nav>
    nav_closes = []
    pos = 0
    while True:
        pos = content.find('</nav>', pos)
        if pos == -1:
            break
        nav_closes.append(pos)
        pos += 6
    
    if len(nav_closes) < 2:
        print(f"- {filename}: No duplication found")
        return
    
    # The first </nav> is part of the duplicate
    # The second </nav> starts the correct content
    # We need to remove everything from just after <body> to just before the second <nav
    
    body_start = content.find('<body')
    body_tag_end = content.find('>', body_start) + 1
    
    # Find the start of the second nav (should be right after first </nav>)
    second_nav_start = content.find('<nav', nav_closes[0])
    
    if body_tag_end == -1 or second_nav_start == -1:
        print(f"! {filename}: Could not locate markers")
        return
    
    # Calculate what to remove
    remove_start = body_tag_end
    remove_end = second_nav_start
    removed_length = remove_end - remove_start
    
    # Build corrected content
    corrected = content[:remove_start] + content[remove_end:]
    
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(corrected)
    
    print(f"✓ {filename}: Removed {removed_length} characters of duplicate content")

# Fix both files
fix_duplicates('marine-audio.html')
fix_duplicates('protection-plan.html')

print("\nAll duplications fixed!")
