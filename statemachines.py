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


 import re

regex = r"\{(.*?)\}"

test_str = ("Server_1 {\n"
    "/directory1 /directory2\n\n"
    "}\n"
    "Server_2 {\n\n"
    "/directory1\n\n"
    "/directory2\n\n"
    "}")

matches = re.finditer(regex, test_str, re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches):
    for groupNum in range(0, len(match.groups())):
        print (match.group(1))


