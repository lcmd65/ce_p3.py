import meta.external_var
import threading
import tksheet 
from tkinter import *
from tkinter import (
    Menu,
    filedialog,
    ttk,
    messagebox)
from tkinter.ttk import Button
from template.ui_func import sequence
from template.loop_frame import LoopFrame
from template.help_frame import HelpFrame
from functools import partial
from PIL import Image, ImageTk
import function.event.database as database
import function.event.compare as compare
import gc
import os

## UI of Laser python CE P3
class LaserFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.nodes = dict()
        self.radio_value = IntVar()
        self.editor = []
        self.path = []
        self.information = []
        self.initUI()
        
    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=True)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))
                
    def processDirectory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open = False)
            self.nodes[oid] = abspath
            print(self.nodes[oid])
            if isdir:
                self.processDirectory(oid, abspath)
    
    def eventButtonClickChangeDataSource(self, tree):
        """
        Button click in data source tree
        """
        for i in tree.get_children():
            tree.delete(i)
        self.datasource_path = filedialog.askdirectory()
        abspath = os.path.abspath(self.datasource_path)
        root_node = tree.insert("", 'end', text = abspath, open = True)
        self.processDirectory(root_node, abspath)
    
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
    
    #view in home
    def eventViewDataHome(self, sheet, data):
        sheet.set_sheet_data(data = data.values.tolist(),\
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
    def eventButtonClickExit(self):
        try:
            meta.external_var.root.destroy()
            from template.login_frame import LoginFrame
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
    def eventButtonClickHelp(self):
        gc.collect()
        meta.external_var.root_temp = Toplevel()
        meta.external_var.root_temp.geometry('600x600+200+200') 
        app_help = HelpFrame(meta.external_var.root_temp)
        meta.external_var.root_temp.mainloop()
    
    # button Edit data in button bar
    def eventButtonClickEdit(self):
        if meta.external_var.roll == "A":
            from template.login_frame import LoginFrameAccuracy 
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
        
    def selectItem(self, tree, information_tab, editor_tab):
        node = tree.focus()
        abspath = self.nodes[str(node)]
        self.path.append(abspath)
        self.editor.append(abspath)
        editor_tab.insert("", 'end', text = str(abspath), open = True)
        for i in information_tab.get_children():
            information_tab.delete(i)
        information_tab.insert("", 'end', text= os.path.getsize(abspath), open = True)
        information_tab.insert("", 'end', text= os.path.getmtime(abspath), open = True)
        information_tab.insert("", 'end', text= os.path.getctime(abspath), open = True)
        
    def clearWorkspace(self, information_tab, editor_tab):
        for i in information_tab.get_children():
            information_tab.delete(i)
        for i in editor_tab.get_children():
            editor_tab.delete(i)
        self.editor.clear()
        self.information.clear()
        self.path.clear()
    
    def eventButtonClickProcessingHome(self, sheet_view, radio):
        type_ = self.tranferString(radio.get())
        df = database.processingConsistOfTypeAndFile(type_, self.path)
        self.eventViewDataHome(sheet_view, df)
        
        
    def initUI(self):
        self.parent.title("CE LASER P3")
        self.pack(fill=BOTH, expand=True)
        
        self.label_privacy = Label(self, text = "First Solar privacy @2022", font=("Roboto", 12, "bold"))
        self.label_privacy.pack(side = BOTTOM, fill = BOTH)
        
        self.label_root = Label(self, i= meta.external_var.bg, bg = None)
        self.label_root.pack()
        
        self.home_menu = Menu(self.parent)
        """
        File menu
        """
        file_menu = Menu(self.home_menu)
        file_menu.add_command(label="New", command = None)
        file_menu.add_command(label="Open", command = None)
        file_menu.add_separator()
        file_menu.add_command(label= "Exit", command = partial(self.eventButtonClickExit))
        
        """ 
        Edit menu 
        """
        edit_menu = Menu(self.home_menu)
        edit_menu.add_command(label="Edit environment", command = partial(self.eventButtonClickEdit))
        
        """ 
        Help menu 
        """
        help_menu = Menu(self.home_menu)
        help_menu.add_command(label = "Help", command = partial(self.eventButtonClickHelp))
        
        for index, label_text, commands in zip(range(1, 4), ["File", "Edit", "Help"], [file_menu, edit_menu, help_menu]):
            self.home_menu.add_cascade(label= label_text, menu = commands)
        
        # Notebook include tab home, laser P3A to C
        self.notebook_control = ttk.Notebook(self.label_root)
        self.notebook_control.pack(expand= True, fill=BOTH, padx=10, pady= 0)
        
        self.noteStyle = ttk.Style()
        self.noteStyle.configure('TNotebook', tabposition='wn')
        self.noteStyle.theme_use('default')
        self.noteStyle.configure("TNotebook", background= "#001c54", borderwidth = 0)
        self.noteStyle.configure("TNotebook.Tab", background = "#001c54", foreground = "#ececec", borderwidth = 0)
        self.noteStyle.map("TNotebook", background= [("selected", "#ececec")] )
        self.noteStyle.map("TNotebook.Tab", foreground = [("selected", "black")])
        
        buttonStyle = ttk.Style()
        buttonStyle.configure('W.TButton', background = "#ececec", foreground = 'black')
        
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
                    self.button_controls[index][se_index] = Button(self.body_controls[index][0], text= button_text, style ='W.TButton', width=15, padding= 2, command = command_)
                    self.button_controls[index][se_index].pack(side = LEFT, padx = 5, pady = 5)
            
            # tab home defineb
            elif index == 0:
                """ 
                UI 2 monitor: tree view and processing
                """
                self.body_controls[index] = [None for _ in range(3)]
                """ 
                Tree view for open and browse data
                """
                self.body_controls[index][0] = Frame(self.tab_controls[index])
                self.body_controls[index][0].pack(fill= Y, padx = 0 ,pady = 5, side = LEFT)
                """ 
                Tree view for open and browse segment
                """
                self.body_controls[index][2] = Frame(self.tab_controls[index])
                self.body_controls[index][2].pack(fill= Y, padx = 0 ,pady = 5, side = RIGHT)
                """
                View for processing data 
                """
                self.body_controls[index][1] = Frame(self.tab_controls[index])
                self.body_controls[index][1].pack(fill= Y, padx = 0 ,pady = 5, side = LEFT)
                
                self.body_control_processing = [None for _ in range(3)]
                for second_index in range(3):
                    self.body_control_processing[second_index] = Frame(self.body_controls[index][1])
                    self.body_control_processing[second_index].pack(fill= BOTH, padx = 0 ,pady = 5)
                    
                self.tree = ttk.Treeview(self.body_controls[index][0])
                ysb = ttk.Scrollbar(self.body_controls[index][0], orient='vertical', command=self.tree.yview)
                xsb = ttk.Scrollbar(self.body_controls[index][0], orient='horizontal', command=self.tree.xview)
                self.tree.configure(yscroll = ysb.set, xscroll = xsb.set, height= 38)
                self.tree.heading('#0', text='Data Source', anchor='n', command= partial(self.eventButtonClickChangeDataSource, self.tree))
                
                abspath = os.path.abspath("data/data_source")
                root_node = self.tree.insert("", 'end', text = abspath, open = True)
                self.processDirectory(root_node, abspath)
                xsb.pack(fill = X, side = BOTTOM)
                ysb.pack(fill = Y, side = RIGHT)
                self.tree.pack(fill = Y)
                
                self.segment_param_tab = ttk.Treeview(self.body_controls[index][2])
                self.segment_param_tab.heading('#0', text='Data Control Plan', anchor='n')
                self.segment_param_tab.configure(height= 28)
                self.segment_param_tab.pack(fill = Y, side = TOP)
                
                self.segment_tab = ttk.Treeview(self.body_controls[index][2])
                self.segment_tab.heading('#0', text='Information', anchor='n')
                self.segment_tab.pack(fill = Y, side = TOP)
                
                self.button_browse = Button(self.body_controls[index][0], style ='W.TButton', text = "Select", command = partial(self.selectItem, self.tree, self.segment_tab, self.segment_param_tab))
                self.button_browse.pack(fill = X, side = BOTTOM)
                
                self.button_clear = Button(self.body_controls[index][2], style ='W.TButton', text = "Clear Workspace", command = partial(self.clearWorkspace, self.segment_param_tab, self.segment_tab))
                self.button_clear.pack(fill = Y, side = BOTTOM)
                
                self.sheet_view_home = tksheet.Sheet(self.body_control_processing[0], height=770, width=1980,  data = [[]])
                self.sheet_view_home.pack(fill = BOTH, side = TOP, padx=5, pady = 0, expand=True)
                self.sheet_view_home.enable_bindings()
                
                self.radio_list = [None for _ in range(3)]
                for second_index, text_ in zip(range(3), ["P3A", "P3B", "P3C"]):
                    self.radio_list[second_index] = Radiobutton(self.body_control_processing[1], text= text_, variable = self.radio_value, value = second_index +1)
                    self.radio_list[second_index].pack(fill = Y, side = LEFT, padx= 5)
                self.button_running_home = Button(self.body_control_processing[1], style ='W.TButton', text = "Run", width= 20 , command = partial(self.eventButtonClickProcessingHome, self.sheet_view_home,self.radio_value))
                self.button_running_home.pack(fill = X, side = RIGHT, padx = 5)
                
if __name__ == "__main__":
                meta.external_var.root = Tk()
                meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image.png'))
                meta.external_var.root.geometry('1200x1000+300+0') 
                app_laser = LaserFrame(meta.external_var.root)
                meta.external_var.root.mainloop()  

## python3 template/laser_frame.py
