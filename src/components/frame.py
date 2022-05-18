import os
from tkinter import ttk


class Frame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.config(ondrop=self.drop)

    def drop(self, event):
        if os.path.isfile(event.data):
            self.base.set_opened_file(event.data)
