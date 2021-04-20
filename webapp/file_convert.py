# PDF reader to parse file text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter  # XMLConverter, HTMLConverter,
from pdfminer.layout import LAParams
import docx
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


def convertDocx(filename):
    """Reutrns string extracted from a docx file"""
    doc = docx.Document(filename)
    extracted = []
    for para in doc.paragraphs:
        extracted.append(para.text)
    return '\n'.join(extracted)


def gettext(name_of_file):
    "returns a string of text from the appropriate file type inputed"
    return_string = ""
    if name_of_file.find(".txt") != -1:
        return_string = convertTxt(name_of_file)
    elif name_of_file.find(".pdf") != -1:
        return_string = pdfparser(name_of_file)
    elif name_of_file.find(".docx") != -1:
        return_string = convertDocx(name_of_file)
    return return_string


def readFile(filename):
    """Reads from filename and converts it into a list of strings."""
    list = gettext(filename)  # get PDF formatted as text
    # fill in spaces to the PDF text
    for x in range(0, len(list)):
        if len(list) > x and filter(list[x]):
            list = list[0: x:] + ' ' + list[x+1::]
    list = list.split()
    return list
