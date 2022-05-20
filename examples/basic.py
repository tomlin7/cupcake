"""
Cupcake running with C++ code editing features.

Features enabled:
- Syntax highlighting
- Autocompletions (keywords & words)
- Minimap
"""

# for importing from top level
from src import Editor
import tkinter as tk
import sys
sys.path.append('.')
sys.path.append('..')


class Basic(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(1100, 700)
        self.config(bg="#1e1e1e")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.base = Editor(self)
        
        self.add_editor()

    def add_editor(self):
        self.editor = Editor(self)
        self.editor.grid(sticky=tk.NSEW)
        self.editor.focus()


root = Basic()
root.focus_set()
root.mainloop()
