import tkinter as tk
import difflib, sys


class Differ(difflib.Differ):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master

    def get_diff(self, lhs, rhs):
        return self.compare(lhs, rhs)


class Editor(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super(Editor, self).__init__(master, *args, **kwargs)
        self.master = master
        
        self.config(
            width=50, font=("Consolas", 15),
            relief=tk.FLAT)
    
    def write(self, text):
        self.insert(tk.END, text)

class CV(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super(CV, self).__init__(master, *args, **kwargs)
        self.master = master
        
        self.config(width=100)

class Base(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super(Base, self).__init__(master, *args, **kwargs)
        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.left_data = ["This is first line", "This is second line", "This is third line"]
        self.right_data = ["This is first line", "ReKt", "This is third line"]

        self.left = Editor(self)
        self.cv = CV(self)
        self.right = Editor(self)

        self.left.grid(row=0, column=0, sticky=tk.NSEW)
        self.cv.grid(row=0, column=1, sticky=tk.NSEW)
        self.right.grid(row=0, column=2, sticky=tk.NSEW)

        self.differ = Differ(self)
        self.show_diff()
    
    def show_diff(self):
        self.diff = self.differ.get_diff(self.left_data, self.right_data)
        for line in self.diff:
            marker = line[0]

            if marker == " ":
                self.left.write(line[2:])
                self.right.write(line[2:])

            elif marker == "-":
                self.left.write(line[2:], "removal")
                self.right.newline("removal")

            elif marker == "+":
                self.left.newline("addition")
                self.right.write(line[2:], "addition")


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.master = self

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.base = Base(self)
        self.base.grid(row=0, column=0, sticky=tk.NSEW)

root = Root()
root.mainloop()