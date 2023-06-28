from tkinter import *
from tkinter.ttk import *
from tkinter import PanedWindow, messagebox
from interface.main_frame import MainFrame
from interface.forgot_frame import ForgotFrame
from functools import partial
import backend.function.user_authen as user_authen
import backend.constrain
from PIL import Image, ImageTk
import meta.external_var

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def connnectUserInfo(self):
        
        if user_authen.authenticantionUser(meta.external_var.username, meta.external_var.password) == True:
            return True
        else:
            return False
    
    def eventClickButtonLogin(self, entry_account, entry_password):
        meta.external_var.username = entry_account.get()
        meta.external_var.password = entry_password.get()
        
        if self.connnectUserInfo() == False:
            messagebox.show("Wrong password or username")
        else:
            meta.external_var.root.destroy()
            meta.external_var.root = Tk()
            meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image.png'))
            meta.external_var.root.geometry('1200x600+200+200') 
            app = MainFrame(meta.external_var.root)
            meta.external_var.root.mainloop()
        
    def eventClickButtonForgotPass(self):
        meta.external_var.root_temp = Toplevel()
        meta.external_var.root_temp.geometry('1200x600+200+200') 
        app = ForgotFrame(meta.external_var.root)
        meta.external_var.root_temp.mainloop()
        return
        
    ## init ui on frame
    def initUI(self):
        
        self.parent.title("Copy Exactly Laser")
        self.pack(fill =BOTH, expand = True)
        
        label = Label(self, i= meta.external_var.bg)
        label.pack()
        
        tab_control = Notebook(label,  height= 300)
        tab_control.pack(expand = True, padx=450, pady= 225)
        
        tab0 = Frame(tab_control)
        tab0.pack(fill = X, side = TOP, padx=0,  pady=20)
        tab_control.add(tab0, text = "LOGIN")
        
        frame5 = Frame(tab0)
        frame5.pack(fill =X, pady =20, side =BOTTOM)
        frame4 = Frame(tab0)
        frame4.pack(fill =X, side =BOTTOM)
        frame3 = Frame(tab0)
        frame3.pack(fill =X, side =BOTTOM)
        frame2 = Frame(tab0)
        frame2.pack(fill =X, side =BOTTOM)
        frame1 = Frame(tab0)
        frame1.pack(fill =X, side =BOTTOM)
        
        label_account = Label(frame1, text = "Username")
        label_account.pack(side = TOP, padx =5, pady =5)
        
        entry_account = Entry(frame2)
        entry_account.pack(fill = X , padx =5, pady =5)
        
        label_password = Label(frame3, text = "Password")
        label_password.pack(side = TOP, padx =5, pady =5)
        
        entry_password = Entry(frame4)
        entry_password.pack(fill = X, padx = 5, pady = 5)    
        
        button_login = Button(frame5, text = "Sign In", command= partial(self.eventClickButtonLogin, entry_account, entry_password))
        button_login.pack(side = RIGHT, fill = BOTH, padx =5 ,pady =5)

        button_forgot = Button(frame5, text = "Forgot password", command = self.eventClickButtonForgotPass)
        button_forgot.pack(side = TOP, padx= 5, pady =5) 
        
        
        
        
    