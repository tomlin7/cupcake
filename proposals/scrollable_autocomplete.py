from distutils.command.config import config
import tkinter as tk

class Item(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.text = tk.Label(self, text=text, width=50, height=1, anchor=tk.W)
        self.text.pack(side=tk.LEFT, fill=tk.X, expand=True)

root = tk.Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root,width=300,height=100)
frame.grid(row=0,column=0)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)

canvas = tk.Canvas(frame, width=300, height=500)

vbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
vbar.grid(row=0, column=1, sticky=tk.NS)
vbar.config(command=canvas.yview)

# hbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
# hbar.pack(side=tk.BOTTOM, fill=tk.X)
# hbar.config(command=canvas.xview)

canvas.config(width=300, height=300)
canvas.config(yscrollcommand=vbar.set) # xscrollcommand=hbar.set
canvas.grid(row=0, column=0, sticky=tk.NSEW)

for i in range(20):
    a = Item(canvas, text=f"Hello world {i}")
    canvas.create_window(0, i * 20, anchor=tk.NW, window=a)

canvas.config(scrollregion=canvas.bbox(tk.ALL))

root.mainloop()