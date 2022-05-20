import tkinter as tk
from cupcake import Editor

def test_editor():
    root = tk.Tk()
    root.after(10, root.destroy)

    e = Editor(root)
    e.pack()

    root.mainloop()
