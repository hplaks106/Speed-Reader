"""Program converts PDF file to text and displays one word at a time."""
from tkinter import StringVar
from tkinter import filedialog
from tkinter import Tk, HORIZONTAL
from tkinter.ttk import Frame, Button, Label, Progressbar, Style
import threading
import time
import fileConvert as conv


class Application(Frame):
    def __init__(self, master=None):
        """Initialization creates GUI, widgets, and variables."""
        super().__init__(master)
        self.master = master
        self.initUI()
        self.count = 0
        self.txt_speed = 0  # starts by not displaying until resumed
        self.saved_speed = 500  # default speed
        self.file = list()
        self.filename = None

    def initUI(self):
        """Initialize the User Interface"""
        global var
        var = StringVar()
        self.master.title("Speed-Reader")

        Style().configure("Tbutton", padding=(0, 5, 0, 5), font="serif 10")
        self.columnconfigure(0, pad=5, minsize=50)

        self.rowconfigure(0, pad=5, minsize=25)
        self.rowconfigure(1, pad=5, minsize=25)
        self.rowconfigure(2, pad=5, minsize=25)
        self.rowconfigure(3, pad=5, minsize=25)
        self.rowconfigure(4, pad=5, minsize=25)
        self.rowconfigure(5, pad=5, minsize=25)

        self.textLabel = Label(self, textvariable=var)
        self.textLabel.grid(row=0, column=2)

        self.restart = Button(self, text="Restart Text",
                              command=self.restart_txt)
        self.restart.grid(row=1, column=2)

        self.pause = Button(self, text="PLAY/PAUSE", command=self.pause_txt)
        self.pause.grid(row=2, column=2)

        self.set_speed = Button(self, text="60 WPM", command=lambda: self.change_speed(750))
        self.set_speed.grid(row=3, column=0)

        self.set_speed = Button(self, text="90 WPM", command=lambda: self.change_speed(625))
        self.set_speed.grid(row=3, column=1)

        self.set_speed = Button(self, text="120 WPM", command=lambda: self.change_speed(500))
        self.set_speed.grid(row=3, column=2)

        self.set_speed = Button(self, text="150 WPM", command=lambda: self.change_speed(375))
        self.set_speed.grid(row=3, column=3)

        self.set_speed = Button(self, text="200 WPM", command=lambda: self.change_speed(250))
        self.set_speed.grid(row=3, column=4)

        self.quit = Button(self, text="QUIT", command=self.master.destroy)
        self.quit.grid(row=4, column=2)

        self.addFile = Button(self, text="OPEN", command=self.UploadAction)
        self.addFile.grid(row=5, column=2)

        self.progress = Progressbar(self, orient=HORIZONTAL, length=250,
                                    mode='determinate')
        self.textLabel.after(1000, self.display_text)

        self.pack()

    def display_text(self):
        """Temporary test case sentence output."""
        list = self.file
        if self.count < len(list):
            if self.txt_speed > 0:
                var.set(list[self.count])
                self.count += 1
                self.textLabel.after(self.txt_speed, self.display_text)

    def pause_txt(self):
        """Pause button stops the text from continously displaying."""
        # Set text speed to 0
        if self.txt_speed > 0:
            self.txt_speed = 0
        else:
            # set the text speed to the last used speed
            self.txt_speed = self.saved_speed
            # Resume the text display when resumed
            self.textLabel.after(self.txt_speed, self.display_text)

    def change_speed(self, speed):
        """Changes the text display speed in 60 WPM increments"""
        self.saved_speed = speed
        self.txt_speed = self.saved_speed

    def restart_txt(self):
        """Resets the displayed text to the beginning of the file."""
        # Pause the text display
        self.txt_speed = 0
        # Set to beginning of the file's text
        self.count = 0
        var.set("")
        self.textLabel.after(self.txt_speed, self.display_text)

    def UploadAction(self):
        """Gets file from user's computer."""
        self.filename = filedialog.askopenfilename()
        print('Selected:', self.filename)
        self.file = conv.readFile(self.filename)

        def real_traitement():
            self.progress.grid(row=5, column=0)
            self.progress.start()
            time.sleep(1)
            self.progress.stop()
            self.progress.grid_forget()
            self.addFile['state'] = 'normal'
        self.addFile['state'] = 'disabled'
        threading.Thread(target=real_traitement).start()


root = Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
