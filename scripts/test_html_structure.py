"""Minimal test: validate basic HTML structure of the ApparelWebsite pages.

Run:  python test_html_structure.py
"""

import os
import sys
import re

PAGES = ["index.html", "products.html", "contact.html"]
ERRORS = []

# Title mapping: page filename -> expected <title> text
TITLE_MAP = {
    "index.html": "Home",
    "products.html": "Products",
    "contact.html": "Contact",
}

for page in PAGES:
    fpath = os.path.join("C:/Users/Parzival/Documents/ApparelWebsite", page)
    if not os.path.exists(fpath):
        ERRORS.append(f"{page} does not exist")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for CSS link
    css_links = re.findall(r'href="([^"]+\.css)"', content)
    for css in css_links:
        css_path = os.path.join("C:/Users/Parzival/Documents/ApparelWebsite", css)
        if not os.path.exists(css_path):
            ERRORS.append(f"{page}: CSS file not found: {css}")

    # Check for JS script
    js_scripts = re.findall(r'src="([^"]+\.js)"', content)
    for js in js_scripts:
        js_path = os.path.join("C:/Users/Parzival/Documents/ApparelWebsite", js)
        if not os.path.exists(js_path):
            ERRORS.append(f"{page}: JS file not found: {js}")

    # Check for image src
    img_srcs = re.findall(r'<img[^>]+src="([^"]+\.(?:jpe?g|png))"', content)
    for img in img_srcs:
        img_path = os.path.join("C:/Users/Parzival/Documents/ApparelWebsite", img)
        if not os.path.exists(img_path):
            ERRORS.append(f"{page}: Image file not found: {img}")

    # Check for required HTML structure
    page_name = TITLE_MAP.get(page, page.replace(".html", ""))
    expected_title = "Jay's Apparel - " + page_name
    title_pattern = rf"<title>{re.escape(expected_title)}</title>"
    if not re.search(title_pattern, content):
        ERRORS.append(f"{page}: Missing or incorrect title (expected: {expected_title})")
    if not re.search(r"<!DOCTYPE html>", content):
        ERRORS.append(f"{page}: Missing DOCTYPE")
    if not re.search(r"<html[^>]*>", content):
        ERRORS.append(f"{page}: Missing html tag")
    if not re.search(r"<head[^>]*>", content):
        ERRORS.append(f"{page}: Missing head tag")
    if not re.search(r"<meta charset=\"UTF-8\">", content):
        ERRORS.append(f"{page}: Missing charset meta tag")

if ERRORS:
    print("HTML Structure Test FAILED")
    for error in ERRORS:
        print(f"  - {error}")
    sys.exit(1)
else:
    print("HTML Structure Test PASSED")
    sys.exit(0)
