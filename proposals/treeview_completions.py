import tkinter as tk
from tkinter import ttk

class AutoComplete(tk.Toplevel):
    def __init__(self, master, items=None, state=False, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
    
        self.tree = ttk.Treeview(self, show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.add_items(items)
        
        self.state = state
        self.items = items
        self.selection = 0
        self.refresh()

        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)

        if not state:
            self.withdraw()
    
    def add_items(self, items):
        for item in items:
            self.tree.insert("", "end", text=item, values=item)
    
    def refresh(self):
        self.select(self.selection)
        
    def select(self, index):
        item = self.tree.get_children()[index]
        self.tree.selection_set(item)
        self.tree.focus(item)
        self.tree.see(item)

    def show(self, *pos):
        if not self.state:
            self.update_idletasks()
            self.geometry("+{}+{}".format(*pos))
            self.deiconify()
            self.state = True
    
    def hide(self, *_):
        if self.state:
            self.withdraw()
            self.state = False
    
    def move_y(self, delta):
        if self.state:
            self.selection += delta
            if self.selection < 0:
                self.selection = len(self.items) - 1
            elif self.selection >= len(self.items):
                self.selection = 0
            self.refresh()
            
            return "break"
    
class Editor(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.text = tk.Text(self)
        self.text.pack(fill=tk.BOTH, expand=True)

        items = ["biscuit", "another", "heehoo", "awesomesauce"]

        self.autocomplete = AutoComplete(self, items=items)
        self.config_bindings()
    
    def config_bindings(self):
        self.text.bind("<KeyRelease>", self.show_autocomplete)
        for btn in ["<Button-2>", "<BackSpace>", "<Escape>", "<Right>", "<Left>", "<Control_L>", "<Control_R>"]:
            self.text.bind(btn, self.autocomplete.hide)
        
        self.text.bind("<Up>", lambda _: self.autocomplete.move_y(-1))
        self.text.bind("<Down>", lambda _: self.autocomplete.move_y(1))

    def show_autocomplete(self, *_):
        pos_x, pos_y = self.winfo_rootx(), self.winfo_rooty()

        cursor = tk.INSERT
        bbox = self.text.bbox(cursor)
        if not bbox:
            return (0, 0)
        
        bbx_x, bbx_y, _, bbx_h = bbox
        self.autocomplete.show(pos_x + bbx_x - 1, pos_y + bbx_y + bbx_h)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("AutoComplete")
    root.geometry("400x400")

    editor = Editor(root)
    editor.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
