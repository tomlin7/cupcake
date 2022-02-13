"""
Contains Editor class
"""

import tkinter as tk

from .events import Events
from .frame import Frame
from .text import Text
from .ln import LineNumbers


class Editor(Frame):
    """
    Editor class
    """
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.text = Text(self)
        self.ln = LineNumbers(self, self.text)

        self.text.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)
        self.ln.pack(fill=tk.Y, side=tk.RIGHT, expand=True)

        self.events = Events(self)

        self.setup_bindings()

    def setup_bindings(self):
        self.text.bind("<<Change>>", self._text_modified)
        self.text.bind("<Configure>", self._redraw_ln)

    def _text_modified(self, *args):
        self._redraw_ln(*args)
        self.text.highlighter.highlight_all()

    def _redraw_ln(self, *args):
        self.ln.redraw()
