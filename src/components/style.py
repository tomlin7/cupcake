from tkinter import ttk


class Style(ttk.Style):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master= master
        
        self.configure("TFrame", background="#1e1e1e", relief="flat")
        self.configure("TLabel", background="#1e1e1e", foreground="#d4d4d4", relief="flat")

        self.configure("TEntry", foreground="#a6a6a6", fieldbackground="#3c3c3c", relief="flat", borderwidth=0)

        self.configure("TMenubutton", background="#3c3c3c", foreground="#a6a6a6", relief="flat")
        self.map("TMenubutton",
            foreground=[
                ("active", "#a6a6a6"), ("pressed", "#a6a6a6")
            ],
            background=[
                ("active", "#3c3c3c"), ("pressed", "#3c3c3c")
            ]
        )

        self.configure("TButton", background="#0e639c", foreground="#ffffff", relief="flat")
        self.map("TButton",
            foreground=[
                ("active", "#ffffff"), ("pressed", "#ffffff")
            ],
            background=[
                ("active", "#1177bb"), ("pressed", "#1177bb")
            ]
        )
