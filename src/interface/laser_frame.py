import meta.external_var
import threading
import tksheet 
from tkinter import *
from tkinter import (
    Button,
    ttk,
    messagebox)
from interface.ui_func import sequence
from interface.loop_frame import LoopFrame
from interface.help_frame import HelpFrame
from functools import partial
from PIL import Image, ImageTk
import backend.function.database as database
import backend.function.compare as compare
import gc

## UI of Laser python CE P3
class LaserFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def processingCal(self, txt,type_check):
        database.processingConsistOfType(type_check)
        txt.insert('1.0', "process successful ")
    
    def eventStateCheckThread(self, txt,type_check):
        t1 = threading.Thread(target=self.eventStateCheck(txt, type_check), )
        t1.start()
        t1.join()
    
    def eventStateCheck(self, txt,type_check):
        try: self.processingCal(txt,type_check)
        except Exception as e: 
            messagebox.showinfo(title= "CE Message", message = e)
    
    def eventLoopProcessing(self, txt, type_check):
        if meta.external_var.state_in_root_temp == "run":
            self.eventStateCheckThread(txt, type_check)
        if meta.external_var.signal_loop == 1:
            meta.external_var.root.after(10000,sequence(partial(self.eventLoopProcessing,txt,type_check)))
            
    ## click for CE function loop checking
    def eventClickedFunctionAppSchedule(self, txt, type_check):
        meta.external_var.signal_loop = 1
        meta.external_var.root_temp= Tk()
        meta.external_var.root_temp.geometry("400x80+300+300")
        app_temp = LoopFrame(meta.external_var.root_temp)
        self.eventLoopProcessing(txt,type_check)
        meta.external_var.root_temp.mainloop()
    
    ## start a new thread to run schefule in app
    def eventClickedFunctionAppScheduleThread(self, txt, type_check):
        temp_1 = threading.Thread(target= self.eventClickedFunctionAppSchedule(txt, type_check), )
        temp_1.start()
        temp_1.join()
    
    # view function in sheet after run function CE compare 
    def eventViewData(self, txt, sheet, type_check):
        df = database.processingUnpush(type_check)
        sheet.set_sheet_data(data = df.values.tolist(),\
                            reset_col_positions = True,\
                            reset_row_positions = True,\
                            redraw = True,\
                            verify = False,\
                            reset_highlights = False)
        self.eventTriggerData(sheet)
    
    # trigger cell that have a same row machine data and ce data difference
    def eventTriggerData(self, sheet_temp):
        for index in range(sheet_temp.get_total_rows()):
            if compare.compareString(sheet_temp.get_cell_data(index, 3, return_copy = True), \
            sheet_temp.get_cell_data(index, 7,  return_copy = True), \
            sheet_temp.get_cell_data(index, 4,  return_copy = True)) == 0:
                sheet_temp.highlight_cells(row = index,\
                                            column = 7,\
                                            bg = "Red",\
                                            fg = None,\
                                            redraw = False,\
                                            overwrite = True)
    
    # exit function CE loop tracking
    def eventExitRoot(self):
        gc.collect()
        meta.external_var.state_in_root_temp = 'end'
        meta.external_var.signal_loop = 0
        meta.external_var.root_temp.destroy()
    
    # exit button ("EXIT") in button bar, function return to Login Frame 
    def eventClickExit(self):
        try:
            meta.external_var.root.destroy()
            from interface.login_frame import LoginFrame
            meta.external_var.root = Tk()
            meta.external_var.root.geometry('1200x1000+300+0') 
            meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image1.png').resize((1920, 1080)))
            meta.external_var.logo = ImageTk.PhotoImage(Image.open('data/images/logo.png').resize((34, 30)))
            app= LoginFrame(meta.external_var.root)
            meta.external_var.root.mainloop()
        except Exception as e:
            messagebox.showerror(message = e)
    
    # button Analyze in tab home
    def eventClickHome(self):
        try:
            database.processing()
        except Exception as e:
            messagebox.showerror(message = e)
    
    # button "HELP" in button bar
    def eventClickHelp(self):
        gc.collect()
        meta.external_var.root_temp = Toplevel()
        meta.external_var.root_temp.geometry('600x600+200+200') 
        app_help = HelpFrame(meta.external_var.root_temp)
        meta.external_var.root_temp.mainloop()
    
    # button Edit data in button bar
    def eventButtonClickEdit(self):
        if meta.external_var.roll == "A":
            from interface.login_frame import LoginFrameAccuracy 
            gc.collect()
            meta.external_var.root_temp = Toplevel()
            meta.external_var.root_temp.geometry('600x800+200+200') 
            app_edit = LoginFrameAccuracy(meta.external_var.root_temp)
            meta.external_var.root_temp.mainloop()
        else:
            messagebox.showinfo(title = "Security", message = "You are not authorized to perform this function")
    
    # function to help tranfer 1 , 2, 3 to char A, B, C
    def tranferString(self, key):
        if key == 1: return "A"
        elif key == 2: return "B"
        elif key == 3: return "C"
    
    def initUI(self):
        self.parent.title("CE LASER P3")
        self.pack(fill=BOTH, expand=True)
        
        self.label_root = Label(self, i= meta.external_var.bg, bg = None)
        self.label_root.pack()
        
        # button bar (consist of Exit, Edit, Help)
        self.button_bar = Frame(self.label_root, bg= None)
        self.button_bar.pack(side = TOP, fill = X)
        self.button_bars = [ None for _ in range(4)]
        for index, label_text, commands in zip(range(4), ["Exit", "File", "Edit", "Help"], [self.eventClickExit, None, self.eventButtonClickEdit, self.eventClickHelp]):
            self.button_bars[index] = Button(self.button_bar, text = label_text, width= 10, command= commands, bg= None, image=None)
            self.button_bars[index].config(bg= None, bd=0)
            self.button_bars[index].pack(side = LEFT, fill = BOTH)
        
        # Notebook include tab home, laser P3A to C
        self.notebook_control = ttk.Notebook(self.label_root)
        self.notebook_control.pack(expand= True, fill=BOTH, padx=5, pady= 20)
        
        # init tab control 
        self.tab_controls = [None for _ in range(4)]
        self.body_controls = [None for _ in range(4)]
        self.button_controls = [None for _ in range(4)]
        self.text_controls = [None for _ in range(4)]
        self.sheet_controls = [None for _ in range(4)]
        
        for index, label_text in zip(range(4), ['    HOME    ', '      P3A      ', '      P3B      ','      P3C      ']):
            self.tab_controls[index] = Frame(self.notebook_control)
            self.tab_controls[index].pack(side= LEFT, padx=0, pady=5)
            self.notebook_control.add(self.tab_controls[index], text = label_text)
            if index != 0: # except home tab
                self.body_controls[index] = [None for _ in range(3)]
                self.button_controls[index] =[None for _ in range(4)]
                for se_index in range(3):
                    self.body_controls[index][se_index] = Frame(self.tab_controls[index])
                    self.body_controls[index][se_index].pack(fill =X)
                
                # sheet view of each laser tab
                self.sheet_controls[index] = tksheet.Sheet(self.body_controls[index][2], data = [[]], height = 800, width = 1500)
                self.sheet_controls[index].pack(fill=BOTH, pady=10, padx=5, expand=True)
                self.sheet_controls[index].grid(row =20, column = 20, sticky="nswe")
                self.sheet_controls[index].enable_bindings()
                
                # text information view of each laser tab
                self.text_controls[index] =  Text(self.body_controls[index][1], bg ="#fcfcfc", height= 2)
                self.text_controls[index].pack(fill=BOTH, pady=0, padx=5, expand=True)
                
                # get type of machine data connect: A, B, C
                temp = self.tranferString(index)
                commands = [
                    partial(self.processingCal, self.text_controls[index], temp),
                    partial(self.eventViewData, self.text_controls[index], self.sheet_controls[index], temp),
                    partial(self.eventClickedFunctionAppScheduleThread, self.text_controls[index], temp),
                    partial(self.eventExitRoot),
                ]
                for se_index, button_text, command_ in zip(range(4), ["Machine CE Monitor", "View CE", "Auto Monitor", "End Auto"], commands):
                    self.button_controls[index][se_index] = Button(self.body_controls[index][0], text= button_text, width=25, command = command_)
                    self.button_controls[index][se_index].pack(side=LEFT, padx=5, pady=5)
            
            # tab home define
            elif index == 0:
                self.body_controls[index] = Frame(self.tab_controls[index])
                self.body_controls[index].pack(fill= X, padx=5 ,pady=5)
                self.button_controls[index] = Button(self.body_controls[index], text="Analyze", width=10, command = sequence(self.eventClickHome))
                self.button_controls[index].pack(side=LEFT, padx=5, pady=5)

