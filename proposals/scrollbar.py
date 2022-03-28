import tkinter as tk

class MyScrollbar(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        self._scroll_kwargs = { 'command':None,
                                'orient':'vertical',
                                'buttontype':'round',
                                'buttoncolor':'#006cd9',
                                'troughcolor':'#00468c',
                                'thumbtype':'rectangle',
                                'thumbcolor':'#4ca6ff',
                                }
        
        kwargs = self._sort_kwargs(kwargs)
        if self._scroll_kwargs['orient'] == 'vertical':
            if 'width' not in kwargs:
                kwargs['width'] = 10
        elif self._scroll_kwargs['orient'] == 'horizontal':
            if 'height' not in kwargs:
                kwargs['height'] = 10
        else:
            raise ValueError
        if 'bd' not in kwargs:
            kwargs['bd'] = 0
        if 'highlightthickness' not in kwargs:
            kwargs['highlightthickness'] = 0
        
        tk.Canvas.__init__(self, master, *args, **kwargs)
        
        self.elements = {   'button-1':None,
                            'button-2':None,
                            'trough':None,
                            'thumb':None}
        
        self._oldwidth = 0
        self._oldheight = 0
        
        self._sb_start = 0
        self._sb_end = 1
        
        self.bind('<Configure>', self._resize)
        self.tag_bind('button-1', '<Button-1>', self._button_1)
        self.tag_bind('button-2', '<Button-1>', self._button_2)
        self.tag_bind('trough', '<Button-1>', self._trough)
        
        self._track = False
        self.tag_bind('thumb', '<ButtonPress-1>', self._thumb_press)
        self.bind('<ButtonRelease-1>', self._thumb_release)
#       self.bind('<Leave>', self._thumb_release)
        
        self.bind('<Motion>', self._thumb_track)
            
    def _sort_kwargs(self, kwargs):
        to_remove = []
        for key in kwargs:
            if key in [ 'buttontype', 'buttoncolor', 'buttonoutline',
                        'troughcolor', 'troughoutline',
                        'thumbcolor', 'thumbtype', 'thumboutline',
                        'command', 'orient']:
                self._scroll_kwargs[key] = kwargs[key] # add to custom dict
                to_remove.append(key)
                
        for key in to_remove:
            del kwargs[key]
        return kwargs
        
    def _get_colour(self, element):
        if element in self._scroll_kwargs: # if element exists in settings
            return self._scroll_kwargs[element]
        if element.endswith('outline'): # if element is outline and wasn't in settings
            return self._scroll_kwargs[element.replace('outline', 'color')] # fetch default for main element
        
    def _width(self):
        return self.winfo_width() - 2 # return width minus 2 pixes to ensure fit in canvas
        
    def _height(self):
        return self.winfo_height() - 2 # return height minus 2 pixes to ensure fit in canvas
                
    def _resize(self, event):
        width = self._width()
        height = self._height()
        if self.elements['button-1']: # exists
            # delete element if vertical scrollbar and width changed
            # or if horizontal and height changed, signals button needs to change
            if (((self._oldwidth != width) and (self._scroll_kwargs['orient'] == 'vertical')) or
                ((self._oldheight != height) and (self._scroll_kwargs['orient'] == 'horizontal'))):
                self.delete(self.elements['button-1'])
                self.elements['button-1'] = None
        if not self.elements['button-1']: # create
            size = width if (self._scroll_kwargs['orient'] == 'vertical') else height
            rect = (0,0,size, size)
            fill = self._get_colour('buttoncolor')
            outline = self._get_colour('buttonoutline')
            if (self._scroll_kwargs['buttontype'] == 'round'):
                self.elements['button-1'] = self.create_oval(rect, fill=fill, outline=outline, tag='button-1')
            elif (self._scroll_kwargs['buttontype'] == 'square'):
                self.elements['button-1'] = self.create_rectangle(rect, fill=fill, outline=outline, tag='button-1')
            
        if self.elements['button-2']: # exists
            coords = self.coords(self.elements['button-2'])
            # delete element if vertical scrollbar and width changed
            # or if horizontal and height changed, signals button needs to change
            if (((self._oldwidth != width) and (self._scroll_kwargs['orient'] == 'vertical')) or
                ((self._oldheight != height) and (self._scroll_kwargs['orient'] == 'horizontal'))):
                self.delete(self.elements['button-2'])
                self.elements['button-2'] = None
            # if vertical scrollbar and height changed button needs to move
            elif ((self._oldheight != height) and (self._scroll_kwargs['orient'] == 'vertical')):
                self.move(self.elements['button-2'], 0, height-coords[3])
            # if horizontal scrollbar and width changed button needs to move
            elif ((self._oldwidth != width) and (self._scroll_kwargs['orient'] == 'horizontal')):
                self.move(self.elements['button-2'], width-coords[2], 0)
        if not self.elements['button-2']: # create
            if (self._scroll_kwargs['orient'] == 'vertical'):
                rect = (0,height-width,width, height)
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                rect = (width-height,0,width, height)
            fill = self._get_colour('buttoncolor')
            outline = self._get_colour('buttonoutline')
            if (self._scroll_kwargs['buttontype'] == 'round'):
                self.elements['button-2'] = self.create_oval(rect, fill=fill, outline=outline, tag='button-2')
            elif (self._scroll_kwargs['buttontype'] == 'square'):
                self.elements['button-2'] = self.create_rectangle(rect, fill=fill, outline=outline, tag='button-2')
        
        if self.elements['trough']: # exists
            coords = self.coords(self.elements['trough'])
            # delete element whenever width or height changes
            if (self._oldwidth != width) or (self._oldheight != height):
                self.delete(self.elements['trough'])
                self.elements['trough'] = None
        if not self.elements['trough']: # create
            if (self._scroll_kwargs['orient'] == 'vertical'):
                rect = (0, int(width/2), width, height-int(width/2))
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                rect = (int(height/2), 0, width-int(height/2), height)
            fill = self._get_colour('troughcolor')
            outline = self._get_colour('troughoutline')
            self.elements['trough'] = self.create_rectangle(rect, fill=fill, outline=outline, tag='trough')

        self.set(self._sb_start, self._sb_end) # hacky way to redraw thumb without moving it
        self.tag_raise('thumb') # ensure thumb always on top of trough
            
        self._oldwidth = width
        self._oldheight = height
        
    def _button_1(self, event):
        command = self._scroll_kwargs['command']
        if command:
            command('scroll', -1, 'pages')
        return 'break'
    
    def _button_2(self, event):
        command = self._scroll_kwargs['command']
        if command:
            command('scroll', 1, 'pages')
        return 'break'
        
    def _trough(self, event):
#       print('trough: (%s, %s)' % (event.x, event.y))
        width = self._width()
        height = self._height()
        
        coords = self.coords(self.elements['trough'])
        
        if (self._scroll_kwargs['orient'] == 'vertical'):
            trough_size = coords[3] - coords[1]
        elif (self._scroll_kwargs['orient'] == 'horizontal'):
            trough_size = coords[2] - coords[0]
#       print('trough size: %s' % trough_size)
        
        size = (self._sb_end - self._sb_start) / 1
        if (self._scroll_kwargs['orient'] == 'vertical'):
            thumbrange = height - width
        elif (self._scroll_kwargs['orient'] == 'horizontal'):
            thumbrange = width - height
        thumbsize = int(thumbrange * size)
        
        if (self._scroll_kwargs['orient'] == 'vertical'):
            thumboffset = int(thumbrange * self._sb_start) + int(width/2)
        elif (self._scroll_kwargs['orient'] == 'horizontal'):
            thumboffset = int(thumbrange * self._sb_start) + int(height/2)
        thumbpos = int(thumbrange * size / 2) + thumboffset
        
        command = self._scroll_kwargs['command']
        if command:
            if (((self._scroll_kwargs['orient'] == 'vertical') and (event.y < thumbpos)) or
                ((self._scroll_kwargs['orient'] == 'horizontal') and (event.x < thumbpos))):
                command('scroll', -1, 'pages')
            elif (((self._scroll_kwargs['orient'] == 'vertical') and (event.y > thumbpos)) or
                ((self._scroll_kwargs['orient'] == 'horizontal') and (event.x > thumbpos))):
                command('scroll', 1, 'pages')
        return 'break'
    
    def _thumb_press(self, event):
        self._track = True
        
    def _thumb_release(self, event):
        self._track = False
            
    def _thumb_track(self, event):
#       print('track')
        if self._track:
            width = self._width()
            height = self._height()
#           print("window size: (%s, %s)" % (width, height))
            
            size = (self._sb_end - self._sb_start) / 1
            
            coords = self.coords(self.elements['trough'])
#           print('trough coords: %s' % coords)
            
            if (self._scroll_kwargs['orient'] == 'vertical'):
                trough_size = coords[3] - coords[1]
                thumbrange = height - width
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                trough_size = coords[2] - coords[0]
                thumbrange = width - height
#           print('trough size: %s' % trough_size)
                
            thumbsize = int(thumbrange * size)
            
            if (self._scroll_kwargs['orient'] == 'vertical'):
                pos = max(min(trough_size, event.y - coords[1] - (thumbsize/2)), 0)
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                pos = max(min(trough_size, event.x - coords[0] - (thumbsize/2)), 0)
            
#           print('pos: %s' % pos)
            
            point = pos / trough_size
#           print('point: %s' % point)
            
            command = self._scroll_kwargs['command']
            if command:
                command('moveto', point)
            return 'break'
        
    def set(self, *args):
#       print('set: %s' % str(args))
        oldsize = (self._sb_end - self._sb_start) / 1
        
        self._sb_start = float(args[0])
        self._sb_end = float(args[1])
        
        size = (self._sb_end - self._sb_start) / 1
        
        width = self._width()
        height = self._height()
        
        if oldsize != size:
            self.delete(self.elements['thumb'])
            self.elements['thumb'] = None
        
        if (self._scroll_kwargs['orient'] == 'vertical'):
            thumbrange = height - width
            thumboffset = int(thumbrange * self._sb_start) + int(width/2)
        elif (self._scroll_kwargs['orient'] == 'horizontal'):
            thumbrange = width - height
            thumboffset = int(thumbrange * self._sb_start) + int(height/2)
        thumbsize = int(thumbrange * size)
        
        if not self.elements['thumb']: # create
            if (self._scroll_kwargs['orient'] == 'vertical'):
                rect = (0, thumboffset,width, thumbsize+thumboffset)
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                rect = (thumboffset, 0, thumbsize+thumboffset, height)
            fill = self._get_colour('thumbcolor')
            outline = self._get_colour('thumboutline')
            if (self._scroll_kwargs['thumbtype'] == 'round'):
                self.elements['thumb'] = self.create_oval(rect, fill=fill, outline=outline, tag='thumb')
            elif (self._scroll_kwargs['thumbtype'] == 'rectangle'):
                self.elements['thumb'] = self.create_rectangle(rect, fill=fill, outline=outline, tag='thumb')
        else: # move
            coords = self.coords(self.elements['thumb'])
            if (self._scroll_kwargs['orient'] == 'vertical'):
                if (thumboffset != coords[1]):
                    self.move(self.elements['thumb'], 0, thumboffset-coords[1])
            elif (self._scroll_kwargs['orient'] == 'horizontal'):
                if (thumboffset != coords[1]):
                    self.move(self.elements['thumb'], thumboffset-coords[0], 0)
        return 'break'
        
if __name__ == '__main__':
    root = tk.Tk()
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(3, weight=1)
    
    lb = tk.Listbox(root)
    lb.grid(column=1, row=1, sticky="nesw")
    for num in range(0,100):
        lb.insert('end', str(num)*100)
        
    sby1 = MyScrollbar(root, width=50, command=lb.yview)
    sby1.grid(column=2, row=1, sticky="nesw")
    
    sby2 = MyScrollbar(root, width=50, command=lb.yview, buttontype='square', thumbtype='round')
    sby2.grid(column=4, row=1, sticky="nesw")
    
    sbx1 = MyScrollbar(root, height=50, command=lb.xview, orient='horizontal', buttoncolor='red', thumbcolor='orange', troughcolor='green')
    sbx1.grid(column=1, row=2, sticky="nesw")
    
    sbx2 = MyScrollbar(root, height=50, command=lb.xview, orient='horizontal', thumbtype='round')
    sbx2.grid(column=1, row=4, sticky="nesw")
    
    def x_set(*args):
        sbx1.set(*args)
        sbx2.set(*args)
        
    def y_set(*args):
        sby1.set(*args)
        sby2.set(*args)
    
    lb.configure(yscrollcommand=y_set, xscrollcommand=x_set)
    root.mainloop()