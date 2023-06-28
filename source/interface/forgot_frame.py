import tkinter
import meta.external_var
from tkinter import *

class ForgotFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title = "Forgot Password"
        
        label = Label(self, i = meta.external_var.bg)
        
        