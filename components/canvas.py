import tkinter as tk


class Canvas(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.config(width=70, bg="#1e1e1e", highlightthickness=0)
