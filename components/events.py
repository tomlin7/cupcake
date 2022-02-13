class Events:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.base = master.base

        self.bind_all()

    def bind_to_editor(self, key, fn):
        self.master.bind(key, fn)

    def bind_to_editor_text(self, key, fn):
        self.master.text.bind(key, fn)
    
    def bind_all(self):
        self.bind_to_editor_text("<Control-a>", self.master.text.select_all)