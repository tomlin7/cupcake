"""
Cupcake with TypeScript lexer
"""

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, ".github/res/screenshot.png")
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
