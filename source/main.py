import meta.external_var
from tkinter import Tk
from interface.login_frame import LoginFrame
from interface import *
from PIL import Image, ImageTk
import pdb
def main():
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x1000+300+0') 
    meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image1.png').resize((1920, 1080)))
    meta.external_var.logo = ImageTk.PhotoImage(Image.open('data/images/logo.png').resize((34, 30)))
    app= LoginFrame(meta.external_var.root)
    meta.external_var.root.mainloop()

if __name__ == "__main__" :
    main()
    pdb.set_trace()