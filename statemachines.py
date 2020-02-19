import tkinter as tk
from tkinter import filedialog
import re
import sys
from sm import SM

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename()
# print(file_path)

file_path = "evacSm.cpp"
# print(file_path)

# input = open('dcosm.dat', 'r')

with open('EvacSM.cpp', 'r') as f:
    all_lines = f.readlines()

all_lines = [x.strip() for x in all_lines]

state_machines = []

it = iter(all_lines)


def newStateTransition():
    global regex, line, sm
    regex = re.compile('},?')
    while regex.match(line) is None:
        if not line.startswith('/'):
            # print(line)
            state_machine.append(line.rstrip(','))
        line = next(it)

    # print('sm', state_machine)
    if len(state_machine) < 5:
        return
    sm = SM()
    sm.init_sm(state_machine[1:])
    state_machines.append(sm)


done = False
for line in it:
    regex = re.compile('fsm.addTransitions')
    result = regex.search(line)
    if not result:
        continue

    line = next(it)
    while not done and line is not None:
        regex = re.compile('}\);')
        while line != '{':
            if regex.match(line):
                done = True
                break
            line = next(it)

        state_machine = []
        newStateTransition()

for s in state_machines:
    s.print()

print('DONE')

