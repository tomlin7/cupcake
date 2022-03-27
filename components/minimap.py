import tkinter as tk


class Minimap(tk.Frame):
    def __init__(self, master, textw, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.tw = textw
        self.font = (self.master.font["family"], 2)

        self.config(bg="#1e1e1e", highlightthickness=0)
        self.cw = tk.Canvas(self, bg="#1e1e1e", width=100, highlightthickness=0)
        self.cw.pack(fill=tk.BOTH, expand=True)

        if textw:
            self.redraw()

    def attach(self, textw):
        self.tw = textw

    def redraw(self):
        self.cw.delete(tk.ALL)
        self.text = self.tw.get_all_text()
        self.cw.create_text(5, 0, text=self.text, anchor=tk.NW, font=self.font, fill="#678ca0")
