#!/usr/bin/env python3
"""
Check which HTML files are NOT using global components
"""

import os

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('.bak')]

files_without_global = []
files_with_global = []

for html_file in sorted(html_files):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if the file has global component placeholders
    has_placeholder = 'header-placeholder' in content and 'footer-placeholder' in content
    has_global_loader = 'global-loader.js' in content
    
    if has_placeholder and has_global_loader:
        files_with_global.append(html_file)
    else:
        files_without_global.append(html_file)

print("✅ FILES WITH GLOBAL COMPONENTS:")
for f in files_with_global:
    print(f"  - {f}")

print(f"\n❌ FILES WITHOUT GLOBAL COMPONENTS ({len(files_without_global)}):")
for f in files_without_global:
    print(f"  - {f}")

print(f"\n📊 SUMMARY:")
print(f"  Total HTML files: {len(html_files)}")
print(f"  Using global components: {len(files_with_global)}")
print(f"  Need updating: {len(files_without_global)}")
