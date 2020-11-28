# PDF reader to parse file text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter  # XMLConverter, HTMLConverter,
from pdfminer.layout import LAParams
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


def convert_pdf(filename):
    """Reads from filename and converts it into a list of strings."""
    list = pdfparser(filename)  # get PDF formatted as text
    # fill in spaces to the PDF text
    for x in range(0, len(list)):
        if len(list) > x and filter(list[x]):
            list = list[0: x:] + ' ' + list[x+1::]
    list = list.split()
    return list