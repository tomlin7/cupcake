import tkinter as tk

from .itemkinds import Kinds

from .item import AutoCompleteItem

class AutoComplete(tk.Toplevel):
    def __init__(self, master, geometry=None, items=None, state=False, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.autocomplete_kinds = Kinds(self)
        self.config(bg="#454545", borderwidth=1)
        
        self.state = state
        self.font = self.master.font

        if not state:
            self.withdraw()
        
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)

        self.grid_columnconfigure(0, weight=1)

        self.menu_items = []
        self.menu_items_text = []

        self.row = 0
        self.selected = 0

        if items:
            self.items = items
            # [(completion, type), ...]
            
            self.add_all_items()
            self.refresh_selected()
        
        self.configure_bindings()
    
    def update_completions(self):
        self.refresh_geometry()

        term = self.master.get_current_word()
        self.hide_all_items()

        new = [i for i in self.get_items_text() if i[0].startswith(term)]
        new += [i for i in self.get_items_text() if term in i[0] and i not in new]
        
        if any(new):
            self.show_items(new, term)
        else:
            self.hide()
    
    def move_up(self, *args):
        if self.state:
            self.select(-1)
            return "break"
    
    def move_down(self, *args):
        if self.state:
            self.select(1)
            return "break"

    def add_all_items(self):
        for i in self.items:
            self.add_item(i[0], i[1] if len(i) > 1 else None)

    def configure_bindings(self):
        root = self.base.root
        
        root.bind("<Button-1>" , self.hide)
        root.bind("<Configure>", self.refresh_geometry)
        root.bind("<FocusOut>", self.hide)

    def add_item(self, left, kind=None):
        new_item = AutoCompleteItem(self, left, kind=kind)
        new_item.grid(row=self.row, sticky=tk.EW)
        
        self.menu_items.append(new_item)
        self.menu_items_text.append((left, new_item))

        self.row += 1
        self.refresh_selected()

    def select(self, delta):
        self.selected += delta
        self.selected = min(max(0, self.selected), len(self.menu_items) - 1)
        self.refresh_selected()
    
    def reset_selection(self):
        self.selected = 0
        self.refresh_selected()

    def refresh_selected(self):
        for i in self.menu_items:
            i.deselect()
        self.menu_items[self.selected].select()

    def get_items(self):
        return self.menu_items
    
    def get_items_text(self):
        return self.menu_items_text
    
    def hide_all_items(self):
        for i in self.menu_items:
            i.grid_forget()
        
        self.menu_items = []
        self.row = 1
    
    def show_items(self, items, term):
        for i in items:
            i[1].grid(row=self.row, sticky=tk.EW, padx=1, pady=(0, 0))
            self.row += 1
            self.menu_items.append(i[1])

            i[1].mark_term(term)

        self.reset_selection()
    
    def refresh_geometry(self, *args):
        self.update_idletasks()
        self.geometry("+{}+{}".format(*self.master.cursor_screen_location()))

    def show(self, pos):
        self.state = True
        self.update_idletasks()
        self.update_completions()
        self.geometry("+{}+{}".format(*pos))
        self.deiconify()

    def hide(self, *args):
        self.state = False
        self.withdraw()
        self.master.completion_active = False
        # self.reset()
    
    def refresh_geometry(self, *args):
        self.update_idletasks()
        self.geometry("+{}+{}".format(*self.master.cursor_screen_location()))
    
    def reset(self):
        self.reset_selection()
    
    def choose(self, *args):
        self.master.auto_complete(self.menu_items_text[self.selected][0])
        self.hide()