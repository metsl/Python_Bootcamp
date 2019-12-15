import Test_class
import tkinter as tk
from tkinter import filedialog
from termcolor import colored


def get_output_option(output):
    """""
        underlining matching text (not with ^) on -u
        Highlighting matching text on -c
        outputting machine readable output on -m
        outputting regular text on -x
    """

    word_str = str(output)
    #print ('The word is', {word_str})

    choice = input("Enter -u (for underscore)\nEnter -c (color highlighting)\nEnter -m (machine "
                   "readable output \nEnter -x (for standard output)")
    choice = str(choice)
    emptyword = ''
    if choice == '-u':
        # print('\033[4m'+ word_str)
         for i in range(0, len(word_str)):
            if word_str[i] == '':
                emptyword = emptyword + word_str[i]
            else:
                emptyword = emptyword + word_str[i]+str('\033[4m')
    elif choice == '-t':
        print.colored( word_str, 'red' )
    print(emptyword)

def main():
    folder = tk.Tk()
    folder.withdraw()
    file_path_string = filedialog.askopenfilename()
    pattern = input("Type text to find: ")
    word = Test_class.Word(file_path_string)
    output = word.find_regex_match(str(pattern))
    # print(output)
    get_output_option(output)


main()