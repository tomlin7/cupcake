import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base
    
    def set_pack_data(self, **kwargs):
        self.pack_data = kwargs
    
    def pack_frame(self):
        self.pack(**self.pack_data)
