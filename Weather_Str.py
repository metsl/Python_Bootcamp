import tkinter as tk
from tkinter import filedialog
import csv

def main():
    folder = tk.Tk()
    folder.withdraw()
    file_path_string = filedialog.askopenfilename()
    with open(file_path_string) as f:
        content = f.read()
    print(content)

    lines = [['max temp: 25, min temp: -10, sunset: 21:00',
              'max temp: 29, min temp: -3, sunset: 22:00',
              'max temp: 24, min temp: 3, sunset: 20:00']]


    header = [content]
    #header = ['Moskow', 'New York', 'London']

    with open("test.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header) # write the header
    # write the actual content line by line
        for l in lines:
            #writer.writerow(l)
    # or we can write in a whole
            writer.writerows(lines)

main()
