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
        self.txt_speed = 0
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

        self.textLabel = Label(self, width=700, bg="white", textvariable=var,
                               borderwidth=0)
        self.textLabel.grid(row=0, column=0)

        self.restart = Button(self, text="Restart Text",
                              command=self.restart_txt)
        self.restart.grid(row=1, column=0)

        self.pause = Button(self, text="PLAY/PAUSE", command=self.pause_txt)
        self.pause.grid(row=2, column=0)

        self.quit = Button(self, text="QUIT", command=self.master.destroy)
        self.quit.grid(row=3, column=0)

        self.addFile = Button(self, text="OPEN", command=self.UploadAction)
        self.addFile.grid(row=4, column=0)

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
            self.txt_speed = 500
            # Resume the text display when resumed
            self.textLabel.after(self.txt_speed, self.display_text)

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
            time.sleep(5)
            self.progress.stop()
            self.progress.grid_forget()
            self.addFile['state'] = 'normal'
        self.addFile['state'] = 'disabled'
        threading.Thread(target=real_traitement).start()


root = Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
