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
        
    def eventButtonChangeVariableClick(self, text, entries):
        try:
            for index in range(len(entries)):
                backend.const.jsonChange(text[index], entries[index].get())
        except Exception as e:
            print(e)
        messagebox.showinfo(title="Message", message="Success")
    
    def eventButtonChangeVariableClickThread(self, text, entries):
        t1 = threading.Thread(target=self.eventButtonChangeVariableClick(text, entries), )
        t1.start()
        t1.join()
        
    def initUI(self):
        self.parent.title("EDIT SYSTEM PATH")
        self.pack(fill = BOTH, expand= True)
        
        label_privacy = Label(self, text = "First Solar privacy @2022", font=("Roboto", 12, "bold"))
        label_privacy.pack(side = BOTTOM, fill = BOTH)
        # body frame
        frame_main = [None for _ in range(3)]
        for index in range(3):
            frame_main[index] = Frame(self)
            frame_main[index].pack(fill = BOTH, padx = 20,  pady = 20)
            
        # frame 1
        label1 = Label(frame_main[0], text = "Path & Environment variable Configuration", font = ("Roboto", 14, "bold"))
        label1.pack(side= LEFT)
        
        # frame 2
        panel_button = PanedWindow(frame_main[1], orient="vertical")
        panel_button.pack(fill = X)
        
        text_label = ["DRIVER",\
            "HOST",\
            "PORT",\
            "USER",\
            "PASSWORD",\
            "DB_GET",\
            "DB_PUSH"]
        
        labels = [None for _ in range(7) ]
        entries = [None for _ in range(7) ]
        frames = [None for _ in range(7) ]
        
        for label, index in zip(text_label, range(len(text_label))):
            frames[index] = Frame(panel_button)
            labels[index] = Label(frames[index], text = label)
            entries[index] = Entry(frames[index])
            entries[index].insert(0, backend.const.jsonConst()[label])
            
            labels[index].pack(side = LEFT, fill = X)
            entries[index].pack(side = TOP, fill = X)
            frames[index].pack(side =TOP, fill = X, pady =5)
        
        frame_main[2].pack(side = BOTTOM)
        button1 = Button(frame_main[2], text = "OK", width= 20, command = partial(self.eventButtonChangeVariableClickThread, text_label, entries))
        button1.pack(side = RIGHT, pady = 20)
