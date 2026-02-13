"""
Remove duplicate content from tv-video.html
The file has everything from nav through footer duplicated
"""

with open('tv-video.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original file: {len(lines)} lines")

# The duplication is from line 20 through line 384 (0-indexed: 19-383)
# Line 19 has: <body...> <!-- NAVBAR -->
# Line 20-69: First nav (THIS IS THE DUPLICATE)
# Line 70-324: First content (THIS IS THE DUPLICATE) 
# Line 325-384: First footer (THIS IS THE DUPLICATE)
# Line 385+: Second nav onwards (THIS IS THE CORRECT VERSION)

# We need to keep:
# - Lines 0-18 (head and beginning of body)
# - Lines 385+ (the actual content)

# Build the corrected file
corrected_lines = []

# Keep header and body tag (lines 0-18)
corrected_lines.extend(lines[0:19])

# Skip the duplicate section (lines 19-384)
# Add the actual content (lines 385+)
corrected_lines.extend(lines[385:])

print(f"Corrected file: {len(corrected_lines)} lines")
print(f"Removed {len(lines) - len(corrected_lines)} duplicate lines")

# Write the corrected file
with open('tv-video.html', 'w', encoding='utf-8') as f:
    f.writelines(corrected_lines)

print("✓ tv-video.html fixed - duplicate content removed")
