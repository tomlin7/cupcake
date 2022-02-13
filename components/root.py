import tkinter as tk
from tkinterDnD import Tk

from .base import Base
from .editor import Editor
from .empty import EmptyWindow


class Root(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(700, 500)

        self.base = Base(self)

        self.add_empty_window()
        self.add_editor()

    def add_empty_window(self):
        self.empty = EmptyWindow(self)
        self.empty.set_pack_data(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.empty.pack_frame()

    def add_editor(self):
        self.editor = Editor(self)
        self.editor.set_pack_data(fill=tk.BOTH, expand=True,  side=tk.TOP)
    
    def show_editor(self):
        self.empty.pack_forget()
        self.editor.pack_frame()
    
    def hide_editor(self):
        self.editor.pack_forget()
        self.empty.pack_frame()
