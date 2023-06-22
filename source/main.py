import meta.external_var
from tkinter import *
from backend.function.function_database import *
from backend.function.function_compare import *
from interface.main_frame import MainFrame

if __name__ == "__main__" :
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x600+200+200') 
    app= MainFrame(meta.external_var.root)
    meta.external_var.root.mainloop()