from tkinter import *
from tkinter import messagebox
from functools import partial
import function.event.user_authen
import meta.external_var

class ForgotFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def eventClickChangePassword(self, account, email, newpass, confirm):
        account_str, email_str, newpass_str, confirm_str  = account.get(), email.get(), newpass.get(), confirm.get()
        if newpass_str != confirm_str:
            messagebox.showinfo(message= "Confirm pass does not match")
        else:
            df = function.event.user_authen.dataframeUSER()
            for index in range(df.shape[0]):
                if df.loc[index, 1] == account_str and df.loc[index, 2] == email_str:
                    try:
                        function.event.user_authen.changePass(account_str, email_str, newpass_str)
                        messagebox.showinfo(message="Password changed")
                        meta.external_var.root_temp.destroy()
                    except Exception as e:
                        messagebox.showerror(message= e)
                    return
            messagebox.showinfo(message="Error Information")
            
    def initUI(self):
        self.parent.title = "Forgot Password"
        self.pack(fill=BOTH, expand=True)
        
        self.frame_bg = Frame(self)
        self.frame_bg.pack(side = TOP, padx = 25, pady =50)
        
        self.frame_panel = [None for _ in range(5)]
        for index in range(5):
            self.frame_panel[index] = Frame(self.frame_bg)
            self.frame_panel[index].pack(fill = X, padx = 5, pady = 5)
        self.frame_panel[4].pack(side = BOTTOM, expand= True)
        
        self.label_account = Label(self.frame_panel[0], text = "Username")
        self.label_account.pack(side = LEFT)
        
        self.entry_account = Entry(self.frame_panel[0], width= 40)
        self.entry_account.pack(side = RIGHT, padx = 10)
        
        self.label_email = Label(self.frame_panel[1], text = "Email")
        self.label_email.pack(side = LEFT)
        
        self.entry_email = Entry(self.frame_panel[1], width = 40)
        self.entry_email.pack(side = RIGHT, padx =10)
        
        self.label_new_password = Label(self.frame_panel[2], text = "New Password")
        self.label_new_password .pack(side = LEFT)
        
        self.entry_new_password  = Entry(self.frame_panel[2], width = 40)
        self.entry_new_password.pack(side = RIGHT, padx =10)
        self.entry_new_password.config(show="*")
        
        self.label_confirm_password = Label(self.frame_panel[3], text = "Confirm New Password")
        self.label_confirm_password .pack(side = LEFT)
        
        self.entry_confirm_password  = Entry(self.frame_panel[3], width = 40)
        self.entry_confirm_password.pack(side = RIGHT, padx =10)
        self.entry_confirm_password.config(show="*")
        
        self.button1 = Button(self.frame_panel[4], text = "OK", width = 15, command= partial(self.eventClickChangePassword, self.entry_account, self.entry_email, self.entry_new_password, self.entry_confirm_password))
        self.button1.pack(side = RIGHT)
