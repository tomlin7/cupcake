from tkinter import *
from PIL import Image, ImageTk

root = Tk()

images = []  # to hold the newly created image

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=images[-1], anchor='nw')

canvas = Canvas(width=300, height=200)
canvas.pack()

create_rectangle(10, 10, 200, 100, fill='blue')
create_rectangle(50, 50, 250, 150, fill='green', alpha=.5)
create_rectangle(80, 80, 150, 120, fill='#800000', alpha=.8)

root.mainloop()