import re, tkinter as tk


class TextW(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.current_word = None
        self.words = []

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        self.config_appearance()

    def replace_current_word(self, new_word):
        if self.current_word.startswith("\n"):
            self.delete("insert-1c wordstart+1c", "insert")
        else:
            self.delete("insert-1c wordstart", "insert")
        self.insert("insert", new_word)
    
    def get_all_text(self, *args):
        return self.get(1.0, tk.END)

    def get_all_text_ac(self, *args):
        return self.get(1.0, "insert-1c wordstart-1c") + self.get("insert+1c", tk.END)
    
    def get_all_words(self, *args):
        return self.words

    def update_words(self):
        for i in re.findall(r"\w+", self.get_all_text_ac()):
            if i not in self.words:
                self.words.append(i)
        self.master.update_completions()

    def on_change(self, *args):
        self.current_word = self.get("insert-1c wordstart", "insert")
        self.update_words()
        print(f"CursorIsOn<{self.current_word.strip()}>")
    
    def config_appearance(self):
        self.config(
            font=self.master.font, bg="#1e1e1e", 
            fg="#d4d4d4", wrap=tk.NONE, relief=tk.FLAT,
            highlightthickness=0, insertbackground="#aeafad")
        self.tag_config(tk.SEL, background="#264f78", foreground="#d4d4d4")
    
    def _proxy(self, *args):
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        return result