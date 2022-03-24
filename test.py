import tkinter as tk

root = tk.Tk()

def update(*args):
    a.set(txt.index(tk.INSERT))

txt = tk.Text(root)
txt.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

a = tk.StringVar()
lbl = tk.Label(root, textvariable=a)
lbl.pack(fill=tk.X, side=tk.BOTTOM, expand=True)

txt.bind("<KeyRelease>", update)

root.mainloop()