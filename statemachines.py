import tkinter as tk
from tkinter import filedialog
import re
import sys

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename()
# print(file_path)
file_path = "evacSm.cpp"
print(file_path)

input = open('dcosm.dat', 'r')

with open("EvacSM.cpp", "r") as f:
    # Define regex searches
    for line in f:
        regexAddTransistions = re.compile("void.*addTransitions", re.DOTALL)
        result = regexAddTransistions.search(line)
        if not result:
            continue
        else:
            print('result2=', result)
            all_lines = "".join(f.readlines())

            regexStartOfStart = re.compile("^{", re.MULTILINE);
            result = regexStartOfStart.search(all_lines)
            if result:
                print ('result3=', result)

            # Find the {...} text
            regex = r"\{(.*^[\s]*)\},$"
            matches = re.finditer(regex, all_lines, re.MULTILINE | re.DOTALL)

            for match_num, match in enumerate(matches):
                print('match={}'.format(match))
                it = re.finditer(r".*?,", match.group(1), re.MULTILINE)
                for i in it:
                    print(i)
