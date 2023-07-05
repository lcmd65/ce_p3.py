from tkinter import *
from tkinter import messagebox
from functools import partial
import backend.function.user_authen
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
            df = backend.function.user_authen.dataframeUSER()
            for index in range(df.shape[0]):
                if df.loc[index, 1] == account_str and df.loc[index, 2] == email_str:
                    try:
                        backend.function.user_authen.changePass(account_str, email_str, newpass_str)
                        messagebox.showinfo(message="Password changed")
                        meta.external_var.root_temp.destroy()
                    except Exception as e:
                        messagebox.showerror(message= e)
                    return
            messagebox.showinfo(message="Error Information")
            
    def initUI(self):
        self.parent.title = "Forgot Password"
        self.pack(fill=BOTH, expand=True)
        
        frame_main = Frame(self)
        frame_main.pack(side = TOP, padx = 25, pady =50)
        
        frame1 = Frame(frame_main)
        frame1.pack(fill = X, padx = 5, pady = 5)
        frame2 = Frame(frame_main)
        frame2.pack(fill = X, padx= 5, pady =5)
        frame3 = Frame(frame_main)
        frame3.pack(fill =X, padx =5, pady =5)
        frame4 = Frame(frame_main)
        frame4.pack(fill =X, padx =5, pady =5)
        frame5 = Frame(frame_main)
        frame5.pack(side = BOTTOM, expand= True)
        
        
        label_account = Label(frame1, text = "Username")
        label_account.pack(side = LEFT)
        
        entry_account = Entry(frame1, width= 40)
        entry_account.pack(side = RIGHT, padx = 10)
        
        label_email = Label(frame2, text = "Email")
        label_email.pack(side = LEFT)
        
        entry_email = Entry(frame2, width = 40)
        entry_email.pack(side = RIGHT, padx =10)
        
        label_new_password = Label(frame3, text = "New Password")
        label_new_password .pack(side = LEFT)
        
        entry_new_password  = Entry(frame3, width = 40)
        entry_new_password.pack(side = RIGHT, padx =10)
        entry_new_password.config(show="*")
        
        label_confirm_password = Label(frame4, text = "Confirm New Password")
        label_confirm_password .pack(side = LEFT)
        
        entry_confirm_password  = Entry(frame4, width = 40)
        entry_confirm_password.pack(side = RIGHT, padx =10)
        entry_confirm_password.config(show="*")
        
        button1 = Button(frame5, text = "OK", width = 15, command= partial(self.eventClickChangePassword, entry_account, entry_email, entry_new_password, entry_confirm_password))
        button1.pack(side = RIGHT)

        
        
        
        
        
        
         