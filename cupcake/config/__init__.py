from tkinter import font


class Config:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.font = font.Font(
            family="Consolas",
            size=11, weight="normal")      
