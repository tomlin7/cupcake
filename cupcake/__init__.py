__version__ = '0.10.0'
__version_info__ = tuple([ int(num) for num in __version__.split('.')])

__all__ = ["Editor", "get_editor", "DiffEditor", "ImageViewer", "TextEditor"]


import os
from tkinter.constants import *

from .utils import FileType, Frame
from .breadcrumbs import BreadCrumbs

from .diffeditor import DiffEditor
from .imageviewer import ImageViewer
from .texteditor import TextEditor

def get_editor(base, path=None, path2=None, diff=False):
    "picks the right editor for the given values"
    if diff:
        return DiffEditor()
    
    if path and os.path.isfile(path):
        if FileType.is_image(path):
            return ImageViewer()
        
        return TextEditor(base, path)
    
    return TextEditor(base)


class Editor(Frame):
    """
    Editor class
    Picks the right editor based on the path, path2 & exists values passed. Supports showing diff, images, text files. 
    If nothing is passed, empty text editor is opened.

    Attributes
    ----------
    path : str
        path of the file to be opened
    path2 : str
        path of file to be opened in diff, required if diff=True is passed
    diff : bool
        whether this is to be opened in diff editor
    showpath : bool
        whether to show the breadcrumbs for editor or not
    
    Methods
    -------
    save(path: str=None)
        If the content is editable writes to the specified path.
    focus()
        Gives focus to the content.
    """
    def __init__(self, master, path: str=None, path2: str=None, diff: bool=False, showpath: bool=True, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #self.config(bg=self.base.theme.border)
        self.path = path
        self.path2 = path2
        self.diff = diff
        self.showpath = showpath
        self.filename = os.path.basename(self.path) if path else None

        self.grid_columnconfigure(0, weight=1)
        self.content = get_editor(self, path, path2, diff)

        if path and self.showpath and not diff:
            self.breadcrumbs = BreadCrumbs(self, path)
            self.grid_rowconfigure(1, weight=1)  
            self.breadcrumbs.grid(row=0, column=0, sticky=EW, pady=(0, 1))
            self.content.grid(row=1, column=0, sticky=NSEW)
        else:
            self.grid_rowconfigure(0, weight=1)
            self.content.grid(row=0, column=0, sticky=NSEW)
    
    def save(self, path: str=None) -> None:
        self.content.save(path)
    
    def focus(self) -> None:
        self.content.focus()
