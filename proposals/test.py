from tkinter import *

class App:
    def __init__(self):
        self.t = Text(root)
        self.t.place(x = 50,y = 50,width = 400,height = 400)
        for i in range(300):
            self.t.insert(END,str(i))
            self.t.insert(END,"\n")
        self.c = Canvas(root)
        self.c.place(x = 450,y = 50,width = 20,height = 400)
        self.trough = Canvas(self.c,bg = "red")
        self.slider = Label(self.c,bg = "grey")
        self.slidery = 20
        self.sliderh = 200
        self.trough.place(x = 0,y = 20,width = 20,height = 360)
        self.slider.place(x = 0,y = 20,width = 20,height = 200)
        self.up = Label(self.c,bg = "purple")
        self.down = Label(self.c,bg = "purple")
        self.up.place(x = 0,y = 0,width = 20,height = 20)
        self.down.place(x = 0,y = 380,width = 20,height = 20)
        self.up.bind("<Button-1>",self.up_view)
        self.down.bind("<Button-1>",self.down_view)
        self.slider.bind("<Button-1>",self.get_slider)
        self.slider.bind("<B1-Motion>",self.move_slider)
        self.slider.bind("<ButtonRelease-1>",self.release_slider)
        self.trough.bind("<Button-1>",self.next_page)
        self.config_slider()

    def next_page(self,event):
        y = event.y
        top = self.slidery - 20
        bottom = self.slidery + self.sliderh - 20
        coords = self.get_coords()
        if y < top:
            self.up_page(coords)
        if y > bottom:
            self.down_page(coords)

    def up_page(self,coords):
        up = -(coords[1] - coords[0])
        self.t.yview(SCROLL,-1,"pages")
        self.pos_slider()

    def down_page(self,coords):
        down = coords[1] - coords[0]
        self.t.yview(SCROLL,1,"pages")
        self.pos_slider()

    def pos_slider(self):
        coords = self.get_coords()
        self.slidery = (coords[0]/coords[2] * 360) + 20
        self.slider.place(y = self.slidery)

    def config_slider(self):
        coords = self.get_coords()
        top = coords[0]
        bottom = coords[1]
        last = coords[2]
        last -= 1
        if bottom-top < last:
            f = int((bottom-top)/last * 360)
        else:
            f = 360
        if f < 10:
            f = 10
        self.sliderh = f
        self.slider.place(height = f,y = self.slidery)

    def get_coords(self):
        root.update()
        top = self.t.index("@0,0")
        bottom = self.t.index("@0,%d" %self.t.winfo_height())
        last = self.t.index(END)
        t = top.split(".")
        b = bottom.split(".")
        l = last.split(".")
        top = int(t[0])
        bottom = int(b[0])
        last = int(l[0])
        return [top,bottom,last]

    def up_view(self,event):
        self.t.yview(SCROLL,-2,"units")
        self.pos_slider()

    def down_view(self,event):
        self.t.yview(SCROLL,2,"units")
        self.pos_slider()

    def get_slider(self,event):
        self.y = event.y_root
        self.config_slider()

    def move_slider(self,event):
        y = event.y_root - self.y
        y += self.slidery
        if y < 20:
            y = 20
        if y > 380 - self.sliderh:
            y = 380 - self.sliderh
        self.slider.place(y = y)
        self.move_text(y)

    def move_text(self,y):
        coords = self.get_coords()
        y1 = 360 - self.sliderh
        if y1 != 0:            
            prop = (coords[1]-coords[0])/coords[2]
            prop1 = 1-prop
            prop2 = (y-20)/prop1
            f = prop2/360 * prop1
            self.t.yview(MOVETO,f)

    def release_slider(self,event):
        y = event.y_root - self.y + self.slidery
        if y < 20:
            y = 20
        if y > 380 - self.sliderh:
            y = 380 - self.sliderh
        self.slidery = y
        self.slider.place(y = y)
        self.move_text(y)    
        self.config_slider()

root = Tk()
root.geometry("500x500")
app = App()
root.mainloop()