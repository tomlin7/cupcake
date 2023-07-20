import os
import tkinter as tk
from .pathview import PathView

from ..utils import Frame, Menubutton


class Item(Menubutton):
    def __init__(self, master, path, *args, **kwargs):
        super().__init__(master, font=("Segoe UI", 10), *args, **kwargs)
        self.path = path
        self.config(height=1, pady=2, padx=1) # **self.base.theme.editors.breadcrumbs.item


class BreadCrumbs(Frame):
    def __init__(self, master, path=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(padx=10) # **self.base.theme.editors.breadcrumbs

        self.pathview = PathView(self)

        # if the file does not belong to active directory, use the absolute path instead
        path = os.path.abspath(path).split('\\')
        for i, item in enumerate(path):
            text = item if item == path[-1] else f"{item} ›"
            self.additem("\\".join(path[:i]), text)

    def additem(self, path, text):
        btn = Item(self, path, text=text)
        btn.bind("<Button-1>", self.pathview.show)
        btn.pack(side=tk.LEFT)
