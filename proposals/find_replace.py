from tkinter import *
  
  
# to create a window  
root = Tk()  
  
# root window is the parent window  
fram = Frame(root)  
  
# Creating Label, Entry Box, Button  
# and packing them adding label to 
# search box  
Label(fram, text ='Find').pack(side = LEFT) 
  
# adding of single line text box  
edit = Entry(fram)  
  
# positioning of text box  
edit.pack(side = LEFT, fill = BOTH, expand = 1)  
  
# setting focus  
edit.focus_set()  
  
# adding of search button  
Find = Button(fram, text ='Find') 
Find.pack(side = LEFT) 
  
  
Label(fram, text = "Replace With ").pack(side = LEFT) 
  
edit2 = Entry(fram) 
edit2.pack(side = LEFT, fill = BOTH, expand = 1) 
edit2.focus_set() 
  
replace = Button(fram, text = 'FindNReplace') 
replace.pack(side = LEFT) 
  
fram.pack(side = TOP)  
  
# text box in root window  
text = Text(root)  
  
# text input area at index 1 in text window  
text.insert('1.0', '''Type your text here''')  
text.pack(side = BOTTOM)  
  
# function to search string in text  
def find():  
    # remove tag 'found' from index 1 to END  
    text.tag_remove('found', '1.0', END)  
      
    # returns to widget currently in focus  
    s = edit.get() 
      
    if (s):  
        idx = '1.0'
        while 1:  
            # searches for desried string from index 1  
            idx = text.search(s, idx, nocase = 1,  
                            stopindex = END) 
              
            if not idx: break
            # last index sum of current index and  
            # length of text  
            lastidx = '% s+% dc' % (idx, len(s)) 
  
            # overwrite 'Found' at idx  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx  
  
        # mark located string as red 
          
        text.tag_config('found', foreground ='red') 
    edit.focus_set() 
  
def findNreplace():  
    # remove tag 'found' from index 1 to END  
    text.tag_remove('found', '1.0', END)  
      
    # returns to widget currently in focus  
    s = edit.get() 
    r = edit2.get() 
      
    if (s and r):  
        idx = '1.0'
        while 1:  
            # searches for desried string from index 1  
            idx = text.search(s, idx, nocase = 1,  
                            stopindex = END) 
            print(idx) 
            if not idx: break
              
            # last index sum of current index and  
            # length of text  
            lastidx = '% s+% dc' % (idx, len(s)) 
  
            text.delete(idx, lastidx) 
            text.insert(idx, r) 
  
            lastidx = '% s+% dc' % (idx, len(r)) 
              
            # overwrite 'Found' at idx  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx  
  
        # mark located string as red 
        text.tag_config('found', foreground ='green', background = 'yellow') 
    edit.focus_set() 
                  
Find.config(command = find) 
replace.config(command = findNreplace) 
  
# mainloop function calls the endless  
# loop of the window, so the window will 
# wait for any user interaction till we 
# close it  
root.mainloop() 