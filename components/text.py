import re, tkinter as tk

from .highlighter import Highlighter
from .autocomplete import AutoComplete

class TextW(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.current_word = None

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        self.config_appearance()

    def on_change(self, *args):
        self.current_word = self.get("insert-1c wordstart", "insert").strip()
        print("Current word: " + self.current_word)
    
    def config_appearance(self):
        self.config(
            font=self.master.font, bg="#1e1e1e", 
            fg="#d4d4d4", wrap=tk.NONE, relief=tk.FLAT,
            highlightthickness=0, insertbackground="#aeafad")
        #self.tag_config(tk.SEL, background="#3a3d41", foreground="#d4d4d4")
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

        self.auto_completion = AutoComplete(self, items=[["print", None], ["test", None]])
        self.completion_active = False

        self.config_bindings()
    
    def config_bindings(self):
        self.textw.bind("<Return>", self.enter_key_events)
        self.textw.bind("<KeyRelease>", self.show_autocomplete)

        for btn in ["<Button-2>", "<BackSpace>", "<Escape>"]:
            self.textw.bind(btn, self.auto_completion.hide)
        
        self.textw.bind("<Up>", self.auto_completion.move_up)
        self.textw.bind("<Down>", self.auto_completion.move_down)

        self.textw.bind("<Tab>", self.auto_completion.choose)

        self.textw.bind("<Right>", self.auto_completion.hide)
        self.textw.bind("<Left>", self.auto_completion.hide)

        # self.textw.bind("<space>", self.handle_space())
    
    # def handle_space(self, *args):
    #     self.textw.insert(tk.INSERT, "-")
        
    #     return "break"

    def get_current_word(self):
        return self.textw.current_word
    
    def cursor_screen_location(self):
        pos_x, pos_y = self.textw.winfo_rootx(), self.textw.winfo_rooty()

        cursor = tk.INSERT
        bbox = self.textw.bbox(cursor)
        if not bbox:
            return (0, 0)
        
        bbx_x, bbx_y, _, bbx_h = bbox
        return (pos_x + bbx_x - 1, pos_y + bbx_y + bbx_h)
    
    def check_autocomplete_keys(self, event):
        match event.keysym:
            case "BackSpace":
                return False
            case "Escape":
                return False
            case "Return":
                return False
            case _:
                return True

    def show_autocomplete(self, event):
        if not self.check_autocomplete_keys(event):
            return
        
        if self.textw.current_word not in ["{", "}", ":", None, " ", "\""]:
            if not self.completion_active:
                pos = self.cursor_screen_location()
                self.completion_active = True
                self.auto_completion.show(pos)
            else:
                self.auto_completion.update_completions()
        else:
            if self.completion_active:
                self.hide_autocomplete()
    
    def hide_autocomplete(self):
        self.auto_completion.hide()
        self.completion_active = False
    
    def move_cursor(self, position):
        self.textw.mark_set(tk.INSERT, position)

    def clear_all_selection(self):
        self.textw.tag_remove(tk.SEL, 1.0, tk.END)
    
    def select_line(self, line):
        self.clear_all_selection()
        line = int(line.split(".")[0])
        start = str(float(line))
        end = str(float(line))
        self.textw.tag_add(tk.SEL, start, end)

        self.move_cursor(end)
    
    def update_current_indent(self):
        line = self.textw.get("insert linestart", "insert lineend")
        match = re.match(r'^(\s+)', line)
        self.current_indent = len(match.group(0)) if match else 0
        print("indentation level updated to ", len(match.group(0)) if match else 0)

    def update_current_line(self):
        self.current_line = self.textw.get("insert linestart", "insert lineend")
        return self.current_line
    
    def add_newline(self, count=1):
        self.textw.insert(tk.INSERT, "\n" * count)
    
    def auto_complete(self, text):
        self.textw.insert(tk.INSERT, text)
    
    def enter_key_events(self, *args):
        if self.completion_active:
            self.auto_completion.choose()
            self.completion_active = False
            return "break"
        return self.check_indentation()

    def check_indentation(self, *args):
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

    # linux    
    def select_all(self, *args):
        self.textw.tag_add(tk.SEL, 1.0, tk.END)

        # scroll to top
        # self.mark_set(tk.INSERT, 1.0)
        # self.see(tk.INSERT)

        return "break"
