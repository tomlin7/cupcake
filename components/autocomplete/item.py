from cgitb import text
import tkinter as tk

# iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MEVBMTczNDg3QzA5MTFFNjk3ODM5NjQyRjE2RjA3QTkiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MEVBMTczNDk3QzA5MTFFNjk3ODM5NjQyRjE2RjA3QTkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowRUExNzM0NjdDMDkxMUU2OTc4Mzk2NDJGMTZGMDdBOSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowRUExNzM0NzdDMDkxMUU2OTc4Mzk2NDJGMTZGMDdBOSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PjjUmssAAAGASURBVHjatJaxTsMwEIbpIzDA6FaMMPYJkDKzVYU+QFeEGPIKfYU8AETkCYI6wANkZQwIKRNDB1hA0Jrf0rk6WXZ8BvWkb4kv99vn89kDrfVexBSYgVNwDA7AN+jAK3gEd+AlGMGIBFDgFvzouK3JV/lihQTOwLtOtw9wIRG5pJn91Tbgqk9kSk7GViADrTD4HCyZ0NQnomi51sb0fUyCMQEbp2WpU67IjfNjwcYyoUDhjJVcZBjYBy40j4wXgaobWoe8Z6Y80CJBwFpunepIzt2AUgFjtXXshNXjVmMh+K+zzp/CMs0CqeuzrxSRpbOKfdCkiMTS1VBQ41uxMyQR2qbrXiiwYN3ACh1FDmsdK2Eu4J6Tlo31dYVtCY88h5ELZIJJ+IRMzBHfyJINrigNkt5VsRiub9nXICdsYyVd2NcVvA3ScE5t2rb5JuEeyZnAhmLt9NK63vX1O5Pe8XaPSuGq1uTrfUgMEp9EJ+CQvr+BJ/AAKvAcCiAR+bf9CjAAluzmdX4AEIIAAAAASUVORK5CYII=


class Kind(tk.Label):
    def __init__(self, master, kind=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base
        self.config_appearance()

        self.img = tk.PhotoImage(data='''
iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAWRJREFUOE/dlL1Rw0AQhb89ApQZOnCIyKgAKAD/dOAOkCvwUgFyBbgDYSgAUwGZFUIH2JkIuGXOoEEY/8F4CLhEGuned29n356w5SVb5vH3wBsdJ4brYSY46TV7B/1VVS11mGl+4pBLsKnHJwHicClIzWPdtsajReBvwEwf9oToUoy2CElD40FVeKN5x4zUhMwoum09mlT/fwMONR+BTTwvnfnNpTAc6tgdCFJraHy6DmgY03cHXLQ1fqoKMs3rAr1QAUKtqfEXU4scmqfYd0SJQUeEK2/FrBFOonM8XYTUU6SO6HkjYLkpuHGgGC1EDGzoQUvXQ83tR8Cy1KHmGt6bGs+ele//AzhOwR1Xwztf8mfo/X1TD2ehL9fCSbnVcesVSYG7EN7Q8SAInQ2hB053sORMD6/np2XF6IXwRglGgsjjh7AO1g/gZaFfe9u8R8eCWzySzAd9Y4e/vSfXOvwpeOvAN08wuhXCJcf7AAAAAElFTkSuQmCC
''')

        if kind:
            self.config_image()

    def config_appearance(self):
        self.config(bg="#252526")
    
    def config_image(self):
        # more images
        self.config(image=self.img)

class AutoCompleteItem(tk.Frame):
    def __init__(self, master, left, kind=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base


        self.left = left
        self.kind = kind

        self.kindw = Kind(self, kind)
        self.leftw = tk.Label(self,
            text=left, font=self.master.font, fg="#d4d4d4", anchor=tk.W, 
            bg="#252526", relief=tk.FLAT, highlightthickness=0, width=30)
        
        self.config(bg="#1e1e1e", width=300)
        # self.bind("<Button-1>", self.on_click)

        self.selected = False
        self.hovered = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.kindw.grid(row=0, column=0, sticky=tk.NSEW)
        self.leftw.grid(row=0, column=1, sticky=tk.NSEW)
    
    def on_click(self, *args):
        self.master.autocomplete(self.completion)
        self.master.hide()

    def toggle_selection(self):
        if self.selected:
            self.select()
        else:
            self.deselect()

    def select(self):
        self.config(bg="#094771") #, fg="#ffffff"
                    # activebackground="#0060c0", activeforeground="#ffffff")
        self.selected = True
    
    def deselect(self):
        self.config(bg="#ffffff") #, fg="#616161", 
                    # activebackground="#e8e8e8", activeforeground="#616161")
        self.selected = False