"""
Cupcake light mode
"""

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, __file__, darkmode=False)
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
