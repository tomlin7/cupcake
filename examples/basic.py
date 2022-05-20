"""
Cupcake running with C++ code editing features.

Features enabled:
- Syntax highlighting
- Autocompletions (keywords & words)
- Minimap
"""

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root)
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
