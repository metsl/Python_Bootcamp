import tkinter as tk
from tkinter import filedialog
import csv


def main():
    folder = tk.Tk()
    folder.withdraw()
    file_path_string = filedialog.askopenfilename()
    with open(file_path_string) as f:
        content = f.read()
    output_file = "city_info.csv"
    fieldnames = ['city', 'max temp', 'min temp', 'sunset']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'max temp': '25', 'min temp': '-10', 'sunset': '21:00'})
    writer.writerow({'max temp': '29', 'min temp': '-3', 'sunset': '22:00'})
     writer.writerow({'max temp': '24', 'min temp': '3', 'sunset': '20:00'})


main()