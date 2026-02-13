#!/usr/bin/env python3
"""Audit all HTML files for footer consistency"""
import os
import re
from pathlib import Path

def check_footer_implementation(filepath):
    """Check if a file properly uses global footer"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check 1: Has footer-placeholder
    if 'footer-placeholder' not in content:
        issues.append("Missing footer-placeholder")
    
    # Check 2: Has global-loader.js
    if 'global-loader.js' not in content:
        issues.append("Missing global-loader.js script")
    
    # Check 3: Has hardcoded <footer> tag (should not have)
    if re.search(r'<footer\s+class', content):
        issues.append("Has hardcoded <footer> tag")
    
    # Check 4: Has header-placeholder
    if 'header-placeholder' not in content:
        issues.append("Missing header-placeholder")
    
    return issues

# Find all HTML files (excluding backups, dist, node_modules)
html_files = []
exclude_patterns = ['node_modules', 'dist', '.git', 'backup', 'EXAMPLE-TEMPLATE']

for file in Path('.').rglob('*.html'):
    # Skip excluded directories
    if any(pattern in str(file) for pattern in exclude_patterns):
        continue
    html_files.append(file)

print("🔍 AUDITING FOOTER CONSISTENCY\n")
print(f"Found {len(html_files)} HTML files\n")

# Check each file
files_with_issues = []
perfect_files = []

for filepath in sorted(html_files):
    issues = check_footer_implementation(filepath)
    
    if issues:
        files_with_issues.append((filepath.name, issues))
        print(f"❌ {filepath.name}")
        for issue in issues:
            print(f"   - {issue}")
        print()
    else:
        perfect_files.append(filepath.name)

# Summary
print("\n" + "="*60)
print("📊 SUMMARY")
print("="*60)
print(f"✅ Perfect files: {len(perfect_files)}")
print(f"❌ Files with issues: {len(files_with_issues)}")

if perfect_files:
    print(f"\n✅ Files using global footer correctly ({len(perfect_files)}):")
    for name in perfect_files:
        print(f"   - {name}")

if files_with_issues:
    print(f"\n❌ Files needing fixes ({len(files_with_issues)}):")
    for name, issues in files_with_issues:
        print(f"   - {name}: {', '.join(issues)}")
