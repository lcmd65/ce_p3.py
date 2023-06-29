from tkinter import *
from tkinter import messagebox
from functools import partial

class EditFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("EDIT SYSTEM PATH")
        self.pack(fill = BOTH, expand= True)
        
        button1 = Button(self.parent, text ="File", width=10)
        button1.pack(side = TOP, fill = BOTH)

if __name__ == "__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app = EditFrame(root)
    root.mainloop()
    