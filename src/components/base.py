from .style import Style
from .config import Config

from tkinter.filedialog import askopenfilename


class Base:
    def __init__(self, root, *args, **kwargs):
        self.root = root

        self.config = Config()
        self.style = Style(self)

        self.opened_file = None
    
    def open_file(self):
        self.opened_file = file = askopenfilename(filetypes=[("All Files", "*.*")])
        
        if file:
            self.set_opened_file(file)
    
    def set_opened_file(self, file):
        if file:
            self.root.editor.load_file(file)
            self.root.show_editor()
            self.root.refresh_editor()
            
