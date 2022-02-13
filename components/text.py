import re, tkinter as tk

from components.highlighter import Highlighter


class TextW(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        self.config_appearance()
    
    def config_appearance(self):
        self.config(
            font=self.master.font, bg="#1e1e1e", 
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
            self.master.event_generate("<<Change>>", when="tail")

        return result


class Text(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.master = master
        self.base = master.base

        self.font = self.master.font

        self.pack_propagate(False)

        self.textw = TextW(self, width=0, height=0, *args, **kwargs)
        self.textw.pack(expand=True, fill=tk.BOTH)

        self.highlighter = Highlighter(self.textw)

        self.config_appearance()

        self.current_indentation = None
        self.current_line = None

        self.textw.bind("<Return>", self.check_indentation)
    
    def update_current_indent(self):
        line = self.textw.get("insert linestart", "insert lineend")
        match = re.match(r'^(\s+)', line)
        self.current_indent = len(match.group(0)) if match else 0
        print("indentation updated to ", len(match.group(0)) if match else 0)

    def update_current_line(self):
        self.current_line = self.textw.get("insert linestart", "insert lineend")
        return self.current_line
    
    def add_newline(self, count=1):
        self.textw.insert(tk.INSERT, "\n" * count)

    def check_indentation(self, event):
        self.update_current_indent()
        if self.update_current_line():
            if self.current_line[-1] in ["{", "[", ":", "("]:
                self.current_indent += 4
            elif self.current_line[-1] in ["}", "]", ")"]:
                self.current_indent -= 4
            
            self.add_newline()
            self.textw.insert(tk.INSERT, " " * self.current_indent)

            self.update_current_indent()
            
            return "break"

    def config_appearance(self):
        self.textw.config(bg="#1e1e1e")

    def get_origin(self):
        return self.textw.index("@0,0")

    def get_line_info(self, line):
        return self.textw.dlineinfo(line)
    
    def clear_insert(self, content):
        self.textw.delete(1.0, tk.END)
        self.textw.insert(1.0, content)

    def load_file(self, path):
        with open(path, 'r') as fp:
            self.clear_insert(fp.read())
    
    def select_all(self, *args):
        self.textw.tag_add(tk.SEL, 1.0, tk.END)

        # scroll to top
        # self.mark_set(tk.INSERT, 1.0)
        # self.see(tk.INSERT)

        return "break"
