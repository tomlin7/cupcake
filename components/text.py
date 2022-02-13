import re, tkinter as tk

from components.highlighter import Highlighter


class Text(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.highlighter = Highlighter(self)

        self.config_appearance()

        self.current_indentation = None
        self.current_line = None

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        self.bind("<Return>", self.check_indentation)
    
    def update_current_indent(self):
        line = self.get("insert linestart", "insert lineend")
        match = re.match(r'^(\s+)', line)
        self.current_indent = len(match.group(0)) if match else 0

    def update_current_line(self):
        self.current_line = self.get("insert linestart", "insert lineend")
        return self.current_line
    
    def add_newline(self, count=1):
        self.insert(tk.INSERT, "\n" * count)

    def check_indentation(self, event):
        if self.update_current_line():
            if self.current_line[-1] in ["{", "[", ":"]:
                self.update_current_indent()

                new_indent = self.current_indent + 1
                self.add_newline()
                self.insert(tk.INSERT, "    " * new_indent)
                
                self.update_current_indent()
                return "break"

    def config_appearance(self):
        self.config(
            font=self.base.config.font, bg="#1e1e1e", 
            fg="#d4d4d4", wrap=tk.NONE, relief=tk.FLAT,
            highlightthickness=0)
        self.tag_config(tk.SEL, background="#3a3d41", foreground="#ffffff")

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

    def get_origin(self):
        return self.index("@0,0")

    def get_line_info(self, line):
        return self.dlineinfo(line)
    
    def clear_insert(self, content):
        self.delete(1.0, tk.END)
        self.insert(1.0, content)

    def load_file(self, path):
        with open(path, 'r') as fp:
            self.clear_insert(fp.read())
    
    def select_all(self, *args):
        self.tag_add(tk.SEL, 1.0, tk.END)

        # scroll to top
        # self.mark_set(tk.INSERT, 1.0)
        # self.see(tk.INSERT)

        return "break"
