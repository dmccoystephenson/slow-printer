# @author Daniel McCoy Stephenson
"""Build the browser version of Slow Printer: web/index.html and web/game.zip.

The program runs in the browser under tak's console runtime
(https://github.com/Stephenson-Software/tak, tak.web.console), its output going
to a terminal on the page. The only change made for this was turning its
Python 2 print statements into print(...) calls (see README.md). Needs tak
installed (see .github/workflows/browser.yml). Serve the result cross-origin
isolated, e.g. with arcade or tak.web.serve:

    python3 web/build_zip.py
    python3 -c "from tak.web.serve import main; main(root='.', title='Slow Printer')"
"""

import os

from tak.web.bundle import build
from tak.web.console import page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "web", "index.html"), "w", encoding="utf-8") as out:
    out.write(
        page(
            title='Slow Printer',
            tagline='Text, one letter at a time (2017)',
            entry='main.py',
            idbName='slow-printer-files',
            footer='More by Daniel Stephenson &rarr; <a href="https://danielstephenson.dev/play">danielstephenson.dev/play</a>',
        )
    )

build(root=ROOT, sourceDirectories=(), extraFiles=('main.py', 'version.txt'))
