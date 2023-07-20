import os
import tkinter as tk

from .frame import Frame
from .tree import Tree


class DirectoryTree(Frame):
    def __init__(self, master, path=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.nodes = {}
        
        self.ignore_dirs = [".git", "__pycache__"]
        self.ignore_exts = [".pyc"]

        self.tree = Tree(self, path, doubleclick=self.openfile, singleclick=self.preview_file, *args, **kwargs)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        self.path = path
        if path:
            self.change_path(path)
        else:
            self.tree.insert('', 0, text='You have not yet opened a file.')

    def change_path(self, path):
        self.nodes.clear()
        self.path = path
        if self.path:
            self.tree.clear_tree()
            self.create_root()
        else:
            self.tree.insert('', 0, text='You have not yet opened a file.')
    
    def create_root(self):
        self.update_treeview([(p, os.path.join(self.path, p)) for p in os.listdir(self.path)])

        for path, item in list(self.nodes.items()):
            if not os.path.exists(path):
                self.tree.delete(item)
                self.nodes.pop(path)

    def get_actionset(self):
        return self.actionset
    
    def scandir(self, path):
        entries = []
        for entry in os.scandir(path):
            entries.append((entry.name, entry.path))
        return entries

    def update_treeview(self, entries, parent=""):
        entries.sort(key=lambda x: (not os.path.isdir(x[1]), x[0]))
        for name, path in entries:
            if os.path.isdir(path):
                if name in self.ignore_dirs:
                    continue
                if path in self.nodes.keys():    
                    continue
                item = self.tree.tree.insert(parent, "end", text=f"  {name}", values=[path, 'directory'], image='foldericon', open=False)
                self.nodes[path] = item
                self.update_treeview(self.scandir(path), item)
            else:
                if name.split(".")[-1] in self.ignore_exts:
                    continue
                if path in self.nodes.keys():    
                    continue

                #TODO check filetype and get matching icon, cases
                item = self.tree.tree.insert(parent, "end", text=f"  {name}", values=[path, 'file'], image='document')
                self.nodes[path] = item

    def close_directory(self):
        self.change_path(None)
    
    def openfile(self, _):
        ...
    
    def preview_file(self, *_):
        ...
