class Events:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.bind_all()

    def bind(self, key, fn):
        self.master.text.bind(key, fn)

    def bind_all(self):
        self.bind("<<Change>>", self.master.refresh_editor)
        self.bind("<Configure>", self.master.redraw_ln)
        self.bind("<Control-f>", self.master.show_find_replace)
