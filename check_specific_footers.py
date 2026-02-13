#!/usr/bin/env python3
"""Check specific pages for footer issues"""
import re

pages_to_check = [
    'home-audio.html',
    'services-residential.html',
    'services-office.html',
    'services-retail.html',
    'return-policy.html',
    'privacy-statement.html'
]

print("Checking footer implementation on specific pages:\n")

for page in pages_to_check:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_placeholder = 'footer-placeholder' in content
        has_loader = 'global-loader.js' in content
        has_hardcoded = bool(re.search(r'<footer\s+class', content))
        
        print(f"📄 {page}")
        print(f"   footer-placeholder: {'✅' if has_placeholder else '❌'}")
        print(f"   global-loader.js: {'✅' if has_loader else '❌'}")
        print(f"   Hardcoded <footer>: {'❌ YES (conflict!)' if has_hardcoded else '✅ No'}")
        
        if has_hardcoded:
            print(f"   🔧 NEEDS FIX: Remove hardcoded footer")
        if not has_placeholder:
            print(f"   🔧 NEEDS FIX: Add footer-placeholder")
        if not has_loader:
            print(f"   🔧 NEEDS FIX: Add global-loader.js script")
        
        print()
    except FileNotFoundError:
        print(f"❌ {page} - File not found\n")
