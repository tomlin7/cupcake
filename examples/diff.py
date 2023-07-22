"""
Cupcake diff editor
"""

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

data1 = """import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, __file__, darkmode=False)
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
"""

data2 = """import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor

root = tk.Tk()
root.minsize(800, 600)
# this is a new line
e = Editor(root, __file__, darkmode=False)

root.mainloop()
"""

e = Editor(root, diff=True)
e.content.show_diff_text(data1, data2)
e.pack(expand=1, fill=tk.BOTH)

root.mainloop()
