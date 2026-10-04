# Slow Printer

[![Play in your browser](https://img.shields.io/badge/Play-in%20your%20browser-2ea44f)](https://danielstephenson.dev/play/slow-printer)

A "Pokemon-style print function": it prints text one letter at a time, like a game's dialogue box. Run on its own it prints "Welcome to the game!"; other programs can import `slowprint` from it.

Written by Daniel McCoy Stephenson in March 2017, as one of his first programs. It is part of the "First Programs" collection on [danielstephenson.dev/play](https://danielstephenson.dev/play).

## Running it
```
python3 main.py
```
It also still runs under Python 2 (`python2 main.py`), which it was written for.

## Play in your browser
The program runs in a browser tab under [tak](https://github.com/Stephenson-Software/tak)'s console runtime (Python via Pyodide): https://slow-printer.play.danielstephenson.dev, listed with the rest at [danielstephenson.dev/play](https://danielstephenson.dev/play).

The only change made for this was turning its Python 2 `print` statements into `print(...)` calls, which print the same text under both Python 2 and Python 3. To build and serve it locally (needs `tak` installed):
```
python3 web/build_zip.py
python3 -c "from tak.web.serve import main; main(root='.', title='Slow Printer')"
```
Pushes to `master` deploy it to [arcade](https://github.com/Stephenson-Software/arcade) (`.github/workflows/browser.yml`).
