import tkinter as tk


class Kinds:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.base = master.base

        self.iobject = None
        
        self.ifunction = tk.PhotoImage(data="""iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAACXBIWXMAAA7DAAAOwwHHb6hk
        AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAddJREFUKJGNkjFrk3EQxn/3vtEW8QMICoK
        CNZYqDn4BndQ2NIMZRHES0TqILomW9toG7aJiW4cOQkGKoAhNagUHEZwspHQQm9SiDoI4iBqJJNb3/Z9D+0IaE+
        iz3d3z4+7gEZpoLru0OwjkDpAE5p3H5eRAfKHRJ/XF5GRhy46v2y9hNmxITiCNcCqqfeRqj3Z8+w/Oa+kouAlDq
        oL1JfTAm2j2VFd2+YQ3PeykiQwvWse4qjhZA5eyhlxAuL5o+x+oimv2Tn5o+biZGxMoJjSe8AAMuQJUzPg9qFgz
        cM1nNYGyQc8zfb/HW+/7AvcFRvJaKswOvTtWD80MF7vyWprD7IkTmwYqq4QxAchpseog/hf3pU38i5j1AwXDbnv
        IaYOUIRNGdTSph3/mtFgO4UisfkNKO1eBe49HP0y111bTIC8MHlksiPf2d31ufMNrbACk0nvLCY1ngKrzY4PNwJ
        bwZhXBoeC2bQZ4pZ/aAX8rfrAO213Be50bKp5XtZbXzOjSiV/U3gIvu3Xfxw0JM2wcqEUJy2mx4vzYIRfyp2XCI
        j0fW2kLvgfXDDIC0wbnwKZAzoA99NuCG92Zgz8i/wY40mx2eWcY2C3BzgosOM/19Q50zjf6/gEMUNa2RFgfkAAA
        AABJRU5ErkJggg==""")
        
        self.iclass = None
        self.imodule = None
        
        self.itext = tk.PhotoImage(data="""iVBORw0KGgoAAAANSUhEUgAAAA8AAAAICAYAAAAm06XyAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAA
        GXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAATBJREFUGJWFjyFLQ2EYhc95t31JEQYiGExaLBO
        DYbvJaFBEGBqHGNW4n6BFBUGw2ZUJCoaxMGT3Xm+1LwkLgrILwzLZdwy7wTD0iec9z4EXmEAcx40wDPcn3X5j/x
        X+gmEYLgA4JLkE4KFSqdzEcdwA0Jc0A0CSzoMgSNrt9pRzrg5gRVLXSNZIfki6AnDa6XRKGBsbku5IPpNsJkky5
        5x7AjAv6ZLkV344HJ4VCoUdM9uUNMrlcsuZfBEEwS0ARFG0670/BrDY6/XWq9XqCEAr75xrABgAeASwKilHElmG
        bIgkpwF8ZuL45yiKUgCBpG+SLwCOSG5LmvXebwEomdk9yTVJife+ViwWm/1+f9tI1iW1ssIrgIGkd0lmZm9mdk1
        yr1wudwFUzewkTdOU5MEPhImOHsSTJnYAAAAASUVORK5CYII=""")
