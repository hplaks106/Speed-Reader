"""Program converts PDF file to text and displays one word at a time."""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import time

def UploadAction(event=None):
    """Gets file from user's computer."""
    filename = filedialog.askopenfilename()
    file = open(filename, "r")
    print('Selected:', filename)

class Application(tk.Frame):
    def __init__(self, master=None):
        """Initialization creates GUI, widgets, and variables."""
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0
        self.txt_speed = 0
        # self.textLabel.after(1000, self.display_text)

    def create_widgets(self):
        """Creates tkinter widgets for the GUI."""
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
        self.addFile = tk.Button(self, text='Open', fg="black",
                              command=UploadAction)
        self.addFile.pack(side="bottom")

    def display_text(self):
        """Temporary test case sentence output."""
        list = ["hi", "my", "name", "is", "pablo", "mf"]
        if self.count < len(list):
            if self.txt_speed > 0:
                var.set(list[self.count])
                self.count += 1
                self.textLabel.after(self.txt_speed, self.display_text)

    def pause_txt(self):
        """Pause button stops the text from continously displaying."""
        if self.txt_speed > 0:
            self.txt_speed = 0
        else:
            self.txt_speed = 200
            self.textLabel.after(self.txt_speed, self.display_text)

    def restart_txt(self):
        """Resets the displayed text to the beginning of the file."""
        self.txt_speed = 0
        self.count = 0
        var.set("")
        self.textLabel.after(self.txt_speed, self.display_text)

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
