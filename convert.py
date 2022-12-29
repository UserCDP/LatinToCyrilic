""" Copyright Daniela Cojocaru 2022 """

import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

ALPHABET = {
    'A': 'А', 'Ă': 'Э', 'Â': 'Ы', 'B': 'Б', 'C': 'К',
    'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Ч',
    'I': 'И', 'Î': 'Ы', 'J': 'Ж', 'K': 'К', 'L': 'Л',
    'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'ЧУ',
    'R': 'Р', 'S': 'С', 'Ș': 'Ш', 'T': 'Т', 'Ț': 'Ц',
    'U': 'У', 'V': 'В', 'W': 'В', 'X': 'Х', 'Y': 'Ы', 'Z': 'З'
} # Then we have symbols for 'IU'-Ю, 'CH'-Ч and 'IA'-Я

def __main__():
    """The main body of the program"""
    Tk().withdraw()
    filename = askopenfilename()
    outfile = open(filename.split('.')[0] + '-ch.txt', 'w')
    if filename.split('.')[1].upper() == 'PDF':
        open_pdf(filename, outfile)
    elif filename.split('.')[1].upper() == 'TXT':
        open_txt(filename, outfile)
    outfile.close()

def open_pdf(filename, outfile):
    """
    A function that recieves the name of the file and the name
    of the outfile and prints the converted text from the
    infile to the outfile
    """
    pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))
    n = len(pdf_reader.pages)
    for k in range(n):
        convert_text(pdf_reader.pages[k].extract_text(), outfile) # convert each page one by one

def open_txt(filename, outfile):
    file = open(filename, 'r')
    for line in file:
        convert_text(line, outfile)


def convert_text(text, outfile):
    """
    A function that uses the ALPHABET dictionary to replace letters
    Recieves as input the text that we want to convert and the name
    of the file to which we want to write the new text.
    Returns nothing
    """
    n = len(text)
    words_per_line = 0
    for i in range(n):
        if text[i].isalpha():
            if text[i].isupper():
                if text[i] == 'I' and text[i+1] == 'U':
                    outfile.write('Ю')
                    i += 1
                elif text[i] == 'I' and text[i+1] == 'A':
                    outfile.write('Я')
                    i += 1
                elif text[i] == 'C' and text[i+1] == 'H':
                    outfile.write('Ч')
                    i += 1
                else:
                    outfile.write(ALPHABET[text[i]])
            else:
                if text[i] == 'i' and text[i+1] == 'u':
                    outfile.write('Ю'.lower())
                    i += 1
                elif text[i] == 'i' and text[i+1] == 'a':
                    outfile.write('Я'.lower())
                    i += 1
                elif text[i] == 'c' and text[i+1] == 'h':
                        outfile.write('Ч'.lower())
                        i += 1
                else:
                    outfile.write(ALPHABET[text[i].upper()].lower())

        else:
            outfile.write(text[i])
            if text[i] == ' ':
                words_per_line += 1

            if words_per_line == 12:
                #outfile.write('\n')
                words_per_line = 0

__main__()