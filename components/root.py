import tkinter as tk
from tkinterDnD import Tk

from .base import Base
from .editor import Editor
from .empty import EmptyWindow


class Root(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(700, 500)
        self.config(bg="#1e1e1e")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.base = Base(self)

        self.add_empty_window()
        self.add_editor()

    def add_empty_window(self):
        self.empty = EmptyWindow(self)
        self.empty.grid(sticky=tk.NSEW)

    def add_editor(self):
        self.editor = Editor(self)
    
    def show_editor(self):
        self.empty.grid_remove()
        self.editor.grid(sticky=tk.NSEW)
    
    def hide_editor(self):
        self.editor.grid_remove()
        self.empty.grid()
