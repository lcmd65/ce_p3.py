from tkinter import *
from interface.ui_func import sequence
import meta.external_var

class LoopFrame(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventRunRootTemp(self):
        meta.external_var.state_in_root_temp = 'run'
        meta.external_var.signal_loop = 1
        
    def eventExitRootTemp(self):
        meta.external_var.state_in_root_temp = 'end'
        meta.external_var.signal_loop = 0
        self.destroy
    
    def initUI(self):
        self.parent.title("CE LASER P3 AUTO RUNNING")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X)
        frame2 = Frame(self)
        frame2.pack(fill= BOTH)
        
        Button1 = Button(frame1, text ="Run",width =15, command = self.eventRunRootTemp)
        Button1.pack(side = BOTTOM, padx =5, pady=5)
        
        Button2 = Button(frame2, text="End", width =5, command = sequence(self.eventExitRootTemp, exit))
        Button2.pack(side = RIGHT, padx=5, pady =5)