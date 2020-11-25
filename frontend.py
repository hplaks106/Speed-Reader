"""Program converts PDF file to text and displays one word at a time."""
from tkinter import StringVar, DoubleVar
from tkinter import filedialog
from tkinter import Tk, Scale
from tkinter.ttk import Frame, Button, Label, Style
import fileConvert as conv


class Application(Frame):
    def __init__(self, master=None):
        """Initialization creates GUI, widgets, and variables."""
        super().__init__(master)
        self.master = master
        self.initUI()
        self.count = 0
        self.txt_speed = 0  # starts by not displaying until resumed
        self.saved_speed = 300  # default speed
        self.file = list()
        self.filename = None

    def initUI(self):
        """Initialize the User Interface"""
        global var
        columns = [0, 1, 2, 3, 4]  # columns grid padding
        rows = [0, 1, 2, 3, 4, 5]  # rows grid padding
        var = StringVar()
        style=Style()
        self.master.title("Speed-Reader")

        Style().configure("Tbutton", padding=(0, 5, 0, 5))
        style.configure('Q.TButton', foreground='red')
        style.configure('O.TButton', foreground='green')
        style.configure('P.TButton', foreground='blue')
        style.configure('T.TButton', font=('serif', 30),
                                foreground = 'black')

        self.columnconfigure(columns, pad=5, minsize=25)
        self.rowconfigure(rows, pad=5, minsize=25)

        self.textLabel = Label(self, style='T.TButton',
                               textvariable=var)

        self.textLabel.grid(row=0, column=3)

        self.restart = Button(self, text="Restart Text",
                              command=self.restart_txt)
        self.restart.grid(row=2, column=2)

        self.pause = Button(self, text="⏯️",  style='P.TButton',
                            command=self.pause_txt)
        self.pause.grid(row=1, column=4)

        init_slide_val = DoubleVar()  # create initial slider value variable
        self.speed_slider = Scale(self, cursor='sb_h_double_arrow', from_=100,
                                  to=300, length=200, tickinterval=50,
                                  resolution=5, orient='horizontal',
                                  variable=init_slide_val, command=lambda x:
                                  self.change_speed(self.speed_slider.get()))

        init_slide_val.set(200)  # initialize the slider to 200 WPM
        self.speed_slider.grid(row=3, column=3)

        self.quit = Button(self, text="QUIT", style='Q.TButton',
                           command=self.master.destroy)
        self.quit.grid(row=2, column=4)

        self.addFile = Button(self, text="OPEN", style='O.TButton',
                              command=self.UploadAction)
        self.addFile.grid(row=1, column=2)

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
        speed = int((60 / speed) * 1000)  # convert WPM to text_speed
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
        self.file = conv.readFile(self.filename, self.master)


root = Tk()
root.geometry()
app = Application(master=root)
app.mainloop()
