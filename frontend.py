import tkinter as tk
from tkinter import *
from tkinter import filedialog
import time

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    file = open(filename, "r")
    print('Selected:', filename)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0
        self.txt_speed = 0
        # self.textLabel.after(1000, self.say_hi)

    def create_widgets(self):
        global var
        var = StringVar()
        self.textLabel = tk.Label(self, textvariable = var)
        self.textLabel.pack(side="top")
        # Button to Restart Text
        self.restart = tk.Button(self, text="Restart Text", fg="black",
                              command=self.restart_txt)
        self.restart.pack(side="bottom")
        # Button to Play/Pause
        self.pause = tk.Button(self, text="PLAY/PAUSE", fg="black",
                              command=self.pause_txt)
        self.pause.pack(side="bottom")
        # Button to terminate program
        self.quit = tk.Button(self, text="QUIT", fg="black",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        # Button to add local file system
        self.addFile = tk.Button(self, text='Open', fg="black", command=UploadAction)
        self.addFile.pack(side="bottom")

    def say_hi(self):
        list = ["hi", "my", "name", "is", "pablo", "mf"]
        if self.count < len(list):
            if self.txt_speed > 0:
                var.set(list[self.count])
                self.count += 1
                self.textLabel.after(self.txt_speed, self.say_hi) # call this method again in 1,000 milliseconds

    def pause_txt(self):
        if self.txt_speed > 0:
            self.txt_speed = 0
        else:
            self.txt_speed = 200
            self.textLabel.after(self.txt_speed, self.say_hi)

    def restart_txt(self):
        self.txt_speed = 0
        self.count = 0
        self.textLabel.after(self.txt_speed, self.say_hi)

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
