import meta.external_var
import gc
import keyboard
import mouse
import time
from tkinter import Tk
from interface.login_frame import LoginFrame
from PIL import Image, ImageTk

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def getTimeSinceLastMouseEvent():
    now = time.time()
    timestamp = mouse.get_last_mouse_event_timestamp()
    if timestamp is not None:
        return now - timestamp
    else:
        return None

def getTimeSinceLastKeyboardEvent():
    now = time.time()
    timestamp = keyboard.get_last_keyboard_event_timestamp()
    if timestamp is not None:
        return now - timestamp
    else:
        return None

def eventCheckLoginStatus():
    if meta.external_var.root != None:
        if meta.external_var.login_status == False:
            meta.external_var.root.destroy()
            meta.external_var.root_temp.destroy()
            gc.colect()
        else: pass
        meta.external_var.root.after(1000,sequence(eventCheckLoginStatus()))

def eventCheckOut():
    if meta.external_var.root != None:
        if getTimeSinceLastKeyboardEvent >=100000 and getTimeSinceLastMouseEvent >= 100000:
            meta.external_var.login_status = False
        meta.external_var.root.after(1000,sequence(eventCheckOut()))

def main():
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x1000+300+0') 
    meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image1.png').resize((1920, 1080)))
    meta.external_var.logo = ImageTk.PhotoImage(Image.open('data/images/logo.png').resize((34, 30)))
    app_login = LoginFrame(meta.external_var.root)
    meta.external_var.root.mainloop()
    try:
        sequence(eventCheckLoginStatus(), eventCheckOut())
    except Exception as e :
        print(e)

if __name__ == "__main__" :
    main()