import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename()
# print(file_path)
file_path = "evacSm.cpp"
print(file_path)

input = open('dcosm.dat', 'r')


with open("EvacSM.cpp", "r") as f:


    reAddTransistions = re.compile("void.*addTransitions.*$")
    reEndOfState = ("^\s+\}")
    reEndOfAddTransitions = ("^\}")
    for line in f:
        result = regex.search(line)
        if result:
            print(result)




