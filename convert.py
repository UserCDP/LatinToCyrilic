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
} # Then we have symbols for 'IU', 'CH' and 'IA'Ю Ч Я

Tk().withdraw()
filename = askopenfilename()
pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))

outfile = open(filename.split('.')[0] + '-ch.txt', 'w')

k = 0
while True:
    try:
        text = pdf_reader.pages[k].extract_text()
    except IndexError:
        break

    k += 1
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
                outfile.write('\n')
                words_per_line = 0

outfile.close()