import tkinter as tk

from ..config import Config
from .events import Events
from .linenumbers import LineNumbers
from .minimap import Minimap
from .scrollbar import Scrollbar
from .language import SyntaxLoader
from .text import Text
from .find_replace import FinderReplacer


class Editor(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.config = Config(self)
        self.font = self.config.font

        self.syntax = SyntaxLoader()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.text = Text(self)
        self.linenumebers = LineNumbers(self, self.text)
        self.minimap = Minimap(self, self.text)
        self.scrollbar = Scrollbar(self, self.text)

        # actual find-replace widget
        # self.find_replace = FindReplace(self, self.text)
        # self.find_replace_active = False
        print("about to instantitate")
        self.find_replace = FinderReplacer(self.master)
        #self.find_replace.on_close()
        self.bind("<Control-s>", self.find_replace.revive)

        self.linenumebers.grid(row=0, column=0, sticky=tk.NS)
        self.text.grid(row=0, column=1, sticky=tk.NSEW)
        self.minimap.grid(row=0, column=2, sticky=tk.NS)
        self.scrollbar.grid(row=0, column=3, sticky=tk.NS)

        self.events = Events(self)
        self.text.textw.config(yscrollcommand=self.text_scrolled)
        self.focus()

    def text_scrolled(self, *args):
        print(args)

    def show_find_replace(self):
        # positioning of the actual find_replace widget
        # if not self.find_replace_active:
        #     pos_x, pos_y, width = self.text.textw.winfo_rootx(), self.text.textw.winfo_rooty(), self.text.textw.winfo_width()
        #     self.find_replace.show(((pos_x + width) - (self.find_replace.winfo_width() + 10), pos_y))
        # else:
        #     self.find_replace.reset()
        self.find_replace.revive()

    def focus(self):
        self.text.textw.focus()
        self.refresh_editor()

    def set_fontsize(self, size):
        self.font.configure(size=size)
        self.linenumebers.set_bar_width(size * 4)

    def refresh_editor(self, *_):
        self.text.textw.on_change()
        self.text.highlighter.highlight_all()
        self.redraw_ln()
        self.minimap.redraw()
        self.scrollbar.redraw()

    def redraw_ln(self, *_):
        self.linenumebers.redraw()
        
    def insert(self, text):
        self.text.clear_insert(text)
    
    def load_file(self, filepath):
        self.text.load_file(filepath)
