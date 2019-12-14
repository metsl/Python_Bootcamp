import re
import fileinput
import sys
import os
import argparse


# inputing data from file (located in the same folder as Python)
# i don't know how to call this function correctly

class InputOutput():

    def __init__(self, pattern, file, text):
        self.pattern = pattern
        self.file = file
        self.text = text

    file = input("enter filename:")
    text = input("enter text to be searched:")

    pattern = open(file, "r")

    for line in pattern:
        if re.match('(.+) ' + text + ' (.+)', line):
            print(line)


# asking user for inputing any of 3 options: underscoring, highliting and generate machine readable output
print("Available output options:\nEnter -u ( --underscore )\nEnter -c ( --color highliting )\nEnter -m ( --machine readable output \nEnter -x for standard output")


# underlining matching text (not with ^)
# print("{:s}\n{:s}\n".format(line, len(line) * "^"))   #underlines with ^ the whole line.
def get_output_option(self):
    if choise == u:
        formattedText = []
        for t in line.lower().split():
            if t == text:
                formattedText.append("\\033[4m" + t + "\033[0m")
            else:
                formattedText.append(t)

        print(" ".join(formattedText))


# Highliting matching text
    elif choise == c:
        formattedText = []
        for t in line.lower().split():
            if t == text:
                formattedText.append("\033[92m" + t + "\033[0m")
            else:
                formattedText.append(t)

        print(" ".join(formattedText))
        # print( "\033[92m {}\033[00m" .format(line))  #highlights the whole line, not pattern

    elif choise == m:
        pass  # machine readable input

    # outputing regular text
    elif choise == x:
        print(line)
    return 0