"""import tkinter as tk


''' 
    Text Location Demo
    Open a Tkinter window just under the location of the insertion cursor 
    of a Text widget.
'''

import tkinter as tk

#Some random text to display in the Text widget
lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Aenean lacinia tortor quis quam vehicula semper. Curabitur
faucibus, purus a egestas bibendum, velit metus hendrerit nulla, non
lobortis dolor mi in dolor. Aliquam ultrices felis sit amet dolor
gravida, id ullamcorper odio rutrum. Fusce consectetur tempor nibh, non
dictum dolor dictum nec. In hac habitasse platea dictumst. Morbi laoreet
consequat metus, at lacinia nisl suscipit id. Quisque vitae sodales
velit, a lobortis nisl. Praesent varius convallis efficitur. Vivamus
fringilla at risus nec viverra. Proin suscipit, lorem sed laoreet
ultricies, velit massa ornare nunc, vel egestas nibh ex vitae leo.'''

lorem_ipsum = lorem_ipsum.replace('\n', ' ')

class TextLocationDemo(object):
    ''' Text widget cursor location demo '''
    def __init__(self):
        root = tk.Tk()
        root.title("Text Location Demo")

        tk.Button(root, text="Show cursor location", 
            command=self.location_cb).pack()

        # Create a Text widget, with word wrapping
        self.textwidget = tw = tk.Text(root, wrap=tk.WORD)
        tw.pack()
        tw.insert(tk.END, lorem_ipsum)

        root.mainloop()

    def alert(self, geometry, msg):
        ''' Display `msg` in an Alert with given geometry,
            which is a tuple of (width, height, ox, oy)
        '''
        top = tk.Toplevel()
        # widget geometry parameter must be given in X windows format
        top.geometry("%dx%d%+d%+d" % geometry)

        msg = tk.Message(top, text=msg, width=geometry[0])
        msg.pack()

        button = tk.Button(top, text="Ok", command=top.destroy)
        button.pack()

    def location_cb(self):
        ''' Determine the location of the insertion cursor
            and display it in a window just under that location
        '''
        w = self.textwidget

        # Get the Text widget's current location
        pos_x, pos_y = w.winfo_rootx(), w.winfo_rooty()

        # Get the bounding box of the insertion cursor
        cursor = tk.INSERT
        bbox = w.bbox(cursor)
        if bbox is None:
            print('Cursor is not currently visible. Scrolling...')
            w.see(cursor)
            bbox = w.bbox(cursor)

        bb_x, bb_y, bb_w, bb_h = bbox

        #Open a window just beneath the insertion cursor
        width = 200
        height = 80
        ox = pos_x + bb_x
        oy = pos_y + bb_y + bb_h
        s = 'Cursor: (%d, %d)' % (ox, oy)
        print(s)

        geometry = (width, height, ox, oy)
        self.alert(geometry, s)


TextLocationDemo()
"""


import tkinter as tk


root = tk.Tk()

img = tk.PhotoImage(data='''
iVBORw0KGgoAAAANSUhEUgAAAAUA
AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO
9TXL0Y4OHwAAAABJRU5ErkJggg==
''')

lbl = tk.Label()
lbl.config(image=img, bg="#000000")
lbl.pack()


root.mainloop()