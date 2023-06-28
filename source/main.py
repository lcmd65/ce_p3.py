import meta.external_var
from tkinter import *
from interface.login_frame import LoginFrame
from PIL import Image, ImageTk

if __name__ == "__main__" :
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x800+100+50') 
    meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image.png'))
    app= LoginFrame(meta.external_var.root)
    meta.external_var.root.mainloop()