"""
Cupcake running with code editing features.

Features enabled:
- Syntax highlighting
- Autocompletions (words only, no lsp)
- Minimap
"""

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root)
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
