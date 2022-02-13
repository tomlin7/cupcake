from textwrap import fill
import tkinter as tk


class Canvas(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.config(width=50, bg="#1e1e1e", highlightthickness=0)


class LineNumbers(tk.Frame):
    def __init__(self, master, tw, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.config_appearance()

        self.tw = tw

        self.cw = Canvas(self)
        self.cw.pack(fill=tk.BOTH, expand=True)

    def config_appearance(self):
        self.font = self.base.config.font
        self.fill = "#ffffff"
        #self.config(bg="#1e1e1e")
    
    def attach(self, tw):
        self.tw = tw

    def redraw(self, *args):
        self.cw.delete(tk.ALL)

        i = self.tw.get_origin()
        while True:
            dline = self.tw.get_line_info(i)

            if not dline:
                break

            y = dline[1]
            ln = str(i).split(".")[0]

            self.cw.create_text(35, y, anchor=tk.NE, text=ln, font=self.font, fill=self.fill)

            i = self.tw.index(f"{i}+1line")

