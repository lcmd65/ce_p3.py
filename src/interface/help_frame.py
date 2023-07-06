from tkinter import *
from tkinter import messagebox
from functools import partial 
import meta.external_var
import email

class HelpFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventClickButtonOK(self, text):
        try:
            content = text.get()
            email_content = email("dat.lemindast@gmail.com", content)
            email_content.send()
        except Exception as e:
            messagebox.showerror(message = e)
    
    def initUI(self):
        self.parent.title("Help")
        self.pack(expand=True, fill = BOTH)
        
        label_privacy = Label(self.parent, text ="First Solar privacy @2022", font =("Roboto",14,"bold"))
        label_privacy.pack(fill= X, side = LEFT)
        
        label_body = Label(self)
        label_body.pack(fill = BOTH)
        
        frame_body = [None for _ in range(3)]
        for index in range(3):
            frame_body[index] = Frame(label_body)
            frame_body[index].pack(fill = X)
        
        text1 = Text(frame_body[0], height= 5)
        text1.insert(0, "please send email to dat.lemindast@gmail.com")
        text1.pack(fill= X, side =LEFT)
        
        text2 = Text(frame_body[1])
        text2.pack(fill = BOTH)
        
        button = Button(frame_body[2], text = "OK", width= 10, command = partial(self.eventClickButtonOK, text2))
        button.pack(side = RIGHT)