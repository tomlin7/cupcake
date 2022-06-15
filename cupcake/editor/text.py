import re
import tkinter as tk

from .highlighter import Highlighter
from .autocomplete import AutoComplete
from .language import SyntaxLoader


class Text(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.master = master

        self.font = self.master.font
        self.syntax = self.master.syntax
        self.pack_propagate(False)

        self.keywords = self.syntax.keywords
        self.current_word = None
        self.words = []

        self.highlighter = Highlighter(self)

        self.current_indentation = None
        self.current_line = None

        self.auto_completion = AutoComplete(
            self, items=self.syntax.get_autocomplete_list())

        self.create_proxy()
        self.config_appearance()
        self.config_tags()
        self.config_bindings()
    
    def create_proxy(self):
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
    
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

    def config_appearance(self):
        self.config(
            font=self.master.font, bg="#1e1e1e", 
            fg="#d4d4d4", wrap=tk.NONE, relief=tk.FLAT,
            highlightthickness=0, insertbackground="#aeafad")

    def config_bindings(self):
        self.bind("<KeyRelease>", self.key_release_events)

        self.bind("<Control-a>", self.select_all)
        self.bind("<Control-d>", self.multi_selection)

        self.bind("<Up>", self.auto_completion.move_up)
        self.bind("<Down>", self.auto_completion.move_down)

        self.bind("<Control-Left>",
                        lambda e: self.handle_ctrl_hmovement())
        self.bind("<Control-Right>",
                        lambda e: self.handle_ctrl_hmovement(True))
    
    def key_release_events(self, event):
        self.show_autocomplete(event)
        self.update_current_line()

        match event.keysym:
            # bracket pair completions
            case "braceleft":
                self.complete_bracket("}")
            case "bracketleft":
                self.complete_bracket("]")
            case "parenleft":
                self.complete_bracket(")")

            # surroundings for selection
            case "apostrophe":
                self.surrounding_selection("\'")
            case "quotedbl":
                self.surrounding_selection("\"")
            
            # autocompletion keys
            case "Button-2" | "BackSpace" | "Escape" | "Control_L" | "Control_R" | "space":
                self.hide_autocomplete()
            case "rightarrow" | "leftarrow":
                self.update_completions()

            # key events
            case "Return":
                self.enter_key_events()
            case "Tab":
                self.tab_key_events()
            
            # extra spaces
            case ":" | ",":
                self.insert(tk.INSERT, " ")

            case _:
                pass
            
    def complete_bracket(self, bracket):
        self.insert(tk.INSERT, bracket)
        self.mark_set(tk.INSERT, "insert-1c")
    
    def surrounding_selection(self, char):
        if self.tag_ranges(tk.SEL):
            self.insert(char, tk.SEL_LAST)
            self.insert(char, tk.SEL_FIRST)
    
    def enter_key_events(self):
        if self.auto_completion.active:
            self.auto_completion.choose()
            return "break"
        return self.check_indentation()

    def tab_key_events(self):
        if self.auto_completion.active:        
            self.auto_completion.choose()
            return "break"

    def move_to_next_word(self):
        self.mark_set(tk.INSERT, self.index("insert+1c wordend"))

    def move_to_previous_word(self):
        self.mark_set(tk.INSERT, self.index("insert-1c wordstart"))

    def handle_ctrl_hmovement(self, delta=False):
        if delta:
            self.move_to_next_word()
        else:
            self.move_to_previous_word()
        
        return "break"

    def get_all_text(self):
        return self.get_all_text()

    def get_all_words(self):
        return self.get_all_words()

    def get_current_word(self):
        return self.current_word.strip()
    
    def cursor_screen_location(self):
        pos_x, pos_y = self.winfo_rootx(), self.winfo_rooty()

        cursor = tk.INSERT
        bbox = self.bbox(cursor)
        if not bbox:
            return (0, 0)
        
        bbx_x, bbx_y, _, bbx_h = bbox
        return (pos_x + bbx_x - 1, pos_y + bbx_y + bbx_h)
    
    def show_autocomplete(self, event):
        if not self.check_autocomplete_keys(event):
            return
        
        if self.current_word.strip() not in ["{", "}", ":", "", None, "\""]:
            if not self.auto_completion.active:
                if event.keysym in ["Left", "Right"]:
                    return
                pos = self.cursor_screen_location()
                self.auto_completion.show(pos)
                self.auto_completion.update_completions()
            else:
                self.auto_completion.update_completions()
        else:
            if self.auto_completion.active:
                self.hide_autocomplete()
    
    def check_autocomplete_keys(self, event):
        return True if event.keysym not in [
            "BackSpace", "Escape", "Return", "Tab", "space", 
            "Up", "Down", "Control_L", "Control_R"] else False 

    def update_completion_words(self):
        self.auto_completion.update_all_words()
    
    def update_completions(self):
        self.auto_completion.update_completions()
    
    def hide_autocomplete(self):
        self.auto_completion.hide()
    
    def move_cursor(self, position):
        self.mark_set(tk.INSERT, position)

    def clear_all_selection(self):
        self.tag_remove(tk.SEL, 1.0, tk.END)
    
    def select_line(self, line):
        self.clear_all_selection()
        
        line = int(line.split(".")[0])
        start = str(float(line))
        end = str(float(line))
        self.tag_add(tk.SEL, start, end)

        self.move_cursor(end)
    
    def update_current_indent(self):
        line = self.get("insert linestart", "insert lineend")
        match = re.match(r'^(\s+)', line)
        self.current_indent = len(match.group(0)) if match else 0

    def update_current_line(self):
        self.current_line = self.get("insert linestart", "insert lineend")
        return self.current_line
    
    def add_newline(self, count=1):
        self.insert(tk.INSERT, "\n" * count)
    
    def confirm_autocomplete(self, text):
        self.replace_current_word(text)

    def check_indentation(self, *args):
        self.update_current_indent()
        if self.update_current_line():
            if self.current_line[-1] in ["{", "[", ":", "("]:
                self.current_indent += 4
            elif self.current_line[-1] in ["}", "]", ")"]:
                self.current_indent -= 4
            
            self.add_newline()
            self.insert(tk.INSERT, " " * self.current_indent)

            self.update_current_indent()
            
            return "break"

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
        
        self.mark_set(tk.INSERT, 1.0)

    def select_all(self, *args):
        self.tag_remove("highlight", 1.0, tk.END)
        
        self.tag_add(tk.SEL, 1.0, tk.END)

        # scroll to top
        # self.mark_set(tk.INSERT, 1.0)
        # self.see(tk.INSERT)

        return "break"

    # def handle_space(self, *args):
    #     self.insert(tk.INSERT, "-")

    #     return "break"

    def multi_selection(self, *args):
        #TODO: multi cursor editing

        return "break"

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
        self.words = re.findall(r"\w+", self.get_all_text_ac())
        self.update_completion_words()

    def highlight_current_word(self):
        self.tag_remove("highlight", 1.0, tk.END)
        text = self.get("insert wordstart", "insert wordend")
        word = re.findall(r"\w+", text)
        if any(word):
            if word[0] not in self.keywords:
                self.highlighter.highlight_pattern(f"\\y{word[0]}\\y", "highlight", regexp=True)

    def on_change(self, *args):
        self.current_word = self.get("insert-1c wordstart", "insert")
        self.update_words()
        self.highlight_current_word()
    
    
    def config_tags(self):
        self.tag_config(tk.SEL, background="#264f78", foreground="#d4d4d4")
        self.tag_config("highlight", background="#464646", foreground="#d4d4d4")
