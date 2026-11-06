#!/c/Users/Parzival/AppData/Local/hermes/installs/cbe413068798fabd/environments/d2e20692300342989991d6097a2c826a/venv/Scripts/python
"""Minimal test: validate basic HTML structure of the ApparelWebsite pages.

Run:  python test_html_structure.py
"""
import os
import sys

PAGES = ["index.html", "products.html", "contact.html"]
ERRORS = []

for page in PAGES:
    fpath = os.path.join("C:/Users/Parzival/Documents/ApparelWebsite", page)
    if not os.path.exists(fpath):
        ERRORS.append(f"{page}: file not found")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Basic structural checks
    checks = {
        "doctype": "<!DOCTYPE html>" in content,
        "html_open": "<html" in content,
        "html_close": "</html>" in content,
        "head_open": "<head" in content,
        "head_close": "</head>" in content,
        "body_open": "<body" in content,
        "body_close": "</body>" in content,
        "title": "title" in content.lower(),
        "jays_ref": "Jay" in content or "Jay's" in content,
    }

    for name, ok in checks.items():
        if not ok:
            ERRORS.append(f"{page}: missing/{name}")

if ERRORS:
    print("HTML STRUCTURE TEST FAILURES:")
    for e in ERRORS:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("HTML STRUCTURE TEST PASSED — all 3 pages have valid basic structure.")
    sys.exit(0)