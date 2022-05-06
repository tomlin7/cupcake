import tkinter as tk
from tkinter.font import Font

class TextPeer(tk.Text):
    """A peer of an existing text widget"""
    count = 0
    def __init__(self, master, cnf={}, **kw):
        TextPeer.count += 1
        parent = master.master
        peerName = "peer-{}".format(TextPeer.count)
        if str(parent) == ".":
            peerPath = ".{}".format(peerName)
        else:
            peerPath = "{}.{}".format(parent, peerName)

        # Create the peer
        master.tk.call(master, 'peer', 'create', peerPath, *self._options(cnf, kw))

        # Create the tkinter widget based on the peer
        # We can't call tk.Text.__init__ because it will try to
        # create a new text widget. Instead, we want to use
        # the peer widget that has already been created.
        tk.BaseWidget._setup(self, parent, {'name': peerName})

root = tk.Tk()

text_font = Font(family="Courier", size=14)
map_font = Font(family="Courier", size=4)

text = tk.Text(root, font=text_font, background="black", foreground="white")
minimap = TextPeer(text, font=map_font, state="disabled",
                   background="black", foreground="white")

minimap.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

root.mainloop()
