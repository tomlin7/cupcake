import tkinter as tk

from .breakpoint import Breakpoint


class LineNumbers(tk.Frame):
    def __init__(self, master, tw, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.config_appearance()

        self.tw = tw

        self.cw = tk.Canvas(self)
        self.cw.config(width=68, bg="#1e1e1e", highlightthickness=0)
        self.cw.pack(fill=tk.BOTH, expand=True)
    
    def set_bar_width(self, width):
        self.configure(width=width)

    def config_appearance(self):
        self.font = self.master.font
        self.fill = "#858585"
        self.highlight_fill = "#c6c6c6"
        self.config(bg="#1e1e1e")
    
    def attach(self, tw):
        self.tw = tw
    
    def clear(self):
        self.cw.delete(tk.ALL)
    
    def mark_line(self, line):
        dline = self.tw.get_line_info(line)
        
        if not dline:
            return
        
        y = dline[1]
        btn =  tk.Menubutton(self.cw, 
            text=">", font=("Consolas", 14), fg="#1e1e1e", bg="#1e1e1e", cursor="hand2", 
            activeforeground="#c5c5c5", activebackground="#1e1e1e", borderwidth=0,
            width=2, height=1, pady=0, padx=0, relief=tk.FLAT)
        self.cw.create_window(70, y-2, anchor=tk.NE, window=btn)
    
    def highlight_current_line(self):
        self.mark_line(tk.INSERT)
    
    def select_line(self, line):
        self.tw.select_line(line)

    def redraw(self, *args):
        self.clear()
        self.highlight_current_line()
        self.redraw_line_numbers()

    def redraw_line_numbers(self):
        i = self.tw.get_origin()
        while True:
            dline = self.tw.get_line_info(i)
            if not dline:
                break

            y = dline[1]
            ln = str(i).split(".")[0]

            curline = self.tw.get_line_info(tk.INSERT)
            cur_y = None
            if curline:
                cur_y = curline[1]

            if y == cur_y:
                number = self.cw.create_text(46, y, anchor=tk.NE, text=ln, font=self.font, fill=self.highlight_fill, tag=i)
            else:
                number = self.cw.create_text(46, y, anchor=tk.NE, text=ln, font=self.font, fill=self.fill, tag=i)
            
            self.cw.tag_bind(i, "<Button-1>", lambda _, i=i: self.select_line(i))

            # drawing breakpoints -- needs optimisations
            # self.draw_breakpoint(y)

            i = self.tw.textw.index(f"{i}+1line")

    def draw_breakpoint(self, y):
        bp = Breakpoint(self.cw)
        self.cw.create_window(21, y-2, anchor=tk.NE, window=bp)
    
    def toggle_breakpoint(self, y):
        ...