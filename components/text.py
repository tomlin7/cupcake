import re, tkinter as tk

from .highlighter import Highlighter
from .autocomplete import AutoComplete
from .syntax import SyntaxLoader
from .textw import TextW

class Text(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.master = master
        self.base = master.base

        self.font = self.master.font
        self.pack_propagate(False)

        self.syntax = SyntaxLoader()

        self.textw = TextW(self, width=0, height=0, *args, **kwargs)
        self.textw.pack(expand=True, fill=tk.BOTH)

        self.highlighter = Highlighter(self.textw)

        self.config_appearance()

        self.current_indentation = None
        self.current_line = None

        self.auto_completion = AutoComplete(self, items=self.syntax.get_autocomplete_list())
        self.completion_active = False

        self.config_bindings()
    
    def config_bindings(self):
        self.textw.bind("<Return>", self.enter_key_events)
        self.textw.bind("<KeyRelease>", self.show_autocomplete)

        for btn in ["<Button-2>", "<BackSpace>", "<Escape>", "<Right>", "<Left>", "<Control_L>", "<Control_R>"]:
            self.textw.bind(btn, self.auto_completion.hide)
        
        self.textw.bind("<Up>", self.auto_completion.move_up)
        self.textw.bind("<Down>", self.auto_completion.move_down)

        self.textw.bind("<Tab>", self.auto_completion.tab)

        # self.textw.bind("<space>", self.handle_space())
    
    # def handle_space(self, *args):
    #     self.textw.insert(tk.INSERT, "-")
        
    #     return "break"

    def get_all_text(self):
        return self.textw.get_all_text()

    def get_all_words(self):
        return self.textw.get_all_words()

    def get_current_word(self):
        return self.textw.current_word.strip()
    
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
            case "Tab":
                return False
            case "space":
                return False
            case "Up":
                return False
            case "Down":
                return False
            case "Control_L":
                return False
            case "Control_R":
                return False
            case _:
                return True

    def show_autocomplete(self, event):
        if not self.check_autocomplete_keys(event):
            return
        
        if self.textw.current_word.strip() not in ["{", "}", ":", "", None, "\""]:
            if not self.completion_active:
                if event.keysym in ["Left", "Right"]:
                    return
                pos = self.cursor_screen_location()
                self.auto_completion.show(pos)
                self.auto_completion.update_completions()
            else:
                self.auto_completion.update_completions()
        else:
            if self.completion_active:
                self.hide_autocomplete()
    
    def update_completion_words(self):
        self.auto_completion.update_all_words()
    
    def update_completions(self):
        self.auto_completion.update_completions()
    
    def hide_autocomplete(self):
        self.auto_completion.hide()
    
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

    def update_current_line(self):
        self.current_line = self.textw.get("insert linestart", "insert lineend")
        return self.current_line
    
    def add_newline(self, count=1):
        self.textw.insert(tk.INSERT, "\n" * count)
    
    def confirm_autocomplete(self, text):
        self.textw.replace_current_word(text)

    def enter_key_events(self, *args):
        if self.completion_active:
            self.auto_completion.choose()
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

    def select_all(self, *args):
        self.textw.tag_remove("highlight", 1.0, tk.END)
        
        self.textw.tag_add(tk.SEL, 1.0, tk.END)

        # scroll to top
        # self.mark_set(tk.INSERT, 1.0)
        # self.see(tk.INSERT)

        return "break"
