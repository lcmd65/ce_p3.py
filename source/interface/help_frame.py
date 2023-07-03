from tkinter import *
import meta.external_var

class HelpFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Help")
        self.pack(expand=True, fill = BOTH)
        
        label_privacy = Label(self.parent, text ="First Solar privacy @2022", font =("Roboto",14,"bold"))
        label_privacy.pack(fill= X, side = LEFT)
        label_body = Label(self, i = meta.external_var.bg)
        label_body.pack()
        
        frame_body = Frame(label_body)
        frame_body.pack(fill = X)
        
        text = Text(frame_body)
        text.insert(0, "please send email to dat.lemindast@gmail.com")
        text.pack(fill= X, side =LEFT)
        
        
        