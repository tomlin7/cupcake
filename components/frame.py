import os
from tkinter import ttk


class Frame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.config(ondrop=self.drop)
    
    def set_pack_data(self, **kwargs):
        self.pack_data = kwargs
    
    def pack_frame(self):
        self.pack(**self.pack_data)

    def drop(self, event):
        if os.path.isfile(event.data):
            self.base.set_opened_file(event.data)
