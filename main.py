from tkinter import *
from tkinter import font
from tkinter import ttk

atm = {
  # letters
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
  # numbers
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
  # special characters
    ' ': '/',
    '.': '.-.-.-',
    '?': '..--..',
    '!': '-.-.--',
    ',': '--..--',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '$': '...-..-',
    '@': '.--.-.',
    '_': '..--.-',
    '"': '.-..-.',
    "'": '.----.',
}


def translate(word):
    return " ".join(atm[char] for char in word.upper())  # make everything upper case


if __name__ == "__main__":

    # Build the GUI layout
    root = Tk()
    root.geometry('1000x300')
    root.title("Morse Code Translator")
    titleFont = font.Font(family=" Calibri ", size=14)

    title = Label(root, text="ASCII to Morse Code Translator", font=titleFont)
    title.pack(side=TOP)

    prompt = Label(root, text="~:{||Ascii to morse code translator||}:~\n")
    prompt.pack(side=TOP)

  # Function for the translate button
    def click():
        word = txt_entry.get()
        try:
            res = (translate(word))
        except:  # catch errors
            res = "Invalid input"
        print(res)
        lbl.configure(text=res, font=titleFont)

    prompt = Label(root, text="Input Alphabet/ASCII:")
    prompt.pack(side=TOP)


    # Text box and translate button
    txt_entry = Entry(root, bd=1)
    txt_entry.pack(side=TOP)

    translate_button = ttk.Button(root, text="Translate", width=20, command=click)
    translate_button.pack(side=TOP)




    lbl = Label(root, text=" ")
    lbl.pack(side=TOP)

    root.mainloop()

    