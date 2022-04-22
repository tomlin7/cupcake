"""
Contains Editor class
"""

import tkinter as tk

from .find_replace import FindReplace
from .utils import Utils
from .events import Events
from .frame import Frame
from .text import Text
from .ln import LineNumbers
from .minimap import Minimap
from .scrollbar import AutoHideScrollbar

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

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.find_replace_active = False

        self.text = Text(self)
        self.ln = LineNumbers(self, self.text)
        self.minimap = Minimap(self, self.text)
        self.scrollbar = AutoHideScrollbar(self, command=self.text.textw.yview)
        self.text.textw.configure(yscrollcommand=self.scrollbar.set)
        self.find_replace = FindReplace(self, self.text)

        self.ln.grid(row=0, column=0, sticky=tk.NS)
        self.text.grid(row=0, column=1, sticky=tk.NSEW)
        self.minimap.grid(row=0, column=2, sticky=tk.NS)
        self.scrollbar.grid(row=0, column=3, sticky=tk.NS)

        self.events = Events(self)
    
    def show_find_replace(self, *args):
        if not self.find_replace_active:
            pos_x, pos_y, width = self.text.textw.winfo_rootx(), self.text.textw.winfo_rooty(), self.text.textw.winfo_width()
            self.find_replace.show(((pos_x + width) - (self.find_replace.winfo_width() + 10), pos_y))
        else:
            self.find_replace.reset()

    def focus(self):
        self.text.textw.focus()

    def set_fontsize(self, size):
        self.font.configure(size=size)
        # self.ln.set_bar_width(size * 4)
        self._redraw_ln()

    def refresh_fontsize(self):
        self.set_fontsize(self.zoom)
    
    def _handle_zoom(self, event):
        if event.delta == -120:
            self.zoom -= 1
        if event.delta == 120:
            self.zoom += 1
        
        # linux
        # if delta > 0:
        #     self.zoom += 1
        # else:
        #     self.zoom -= 1

        self.zoom = Utils.clamp(self.zoom, 5, 50)
        self.refresh_fontsize()
        return "break"

    def refresh_editor(self, *_):
        self._redraw_ln()
        self.text.textw.on_change()
        self.text.highlighter.highlight_all()
        self.minimap.redraw()

    def _redraw_ln(self, *_):
        self.ln.redraw()
    
    def load_file(self, filepath):
        self.text.load_file(filepath)
