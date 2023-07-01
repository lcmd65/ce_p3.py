
import meta.external_var
import threading
import tksheet 
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from interface.ui_func import sequence
from interface.loop_frame import LoopFrame
from interface.edit_frame import EditFrame
from functools import partial
from PIL import Image, ImageTk
import backend.function.database as database
import backend.function.compare as compare



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
        except: messagebox.showinfo(title= "CE Message", message ="Error in connect")
            
    def eventLoopProcessing(self, txt, type_check):
        if meta.external_var.state_in_root_temp == "run":
            self.eventStateCheckThread(txt, type_check)
        if meta.external_var.signal_loop == 1:
            meta.external_var.root.after(10000,sequence(partial(self.eventLoopProcessing,txt,type_check)))
    
    def eventClickedFunctionAppSchedule(self, txt, type_check):
        meta.external_var.signal_loop = 1
        root_temp= Tk()
        root_temp.geometry("400x80+300+300")
        app_temp = LoopFrame(root_temp)
        self.eventLoopProcessing(txt,type_check)
        root_temp.mainloop()
    
    ##start a new thread to run schefule in app
    def eventClickedFunctionAppScheduleThread(self, txt, type_check):
        temp_1 = threading.Thread(target= self.eventClickedFunctionAppSchedule(txt, type_check), )
        temp_1.start()
        temp_1.join()

    def eventViewData(self, txt, sheet, type_check):
        df = database.processingUnpush(type_check)
        sheet.set_sheet_data(data = df.values.tolist(),\
                    reset_col_positions = True,\
                    reset_row_positions = True,\
                    redraw = True,\
                    verify = False,\
                    reset_highlights = False)
        self.eventTriggerData(sheet)

    def eventTriggerData(self, sheet_temp):
        for i in range(sheet_temp.get_total_rows()):
            if compare.compareString(sheet_temp.get_cell_data(i, 3, return_copy = True), \
            sheet_temp.get_cell_data(i, 7,  return_copy = True), \
            sheet_temp.get_cell_data(i, 4,  return_copy = True)) == 0:
                sheet_temp.highlight_cells(row = i,\
                column = 7,\
                bg = "Red",\
                fg = None,\
                redraw = False,\
                overwrite = True)
    
    def eventExitRoot(self):
        meta.external_var.state_in_root_temp = 'end'
        meta.external_var.signal_loop = 0
                
    def eventClickExit(self):
        from interface.login_frame import LoginFrame
        meta.external_var.root = Tk()
        meta.external_var.root.geometry('1200x1000+300+0') 
        meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image1.png').resize((1920, 1080)))
        meta.external_var.logo = ImageTk.PhotoImage(Image.open('data/images/logo.png').resize((34, 30)))
        app= LoginFrame(meta.external_var.root)
        meta.external_var.root.mainloop()
    
    def eventClickHome(self):
        return
    
    def eventButtonClickEdit(self):
        meta.external_var.root_temp = Toplevel(meta.external_var.root)
        meta.external_var.root_temp.geometry('600x800+200+200') 
        app = EditFrame(meta.external_var.root_temp)
        meta.external_var.root_temp.mainloop()
    
    def initUI(self):
        self.parent.title("CE LASER P3")
        self.pack(fill=BOTH, expand=True)
        
        label = Label(self, i= meta.external_var.bg)
        label.pack()

        button_bar = Frame(label)
        button_bar.pack(side = TOP, fill = BOTH)
        
        button_bar0 = Button(button_bar, text= "Exit", width= 10 ,background = None, command= self.eventClickExit)
        button_bar0.pack(side = LEFT)
        button_bar1 = Button(button_bar, text= "File", width= 10 ,background = None)
        button_bar1.pack(side = LEFT)
        button_bar2 = Button(button_bar, text= "Edit", width= 10, background= None, command= self.eventButtonClickEdit)
        button_bar2.pack(side = LEFT)
        button_bar3 = Button(button_bar, text= "Help", width= 10, background = None)
        button_bar3.pack(side = LEFT)
        
        # Tab
        tab_control = Notebook(label)
        tab_control.pack(expand= True, fill=BOTH, padx=40, pady= 0)
        
        tab0 = Frame(tab_control)
        tab0.pack(side= LEFT, padx=0, pady=5)
        tab1 = Frame(tab_control)
        tab1.pack(side= LEFT, padx=0, pady=5)
        tab2 = Frame(tab_control)
        tab2.pack(side= LEFT, padx=0, pady=5)
        tab3 = Frame(tab_control)
        tab3.pack(side = LEFT, padx=0, pady=5)
        
        tab_control.add(tab0, text='HOME')
        tab_control.add(tab1, text='P3A')
        tab_control.add(tab2, text='P3B')
        tab_control.add(tab3, text='P3C')
        
        canvas1 = Canvas(tab0)
        canvas1.pack(fill = BOTH, expand= 1)
        canvas1.create_image( 0, 0,  anchor = "nw")
        
        # HOME
        frame_tab0_1 = Frame(canvas1)
        frame_tab0_1.pack(fill= X, padx=5 ,pady=5)
        
        Button_tab0_0 = Button(frame_tab0_1, text="Analyze", width=10, command = sequence(self.eventClickHome))
        Button_tab0_0.pack(side=LEFT, padx=5, pady=5)
        
        # P3A
        frame1a = Frame(tab1)
        frame1a.pack(fill=X)
        frame2a = Frame(tab1)
        frame2a.pack(fill=X)
        frame3a = Frame(tab1)
        frame3a.pack(side= LEFT, fill=Y, pady=5, padx =5)
        
        sheet1 =tksheet.Sheet(frame3a, data = [[]], height = 800, width = 1500)
        sheet1.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet1.grid(row =20, column = 20,sticky="nswe")
        sheet1.enable_bindings()
        
        txt = Text(frame2a, bg ="#fcfcfc", height= 2)
        txt.pack(fill=BOTH, pady=0, padx=5, expand=True)
    
        Button_tab1_1 = Button(frame1a, text="Laser P3 Tracking", width=25, command = sequence(partial(self.processingCal, txt, "A")))
        Button_tab1_1.pack(side=LEFT, padx=5, pady=5)
        Button_tab1_2 = Button(frame1a, text="End Auto", width=25, command = sequence(self.eventExitRoot))
        Button_tab1_2.pack(side=LEFT, padx=5, pady=5)
        Button_tab1_3 = Button(frame1a, text="Auto", width =25,  command = sequence(partial(self.eventClickedFunctionAppScheduleThread, txt, "A")))
        Button_tab1_3.pack(side=LEFT, padx=5, pady=5)
        Button_tab1_4 = Button(frame1a, text="View", width =25, command= partial(self.eventViewData,txt,sheet1, "A"))
        Button_tab1_4.pack(side=LEFT, padx=5, pady=5)
        
        # P3B
        frame1b = Frame(tab2)
        frame1b.pack(fill=X)
        frame2b = Frame(tab2)
        frame2b.pack(fill=X)
        frame3b = Frame(tab2)
        frame3b.pack(side= LEFT, fill=Y, pady=5, padx =5)
        
        sheet2 =tksheet.Sheet(frame3b, data = [[]], height = 800, width = 1500)
        sheet2.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet2.grid(row =20, column = 20,sticky="nswe")
        sheet2.enable_bindings()
        
        text_b = Text(frame2b,  height= 2)
        text_b.pack(fill = X)
        Button_tab2_1 = Button(frame1b, text="Laser P3 Tracking", width =25, command = partial(self.processingCal,text_b, "B"))
        Button_tab2_1.pack(side =LEFT, padx=5, pady=5)
        Button_tab2_2 = Button(frame1b, text="End Auto", width =25, command= self.eventExitRoot)
        Button_tab2_2.pack(side=LEFT, padx=5, pady=5)
        Button_tab2_3 = Button(frame1b, text="Auto", width =25,  command = sequence(partial(self.eventClickedFunctionAppScheduleThread, text_b, "B")))
        Button_tab2_3.pack(side=LEFT, padx=5, pady=5)
        Button_tab2_4 = Button(frame1b, text="View", width =25, command= partial(self.eventViewData, text_b, sheet2, "B"))
        Button_tab2_4.pack(side =LEFT, padx=5, pady=5)
        # P3C
        
        frame1c = Frame(tab3)
        frame1c.pack(fill=X)
        frame2c = Frame(tab3)
        frame2c.pack(fill=X)
        frame3c = Frame(tab3)
        frame3c.pack(side= LEFT, fill=Y, pady=5, padx =5)
        
        sheet3 =tksheet.Sheet(frame3c, data = [[]], height = 800, width = 1500)
        sheet3.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet3.grid(row =20, column = 20,sticky="nswe")
        sheet3.enable_bindings()
        
        text_c = Text(frame2c,  height= 2)
        text_c.pack(fill =X)
        
        Button_tab3_1 = Button(frame1c, text="Laser P3 Tracking", width =25, command = partial(self.processingCal,text_c, "C"))
        Button_tab3_1.pack(side =LEFT, padx=5, pady=5)
        Button_tab3_2 = Button(frame1c, text="End Auto", width =25, command = self.eventExitRoot)
        Button_tab3_2.pack(side=LEFT, padx=5, pady=5)
        Button_tab3_3 = Button(frame1c, text="Auto", width =25,  command = sequence(partial(self.eventClickedFunctionAppScheduleThread, text_c, "C")))
        Button_tab3_3.pack(side=LEFT, padx=5, pady=5)
        Button_tab3_4 = Button(frame1c, text="View", width =25, command= partial(self.eventViewData,text_c, sheet3, "C"))
        Button_tab3_4.pack(side =LEFT, padx=5, pady=5)
