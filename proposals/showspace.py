# Display invisible characters space, tab and newline

text = "\tMary had a little lamb\n\tWhose fleece was white as snow.\n\n"\
"\nCommands:\t\tCtrl-w toggles the display.\n"\
"\t\tCtrl-q quits the programme.\n\n"\
"I ported the above Tcl script to Python 3.6 and its work all right, except that the substitution character for space (0xb7) prevents word wrapping.\n"\
"I tried adding a zero-width space character (ZWSP - 0x200b in the commented-out lines), but tkinker doesn't treat it as an easy break character."

from tkinter import *
import sys

class GuiContainer:
    def __init__(self):
        self.root = None
        self.frame = None
        self.showinvis = False
    def initBuildWindow(self):
        self.root = Tk()
        self.root.geometry("650x450+50+50")
        self.root.title("{0} GUI".format(sys.argv[0]))
        self.frame = Frame(self.root, name="mframe")
        self.frame.pack(fill=BOTH, expand=1)
        self.tainput = Text(self.frame, wrap=WORD, bd=0, height=17, undo=True)
        self.tainput.pack(fill=BOTH, expand=1)
        self.tainput.insert(INSERT, text)
        self.tainput.bind("<Key-space>",lambda event: self.onKeyWhitechar(self.tainput, ' '))
        self.tainput.bind("<Key-Tab>", lambda event: self.onKeyWhitechar(self.tainput,'\t'))
        self.tainput.bind("<Return>", lambda event: self.onKeyWhitechar(self.tainput,'\n'))
        self.tainput.bind("<Control-w>", lambda event: self.onShowInvisible())
        self.tainput.bind("<Control-q>", lambda event: self.root.quit())
        self.tainput.focus_force()
        self.tainput.mark_set(INSERT, END)

    def onKeyWhitechar(self, char, event=None):
        convstr = ''
        if self.showinvis:
            if char == ' ':      convstr = '·'      # 0x20 -> 0xb7
            #if char == ' ':      convstr = '·'+chr(0x200b)
            elif char == '\t':   convstr = '»\t'
            elif char == '\n':   convstr = '¶\n'
            self.tainput.insert(INSERT, convstr)
    def convertWhitechars(self):
        if self.showinvis:
            convlst = [[' ','·'], ['\t','»\t'], ['\n','¶\n']]
            #convlst = [[' ','·'+chr(0x200b)], ['\t','»\t'], ['\n','¶\n']]
        else:
            convlst = [['·',' '], ['»\t','\t'], ['¶\n','\n']]
            #convlst = [['·'+chr(0x200b),' '], ['»\t','\t'], ['¶\n','\n']]
        for i in range(len(convlst)):
            res = True
            char = convlst[i][0]; subchar = convlst[i][1]
            while res:
                res = self.replace(char, subchar)
    def replace(self, char, subchar):
        where = '1.0'; past_subchar = '1.0'
        while where:
            where = self.tainput.search(char, past_subchar, END+'-1c')
            past_subchar= '{}+{}c'.format(where, len(subchar));
            past_char = '{}+{}c'.format(where, len(char));
            if where:
                self.tainput.delete(where, past_char)
                self.tainput.insert(where, subchar)
            else:
                return False
    def onShowInvisible(self):
        self.showinvis = not self.showinvis
        self.convertWhitechars()

def main():
    guiCO = GuiContainer()
    guiCO.initBuildWindow()
    guiCO.root.mainloop()

if __name__ == "__main__":
    main()