import meta.external_var
from tkinter import *
from interface.login_frame import LoginFrame

if __name__ == "__main__" :
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x600+200+200') 
    app= LoginFrame(meta.external_var.root)
    meta.external_var.root.mainloop()