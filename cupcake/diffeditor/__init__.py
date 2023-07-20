import re
import threading
import tkinter as tk

from .pane import DiffPane
from .differ import Differ
from ..editor import BaseEditor


class DiffEditor(BaseEditor):
    def __init__(self, master, path1, path2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # self.config(bg=self.base.theme.border)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.path1 = path1
        self.path2 = path2
        self.editable = True

        self.lhs_data = []
        self.rhs_data = []

        self.lhs_last_line = 0
        self.rhs_last_line = 0

        self.lhs = DiffPane(self, path1)
        self.lhs.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, 1))

        self.rhs = DiffPane(self, path2)
        self.rhs.grid(row=0, column=1, sticky=tk.NSEW)

        self.left = self.lhs.text
        self.right = self.text = self.rhs.text

        self.lhs.scrollbar['command'] = self.on_scrollbar
        self.rhs.scrollbar['command'] = self.on_scrollbar
        self.left['yscrollcommand'] = self.on_textscroll
        self.right['yscrollcommand'] = self.on_textscroll

        self.stipple = self.base.settings.res.stipple

        self.left.tag_config("addition", background=self.base.theme.editors.diff.not_exist, bgstipple=f"@{self.stipple}")
        self.left.tag_config("removal", background=self.base.theme.editors.diff.removed)

        # testing word based diff per line
        self.left.tag_config("uhhh", background="red")
        
        self.right.tag_config("addition", background=self.base.theme.editors.diff.addition)
        self.right.tag_config("removal", background=self.base.theme.editors.diff.not_exist, bgstipple=f"@{self.stipple}")

        # testing word based diff per line
        self.right.tag_config("uhhh", background="green")

        self.differ = Differ(self)
        self.show_diff()
        
        self.left.set_active(False)

    def on_scrollbar(self, *args):
        self.left.yview(*args)
        self.lhs.on_scroll()

        self.right.yview(*args)
        self.rhs.on_scroll()

    def on_textscroll(self, *args):
        self.lhs.scrollbar.set(*args)
        self.rhs.scrollbar.set(*args)
        self.on_scrollbar('moveto', args[0])
    
    def run_show_diff(self):
        threading.Thread(target=self.show_diff).start()
    
    def show_diff(self):
        with open(self.path1, 'r') as f:
            lhs_data = f.read()
        with open(self.path2, 'r') as f:
            rhs_data = f.read()

        lhs_lines = [line+"\n" for line in lhs_data.split('\n')]
        rhs_lines = [line+"\n" for line in rhs_data.split('\n')]
        
        self.diff = list(self.differ.get_diff(lhs_lines, rhs_lines))
        for i, line in enumerate(self.diff):
            marker = line[0]
            content = line[2:]

            match marker:
                case " ":
                    # line is same in both
                    self.left.write(content)
                    self.right.write(content)

                case "-":
                    # line is only on the left
                    self.lhs_last_line = int(float(self.left.index(tk.INSERT)))
                    self.left.write(content, "removal")

                    # TODO this check is done to make sure if this is a line with modifications
                    # and not a newly added line, but this is not done right.
                    self.left.newline("addition")

                case "+":
                    # line is only on the right
                    self.rhs_last_line = int(float(self.right.index(tk.INSERT)))
                    self.right.write(content, "addition")
                    
                    # TODO this check is done to make sure if this is a line with modifications
                    # and not a newly added line, but this is not done right.
                    self.left.newline("addition")

                case "?":
                    # the above line has changes
                    if matches := re.finditer(r'\++', content):
                        self.left.delete(str(float(self.rhs_last_line+1)), str(float(int(float(self.left.index(tk.INSERT))))))
                        for match in matches:
                            start = f"{self.rhs_last_line}.{match.start()}"
                            end = f"{self.rhs_last_line}.{match.end()}"
                            self.right.tag_add("uhhh", start, end)

                    if matches := re.finditer(r'-+', content):
                        self.right.delete(str(float(self.lhs_last_line+1)), str(float(int(float(self.right.index(tk.INSERT))))))
                        for match in matches:
                            start = f"{self.lhs_last_line}.{match.start()}"
                            end = f"{self.lhs_last_line}.{match.end()}"
                            self.left.tag_add("uhhh", start, end)
                    
            self.left.update()
            self.right.update()
        
        self.left.highlighter.highlight()
        self.right.highlighter.highlight()

        # Add extra empty lines at the bottom if one side has fewer lines
        lhs_line_count = int(float(self.left.index(tk.END))) - 1
        rhs_line_count = int(float(self.right.index(tk.END))) - 1
        if lhs_line_count > rhs_line_count:
            extra_newlines = lhs_line_count - rhs_line_count
            for _ in range(extra_newlines):
                self.right.newline()
        elif rhs_line_count > lhs_line_count:
            extra_newlines = rhs_line_count - lhs_line_count
            for _ in range(extra_newlines):
                self.left.newline()
