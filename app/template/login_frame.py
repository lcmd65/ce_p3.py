from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from template.forgot_frame import ForgotFrame
from template.edit_frame import EditFrame
from functools import partial
import function.event.user_authen as user_authen
from PIL import Image, ImageTk
import meta.external_var


class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventClickButtonLogin(self, entry_account, entry_password):
        meta.external_var.username = entry_account.get()
        meta.external_var.password = entry_password.get()
        try:
            if user_authen.authenticantionUser(meta.external_var.username, meta.external_var.password) == False:
                messagebox.showinfo(message = "Wrong password or username")
            elif user_authen.authenticantionUser(meta.external_var.username, meta.external_var.password) == True:
                from template.laser_frame import LaserFrame
                meta.external_var.root.destroy()
                meta.external_var.root = Tk()
                meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image.png'))
                meta.external_var.root.geometry('1200x1000+300+0') 
                app_laser = LaserFrame(meta.external_var.root)
                meta.external_var.root.mainloop()  
            else:
                pass          
        except Exception as e:
            messagebox.showinfo(title= "Error", message = e)
        
    def eventClickButtonForgotPass(self):
        meta.external_var.root_temp = Toplevel()
        meta.external_var.root_temp.geometry('600x400+200+200') 
        app_forgot = ForgotFrame(meta.external_var.root_temp)
        meta.external_var.root_temp.mainloop()
        
    ## init ui on frame
    def initUI(self):
        self.parent.title("Copy Exactly Laser")
        self.pack(fill =BOTH, expand = True)
        
        self.label_privacy = Label(self, text = "First Solar privacy @2022", font=("Roboto", 12, "bold"))
        self.label_privacy.pack(side = BOTTOM, fill = BOTH)
        
        self.label = Label(self, i= meta.external_var.bg)
        self.label.pack(fill = BOTH, side = BOTTOM)
        
        self.tab_control = Notebook(self.label,  height= 400, width= 250)
        self.tab_control.pack(expand = False, anchor= "center", padx =400, pady = 175, ipadx = 10, ipady=100 )
        noteStyle = Style()
        noteStyle.layout("TNotebook.Tab", [])
        
        self.tab_panel = Frame(self.tab_control, width= 100)
        self.tab_panel.pack(fill = X, side = TOP, padx=0,  pady=20)
        self.tab_control.add(self.tab_panel, padding= 5)
        
        self.frame_login = [None for _ in range(7)]
        for index in range(7):
            self.frame_login[index] = Frame(self.tab_panel)
            self.frame_login[index].pack(fill =X, padx = 10, side =BOTTOM)
        self.frame_login[0].pack(pady = 20)
        self.frame_login[5].pack(fill =X, padx = 110, pady =10, side =TOP)
        self.frame_login[6].pack(fill =X, padx = 50, pady =10, side =TOP)
        
        # account widget
        self.label_account = Label(self.frame_login[4], text = "Username", font = ("Calibri", 11))
        self.label_account.pack(side = TOP, padx =5, pady =5)
       
        self.entry_account = Entry(self.frame_login[3])
        self.entry_account.pack(fill = X , padx =5, pady =5)
        
        # password widget
        self.label_password = Label(self.frame_login[2], text = "Password", font =("Calibri", 11))
        self.label_password.pack(side = TOP, padx =5, pady =5)
        
        self.entry_password = Entry(self.frame_login[1])
        self.entry_password.pack(fill = X, padx = 5, pady = 5)
        self.entry_password.config(show="*")
        
        self.button_login = Button(self.frame_login[0], text = "Sign In", command= partial(self.eventClickButtonLogin, self.entry_account, self.entry_password))
        self.button_login.pack(side = RIGHT, fill = BOTH, padx =5 ,pady =5)

        self.button_forgot = Button(self.frame_login[0], text = "Forgot password", command = self.eventClickButtonForgotPass)
        self.button_forgot.pack(side = LEFT,fill = BOTH, padx= 5, pady =5) 
        
        self.label_logo = Label(self.frame_login[5], i= meta.external_var.logo)
        self.label_logo.pack(fill = BOTH, side = TOP, anchor= "center")
        
        self.label_password = Label(self.frame_login[6], text = "Login", font =("Calibri", 12, 'bold'))
        self.label_password.pack(side = TOP)

class LoginFrameAccuracy(LoginFrame):
    def __init__(self, parent):
        LoginFrame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def eventClickButtonLogin(self, entry_account, entry_password):
        meta.external_var.username = entry_account.get()
        meta.external_var.password = entry_password.get()
        try:
            if user_authen.authenticantionUser(meta.external_var.username, meta.external_var.password) == False:
                messagebox.showinfo(message = "Wrong password or username")
            else:
                meta.external_var.root_temp.destroy()
                meta.external_var.root_temp = Toplevel()
                meta.external_var.root_temp.geometry('600x800+200+200') 
                app_edit = EditFrame(meta.external_var.root_temp)
                meta.external_var.root_temp.mainloop()
        except Exception as e:
            messagebox.showerror(message= e)
        
    def initUI(self):
        super().initUI()