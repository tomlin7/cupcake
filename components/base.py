from .config import Config

from tkinter.filedialog import askopenfilename


class Base:
    def __init__(self, root, *args, **kwargs):
        self.root = root

        self.config = Config()

        self.opened_file = None
    
    def open_file(self):
        self.opened_file = askopenfilename(filetypes=[("All Files", "*.*")])
        
        if self.opened_file:
            self.root.editor.text.load_file(self.opened_file)

            self.root.show_editor()
