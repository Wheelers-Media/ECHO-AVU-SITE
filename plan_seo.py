import os
import json
import re

def process_html_files(directory):
    html_files = [f for f in os.listdir(directory) if f.endswith('.html') and not f.endswith('.bak')]
    
    report = {}
    images = set()

    for file in html_files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else None
        
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else None
        
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else None
        
        page_images = []
        img_matches = re.finditer(r'<img\s+([^>]+)>', content, re.IGNORECASE)
        for d_match in img_matches:
            img_attrs = d_match.group(1)
            src_match = re.search(r'src=["\'](.*?)["\']', img_attrs, re.IGNORECASE)
            alt_match = re.search(r'alt=["\'](.*?)["\']', img_attrs, re.IGNORECASE)
            
            src = src_match.group(1) if src_match else None
            alt = alt_match.group(1) if alt_match else ''
            
            if src:
                page_images.append({'src': src, 'alt': alt})
                if 'assets/' in src:
                    images.add(src.split('/')[-1])
                elif '/' not in src and '.' in src:
                    images.add(src)
                
        report[file] = {
            'title': title,
            'description': description,
            'h1': h1,
            'images': page_images
        }
        
    return {
        'files': report,
        'unique_local_images': list(images)
    }

if __name__ == '__main__':
    directory = r'g:\Echo AVU Website Build'
    report = process_html_files(directory)
    with open('seo_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    print("Report generated at seo_report.json")
