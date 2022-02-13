"""
Contains Editor class
"""

import tkinter as tk

from .utils import Utils

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

        self.font = self.base.config.font
        self.zoom = self.font["size"]

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.text = Text(self)
        self.ln = LineNumbers(self, self.text)

        self.ln.grid(row=0, column=0, sticky=tk.NS)
        self.text.grid(row=0, column=1, sticky=tk.NSEW)

        self.events = Events(self)

    def set_fontsize(self, size):
        self.font.configure(size=size)
        self.ln.set_bar_width(size * 4)
        self._redraw_ln()

    def refresh_fontsize(self):
        self.set_fontsize(self.zoom)
    
    def handle_zoom(self, delta):
        print("handle zoom")
        if 5 <= self.zoom <= 50:
            if delta > 0:
                self.zoom += 1
            else:
                self.zoom -= 1
        self.zoom = Utils.clamp(self.zoom, 5, 50)

        self.refresh_fontsize()
        return "break"

    def _text_modified(self, *args):
        self._redraw_ln(*args)
        self.text.highlighter.highlight_all()

    def _redraw_ln(self, *args):
        self.ln.redraw()
