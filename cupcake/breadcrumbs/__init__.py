import os
import tkinter as tk

from ..utils import Frame, Menubutton
from .pathview import PathView


class Item(Menubutton):
    def __init__(self, master, path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.path = path
        self.config(
            pady=3,
            padx=3,
            font=self.base.settings.uifont,
            **self.base.theme.breadcrumbs,
        )


class BreadCrumbs(Frame):
    """BreadCrumbs class.

    Args:
        master: Parent widget.
        path: Path to the file.

    Attributes:
        pathview: PathView object.
    """

    def __init__(self, master, path="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(padx=20, bg=self.base.theme.breadcrumbs["background"])

        self.pathview = PathView(self)
        path = os.path.abspath(path).split("\\")
        for i, item in enumerate(path):
            text = item if item == path[-1] else f"{item} ›"
            self.additem("\\".join(path[:i]), text)

    def additem(self, path: str, text: str):
        """Adds an item to the breadcrumbs.

        Args:
            path: Path to the item.
            text: Text to display.
        """

        btn = Item(self, path, text=text)
        btn.bind("<Button-1>", self.pathview.show)
        btn.pack(side=tk.LEFT)
