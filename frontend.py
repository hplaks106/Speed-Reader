import tkinter as tk
from tkinter import *
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0
        self.textLabel.after(1000, self.say_hi)

    def create_widgets(self):
        global var
        var = StringVar()
        self.textLabel = tk.Label(self, textvariable = var)
        self.textLabel.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        list = ["hi", "my", "name", "is", "pablo", "mf"]
        if self.count < len(list):
            var.set(list[self.count])
            self.textLabel.after(200, self.say_hi) # call this method again in 1,000 milliseconds
            self.count += 1

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
