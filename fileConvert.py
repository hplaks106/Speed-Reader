# Please make sure you have modules pdf, pdfminer, and subsequent modules.
# import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter  # XMLConverter, HTMLConverter,
from pdfminer.layout import LAParams
import io


def filter(character):
    if (character.isalnum() is not True and character != " "
            and character != "." and character != "?"
            and character != "'" and character != ":"):
        return True
    else:
        return False


def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    return data


def readFile(filename):
    text = pdfparser(filename)
    for x in range(0, len(text)):
        if len(text) > x and filter(text[x]):
            text = text[0: x:] + ' ' + text[x+1::]
    text = text.split()
    return text
