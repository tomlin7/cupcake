from cgitb import text
import tkinter as tk

from .itemkinds import Kinds


class Kind(tk.Label):
    def __init__(self, master, kinds, kind="text", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base
        self.kinds = kinds
        self.kind = kind

        self.image = None

        self.config_appearance()
        self.config_image()

    def config_appearance(self):
        self.config(bg="#252526")
    
    def config_image(self):
        match self.kind:
            case "object":
                self.image = self.kinds.iobject
            case "function":
                self.image = self.kinds.ifunction
            case "class":
                self.image = self.kinds.iclass
            case "module":
                self.image = self.kinds.imodule
            case _:
                self.image = self.kinds.itext
            # case "method":
            #     self.image = self.base.images.method_icon
            # case "attribute":
            #     self.image = self.base.images.attribute_icon
            # case "variable":
            #     self.image = self.base.images.variable_icon
            # case "keyword":
            #     self.image = self.base.images.keyword_icon
            # case "builtin":
            #     self.image = self.base.images.builtin_icon
        self.config(image=self.image)

class AutoCompleteItem(tk.Frame):
    def __init__(self, master, left, kind=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base
        
        self.left = left
        self.kind = kind

        self.kindw = Kind(self, self.master.autocomplete_kinds, kind)
        self.leftw = tk.Text(self, 
            font=(self.master.font['family'], 10), fg="#d4d4d4",
            bg="#252526", relief=tk.FLAT, highlightthickness=0, width=30, height=1)
        self.leftw.insert(tk.END, left)
        self.leftw.config(state=tk.DISABLED)

        self.leftw.tag_config("term", foreground="#18a3ff")
        
        self.config(bg="#1e1e1e", width=300)

        self.kindw.bind("<Button-1>", self.on_click)
        self.leftw.bind("<Button-1>", self.on_click)

        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

        self.selected = False
        self.hovered = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.kindw.grid(row=0, column=0, sticky=tk.NSEW)
        self.leftw.grid(row=0, column=1, sticky=tk.NSEW)
    
    def get_text(self):
        return self.left
    
    def get_kind(self):
        return self.kind

    def mark_term(self, term):
        start_pos = self.left.find(term)
        end_pos = start_pos + len(term)
        self.leftw.tag_remove("term", 1.0, tk.END)
        self.leftw.tag_add("term", f"1.{start_pos}", f"1.{end_pos}")
    
    def on_click(self, *args):
        self.master.choose(self)
    
    def on_hover(self, *args):
        if not self.selected:
            self.kindw.config(bg="#2a2d2e")
            self.leftw.config(bg="#2a2d2e")
            self.hovered = True

    def off_hover(self, *args):
        if not self.selected:
            self.kindw.config(bg="#252526")
            self.leftw.config(bg="#252526")
            self.hovered = False
    
    def toggle_selection(self):
        if self.selected:
            self.select()
        else:
            self.deselect()

    def select(self):
        self.kindw.config(bg="#094771")
        self.leftw.config(bg="#094771", fg="#ffffff")
        self.selected = True
    
    def deselect(self):
        self.kindw.config(bg="#252526")
        self.leftw.config(bg="#252526", fg="#d4d4d4")
        self.selected = False