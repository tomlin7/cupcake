import tkinter as tk


class SelectableText(tk.Text):

    def __init__(self, master, **kwarg):
        super().__init__(master, **kwarg)
        self.down_ind = ''
        self.up_ind = ''
        self.bind("<Control-Button-1>", self.mouse_down)
        self.bind("<B1-Motion>", self.mouse_drag)
        self.bind("<ButtonRelease-1>", self.mouse_up)
        self.bind("<BackSpace>", self.delete_)

    def mouse_down(self, event):
        self.down_ind = self.index(f"@{event.x},{event.y}")

    def mouse_drag(self, event):
        self.up_ind = self.index(f"@{event.x},{event.y}")
        if self.down_ind and self.down_ind != self.up_ind:
            self.tag_add(tk.SEL, self.down_ind, self.up_ind)
            self.tag_add(tk.SEL, self.up_ind, self.down_ind)

    def mouse_up(self, event):
        self.down_ind = ''
        self.up_ind = ''

    def delete_(self, event):
        selected = self.tag_ranges(tk.SEL)
        if len(selected) > 2:
            not_deleting = ''
            for i in range(1, len(selected) - 1):
                if i % 2 == 0:
                    not_deleting += self.get(selected[i-1].string, selected[i].string)
            self.delete(selected[0].string, selected[-1].string)
            self.insert(selected[0].string, not_deleting)
            return "break"


root = tk.Tk()

text = SelectableText(root, width=50, height=10)
text.grid()
text.insert('end', "This is the first line.\nThis is the second line.\nThis is the third line.")

root.mainloop()
