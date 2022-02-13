import tkinter as tk


class Button(tk.Menubutton):
    def __init__(self, master, command, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.command = command

        self.config(
            bg="#0e639c", fg="#ffffff", activebackground="#1177bb", 
            activeforeground="#ffffff", font=("Helvetica", 13), pady=15, padx=15)

        self.bind("<Button-1>", command)