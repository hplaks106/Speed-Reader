# Please make sure you have modules pdf, pdfminer, and subsequent modules.
# import sys
# PDF reader to parse file text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter  # XMLConverter, HTMLConverter,
from pdfminer.layout import LAParams
from tkinter.ttk import Progressbar
from tkinter import BOTTOM
import time
import io


def filter(character):
    """Checks whether the character is ' ', '.', or '?' for proper display."""
    if (character.isalnum() is not True and character != " "
            and character != "." and character != "?"
            and character != "'" and character != ":"):
        return True
    else:
        return False


def pdfparser(data):
    """Decodes the file using utf-8 and returns the data to readFile."""
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()  # stores fonts, images, etc.
    retstr = io.StringIO()  # creates string buffer
    laparams = LAParams()  # Layout Parameters

    # obtains the format of the PDF: decoded text, fonts, layout, lines, etc.
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Process each page contained in the document
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    return data


def convertTxt(name_of_file):
    """Converts the file to txt and returns as a string"""
    opened = open(name_of_file, "rb")
    text = ""
    for line in opened:
        text = text + " " + line.decode("utf-8").rstrip()
    return text


def gettext(name_of_file):
    "returns a string of text from the appropriate file type inputed"
    return_string = ""
    if name_of_file.find(".txt") != -1:
        return_string = convertTxt(name_of_file)
    elif name_of_file.find(".pdf"):
        return_string = pdfparser(name_of_file)
    return return_string


def readFile(filename, master):
    """Reads from filename and converts it into a list of strings."""
    # progress bar to show progress to user
    progress = Progressbar(master, orient='horizontal', length=400,
                           mode='determinate')
    progress.pack(side=BOTTOM, padx=5, pady=5)  # Placment and padding
    progress['value'] = 25  # update progress bar value
    master.update()  # update the window
    list = gettext(filename)
    progress['value'] = 50  # update the value after 50% of work completed
    master.update()  # update the window
    # fill in spaces to the PDF text
    for x in range(0, len(list)):
        if len(list) > x and filter(list[x]):
            list = list[0: x:] + ' ' + list[x+1::]
    progress['value'] = 75  # update value to 75% completion
    master.update()  # update the window
    list = list.split()
    progress['value'] = 100  # update to 100% completion
    master.update()  # update window
    time.sleep(5)  # sleep so user can see completion rate of 100%
    progress.destroy()  # destroy progress bar
    master.update()  # update the window
    return list
