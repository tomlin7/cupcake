import tkinter as tk

from .button import Button
from .frame import Frame


class EmptyWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.button = Button(self, command=self.open_file, text="Open File")
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def open_file(self, *args):
        self.base.open_file()
