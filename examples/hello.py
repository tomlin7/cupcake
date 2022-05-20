"""
Hello, have a Cupcake! 🧁
"""

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(700, 600)

e = Editor(root)
e.pack(expand=1, fill=tk.BOTH)

e.insert("Hello, have a cupcake!")

root.mainloop()
