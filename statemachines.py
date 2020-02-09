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
    #Define regex searches
    reAddTransistions = re.compile("_fsm.addTransitions.*$")
    reEndOfState = ("^\s*\}")
    reEndOfAddTransitions = ("^\}")

    for line in f:
        result = reAddTransistions.search(line)
        if result:
            print(result)

            data = "".join(f.readlines())
            regex = r"\{(.*?)\}"
            matches = re.finditer(regex, data, re.MULTILINE | re.DOTALL)

            for matchNum, match in enumerate(matches):
                print(matchNum, match)
                for groupNum in range(0, len(match.groups())):
                    print (match.group(1))


