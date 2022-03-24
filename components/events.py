class Events:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.base = master.base

        self.bind_all()

    def bind_to_editor(self, key, fn):
        self.master.bind(key, fn)

    def bind_to_editor_text(self, key, fn):
        self.master.text.textw.bind(key, fn)
    
    def bind_all(self):
        # self.bind_to_editor_text("<Control-a>", self.master.text.select_all)
        self.bind_to_editor_text("<<Change>>", self.master._text_modified)
        self.bind_to_editor_text("<Configure>", self.master._redraw_ln)

        self.bind_to_editor_text("<Control-MouseWheel>", self.master._handle_zoom)

        # linux 
        # self.bind_to_editor_text("<Control-Button-4>", lambda *args: self.master._handle_zoom(1))
        # self.bind_to_editor_text("<Control-Button-5>", lambda *args: self.master._handle_zoom(-1))