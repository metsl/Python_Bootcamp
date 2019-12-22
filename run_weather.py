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


    output_file = "city_info.csv"
    city_info = ('max temp: 25, min temp: -10, sunset: 21:00',
                 'max temp: 29, min temp: -3, sunset: 22:00',
                 'max temp: 24, min temp: 3, sunset: 20:00')
    with open(output_file, 'w') as f:
        w = csv.DictWriter(f, fieldnames = ['city', 'city_info'], delimiter=" ")
        w.writeheader()
        for i in range(0, len(city_info)):
             writer.writerow({'city': content[i], 'city_info': city_info[i]}

main()
