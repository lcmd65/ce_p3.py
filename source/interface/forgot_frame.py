import tkinter
from tkinter import *

class ForgotFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title = "Forgot Password"
        
        