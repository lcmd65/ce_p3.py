from tkinter import *
from tkinter import messagebox
from functools import partial 
import meta.external_var
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class HelpFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def sendEmail(self, sender, recipient, subject, body):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, "fsvn-123456")
            message = MIMEMultipart()
            message["From"] = sender
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
        except: pass
            
    def eventClickButtonOK(self, recipient, body):
        try:
            body_send = "We have received your Information and will Feedback soon. Thank You \n FSVN-CE Help"
            self.sendEmail("help.CEFSVN@gmail.com", "help.CEFSVN@gmail.com", "Help", body.get())
            self.sendEmail("help.CEFSVN@gmail.com", recipient, "FSVN - Copy Exactly", body_send)
        except Exception as e:
            messagebox.showerror(message = e)
    
    def initUI(self):
        self.parent.title("Help")
        self.pack(expand=True, fill = BOTH)
        
        self.label_privacy = Label(self.parent, text ="First Solar privacy @2022", font =("Roboto",14,"bold"))
        self.label_privacy.pack(fill= X, side = LEFT)
        
        label_body = Label(self)
        label_body.pack(fill = BOTH)
        
        frame_body = [None for _ in range(4)]
        for index in range(4):
            frame_body[index] = Frame(label_body)
            frame_body[index].pack(fill = X)
        
        text1 = Text(frame_body[0], height= 5)
        text1.insert(1.0, "please send email to dat.lemindast@gmail.com")
        text1.pack(fill= X, side =LEFT)
        
        label_email = Label(frame_body[1], text = meta.external_var.email)
        label_email.pack(fill = X )
        
        text2 = Text(frame_body[1])
        text2.pack(fill = BOTH)
        
        text3 = Text(frame_body[2])
        text3.pack(fill = BOTH)
        
        button = Button(frame_body[3], text = "OK", width= 10, command = partial(self.eventClickButtonOK, text2, text3 ))
        button.pack(side = RIGHT)
