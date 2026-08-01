"""
setup_offline.py — Download external assets so lessons work fully offline.

Run once with your Anaconda Python:

    cd "D:\\OneDrive\\1. Quant\\Quant-Practice"
    python setup_offline.py

What it does:
- Downloads MathJax SVG bundle (single self-contained file, ~1.5 MB)
- Downloads Google Fonts (Playfair Display + Inter, ~200 KB total)
- Saves everything under Codex/assets/
- After running, lesson HTML files load MathJax and fonts from local disk
- No internet needed for subsequent viewing

Safe to re-run — will just overwrite existing files.
"""

import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")

# ---------------- What to download ----------------

DOWNLOADS = [
    # MathJax SVG bundle — self-contained, no additional font files needed.
    # This is the only critical asset for offline math rendering.
    (
        "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js",
        "mathjax/tex-mml-svg.js",
        "MathJax SVG (self-contained math renderer)",
    ),
    # NOTE: Fonts (Playfair Display + Inter) were removed from download because
    # Google Fonts URLs change with each version update (v37 -> v40 -> ...).
    # The HTML uses system-font fallbacks (Georgia + Segoe UI/system-ui) which
    # look nearly identical and are always available. No offline download needed.
]

# ---------------- Local fonts.css: empty stylesheet triggers the smart loader
# to fall through to the system font stack declared in the HTML. Prevents
# 404 error on ../../assets/fonts/fonts.css when we don't ship fonts.
FONTS_CSS = """/* Placeholder — fonts served from system fallback stack in HTML.
   No web fonts downloaded to avoid Google Fonts version churn.
   HTML falls back to Georgia (serif) and system-ui (sans) automatically. */
"""


def download_one(url, rel_target, description):
    target = os.path.join(ASSETS, rel_target)
    os.makedirs(os.path.dirname(target), exist_ok=True)

    print(f"  → {description}")
    print(f"    URL: {url}")

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (offline-setup)",
                "Accept": "*/*",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
        with open(target, "wb") as f:
            f.write(data)
        size_kb = len(data) / 1024
        print(f"    ✓ Saved to {rel_target} ({size_kb:.0f} KB)")
        return True
    except urllib.error.HTTPError as e:
        print(f"    ✗ HTTP {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"    ✗ Network error: {e.reason}")
        return False
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def write_fonts_css():
    target = os.path.join(ASSETS, "fonts", "fonts.css")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(FONTS_CSS)
    print(f"  ✓ Wrote fonts.css")


def main():
    print("=" * 60)
    print("  Quant-Practice offline setup")
    print("=" * 60)
    print(f"Target folder: {ASSETS}")
    print()

    if not os.path.exists(os.path.join(ROOT, "lessons")):
        print("ERROR: lessons/ folder not found in the current directory.")
        print(f"Expected: {os.path.join(ROOT, 'lessons')}")
        print("Run this script from inside your Quant-Practice folder.")
        sys.exit(1)

    print("Downloading assets...")
    print()

    ok = 0
    fail = 0
    for url, rel, desc in DOWNLOADS:
        if download_one(url, rel, desc):
            ok += 1
        else:
            fail += 1
        print()

    print("Writing local fonts.css...")
    write_fonts_css()
    print()

    print("=" * 60)
    print(f"  Done. {ok} downloaded, {fail} failed.")
    print("=" * 60)

    if fail == 0:
        print()
        print("✓ Offline assets ready.")
        print("  Lesson HTML files will now load MathJax and fonts from local disk.")
        print("  You can view lessons without internet after browser caches once.")
    else:
        print()
        print(f"⚠ {fail} downloads failed.")
        print("  Lessons will still work via CDN when online.")
        print("  Re-run this script when network is stable.")


if __name__ == "__main__":
    main()
