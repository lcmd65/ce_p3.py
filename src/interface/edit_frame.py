from tkinter import *
from tkinter import messagebox
from functools import partial
from interface.ui_func import stopAllProcesingToFile
import backend.const
import threading

class EditFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    # button OK Click in Frame
    def eventButtonChangeVariableClick(self, text, entries):
        try:
            for index in range(len(entries)):
                backend.const.jsonChange(text[index], entries[index].get())
            messagebox.showinfo(title="Message", message="Success")
        except Exception as e:
            print(e)
    
    # thread to prevent Deamon Thread error
    def eventButtonChangeVariableClickThread(self, text, entries):
        t1 = threading.Thread(target=self.eventButtonChangeVariableClick(text, entries), )
        t1.start()
        t1.join()
        
    def initUI(self):
        self.parent.title("EDIT SYSTEM PATH")
        self.pack(fill = BOTH, expand= True)
        
        self.label_privacy = Label(self, text = "First Solar privacy @2022", font=("Roboto", 12, "bold"))
        self.label_privacy.pack(side = BOTTOM, fill = BOTH)
        
        # body frame
        self.frame_main = [None for _ in range(3)]
        for index in range(3):
            self.frame_main[index] = Frame(self)
            self.frame_main[index].pack(fill = BOTH, padx = 20,  pady = 20)
            
        # frame config label
        self.label_info = Label(self.frame_main[0], text = "Path & Environment variable Configuration", font = ("Roboto", 14, "bold"))
        self.label_info.pack(side= LEFT)
        
        # frame 2 (body frame)
        self.panel_button = PanedWindow(self.frame_main[1], orient="vertical")
        self.panel_button.pack(fill = X)
        
        # text label view of parameter
        text_label = ["DRIVER",\
                    "HOST",\
                    "PORT",\
                    "USER",\
                    "PASSWORD",\
                    "DB_GET",\
                    "DB_PUSH"]
        
        self.labels = [None for _ in range(7) ]
        self.entries = [None for _ in range(7) ]
        self.frames = [None for _ in range(7) ]
        
        for label, index in zip(text_label, range(len(text_label))):
            self.frames[index] = Frame(self.panel_button)
            self.labels[index] = Label(self.frames[index], text = label)
            self.entries[index] = Entry(self.frames[index])
            self.entries[index].insert(0, backend.const.jsonConst()[label])
            
            self.labels[index].pack(side = LEFT, fill = X)
            self.entries[index].pack(side = TOP, fill = X)
            self.frames[index].pack(side =TOP, fill = X, pady =5)
        
        self.frame_main[2].pack(side = BOTTOM)
        self.button1 = Button(self.frame_main[2], text = "OK", width= 20, command = partial(self.eventButtonChangeVariableClickThread, text_label, self.entries))
        self.button1.pack(side = RIGHT, pady = 20)
