from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from interface.laser_frame import LaserFrame
from interface.forgot_frame import ForgotFrame
from functools import partial
import backend.function.user_authen as user_authen
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
            messagebox.showinfo(message = "Wrong password or username")
        else:
            meta.external_var.root.destroy()
            meta.external_var.root = Tk()
            meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image.png'))
            meta.external_var.root.geometry('1200x600+200+200') 
            app = LaserFrame(meta.external_var.root)
            meta.external_var.root.mainloop()
        
    def eventClickButtonForgotPass(self):
        meta.external_var.root_temp = Toplevel()
        meta.external_var.root_temp.geometry('600x400+200+200') 
        app = ForgotFrame(meta.external_var.root_temp)
        meta.external_var.root_temp.mainloop()
        
    ## init ui on frame
    def initUI(self):
        self.parent.title("Copy Exactly Laser")
        self.pack(fill =BOTH, expand = True)
        
        label_privacy = Label(self, text = "First Solar privacy @2022", font=("Roboto", 12, "bold"))
        label_privacy.pack(side = BOTTOM, fill = BOTH)
        
        label = Label(self, i= meta.external_var.bg)
        label.pack(fill = BOTH, side = BOTTOM)
        
        tab_control = Notebook(label,  height= 400, width= 250)
        tab_control.pack(expand = False, anchor= "center", padx =400, pady = 300, ipadx = 10, ipady=75 )
        
        tab0 = Frame(tab_control, width= 100)
        tab0.pack(fill = X, side = TOP, padx=0,  pady=20)
        tab_control.add(tab0, padding= 5)
        
        
        frame6 = Frame(tab0)
        frame6.pack(fill =X,padx = 110, pady =10, side =TOP)
        frame7 = Frame(tab0)
        frame7.pack(fill =X,padx = 50, pady =10, side =TOP)
        
        frame5 = Frame(tab0)
        frame5.pack(fill =X, padx = 10, pady =20, side =BOTTOM)
        frame4 = Frame(tab0)
        frame4.pack(fill =X, padx = 10, side =BOTTOM)
        frame3 = Frame(tab0)
        frame3.pack(fill =X, padx = 10, side =BOTTOM)
        frame2 = Frame(tab0)
        frame2.pack(fill =X, padx = 10, side =BOTTOM)
        frame1 = Frame(tab0)
        frame1.pack(fill =X, padx = 10, side =BOTTOM)
        
        label_account = Label(frame1, text = "Username", font = ("Calibri", 11))
        label_account.pack(side = TOP, padx =5, pady =5)
        
        entry_account = Entry(frame2)
        entry_account.pack(fill = X , padx =5, pady =5)
        
        label_password = Label(frame3, text = "Password", font =("Calibri", 11))
        label_password.pack(side = TOP, padx =5, pady =5)
        
        entry_password = Entry(frame4)
        entry_password.pack(fill = X, padx = 5, pady = 5)
        entry_password.config(show="*")
        
        button_login = Button(frame5, text = "Sign In", command= partial(self.eventClickButtonLogin, entry_account, entry_password))
        button_login.pack(side = RIGHT, fill = BOTH, padx =5 ,pady =5)

        button_forgot = Button(frame5, text = "Forgot password", command = self.eventClickButtonForgotPass)
        button_forgot.pack(side = LEFT,fill = BOTH, padx= 5, pady =5) 
        
        label_logo = Label(frame6, i= meta.external_var.logo)
        label_logo.pack(fill = BOTH, side = TOP, anchor= "center")
        
        label_password = Label(frame7, text = "Login", font =("Calibri", 12, 'bold'))
        label_password.pack(side = TOP)
        
        
        
        
    