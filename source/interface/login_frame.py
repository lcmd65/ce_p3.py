from tkinter import *
from tkinter import PanedWindow, messagebox
from interface.main_frame import MainFrame
from interface.forgot_frame import ForgotFrame
import meta.external_var

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def connnectUserInfo(self):
        return
    
    def eventClickButtonLogin(self, entry_account, entry_password):
        meta.external_var.username = entry_account.get()
        meta.external_var.password = entry_password.get()
        
        if self.connnectUserInfo() == False:
            messagebox.show("wrong password or account")
        else:
            self.destroy
            meta.external_var.root = Tk()
            meta.external_var.root.geometry('1200x600+200+200') 
            app = MainFrame(meta.external_var.root)
            meta.external_var.root.mainloop()
        
    def evnetClickButtonForgotPass(self):
        return
        
    ## init ui on frame
    def initUI(self):
        
        self.parent.title = "Login"
        self.pack(fill =BOTH, expand = True)
        
        frame_login = Frame(self)
        frame_login.pack()
         
        panel_login = PanedWindow(frame_login)
        panel_login.pack(fill = BOTH, padx = 20, pady =20)
        
        label_login = Label(panel_login, text= "LOGIN")
        label_login.pack(side = TOP)
        
        label_account = Label(panel_login, text = "Username")
        label_account.pack(side = LEFT, padx =5, pady =5)
        
        entry_account = Entry(panel_login, width = 20)
        entry_account.pack(side = LEFT, padx =5, pady =5)
        
        label_password = Label(panel_login, text = "Password")
        label_password.pack(side = LEFT, padx =5, pady =5)
        
        entry_password = Entry(panel_login, widht = 20)
        entry_password.pack(side = LEFT, padx = 5, pady = 5)    
        
        button_login = Button(panel_login, text = "Signin", command= self.eventClickButtonLogin)
        button_login.pack(side = RIGHT, fill = BOTH, padx =5 ,pady =5)

        button_forgot = Button(panel_login, text = "forgot password", command = self.evnetClickButtonForgotPass)
        button_forgot.pack(side = TOP, padx= 5, pady =5) 
        
        
        
    