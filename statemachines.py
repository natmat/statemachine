import tkinter as tk
from tkinter import filedialog
import re
import sys
from sm import SM

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    filetypes=[("sm files","*.cpp")]
)
# file_path = "evacSm.cpp"
# file_path = "dcosm.dat"
# print(file_path)
# file_path = "D:\svn\Gen6\QA\Libraries\TmcStadler\DcoSm.cpp"
with open(file_path, 'r') as f:
    all_lines = f.readlines()

all_lines = [x.strip() for x in all_lines]

state_machines = []

it = iter(all_lines)


def newStateTransition(lines):
    if len(lines) < 5:
        print("ERROR: not enough SM inputs")
        return

    sm = SM()
    try:
        sm.init_sm(lines)
    except IndexError as e:
        print("ERROR: ", repr(e))
    state_machines.append(sm)


done = False
for line in it:
    if '_fsm.addTransitions' in line:
        break

while not done:
    line = next(it)
    if re.match('^}\);', line.strip()):
        done = True
        continue

    if not re.match('^{', line.strip()):
        continue

    line = next(it)
    sm_lines = []
    while not re.match('^},?', line.strip()):
        if not re.match('^//', line):
            sm_lines.append(line.strip().rstrip(','))
        line = next(it)

    state_machine = []
    newStateTransition(sm_lines)

print('# {}'.format(file_path))
print("""
digraph G {
	rankdir=LR;
	node [shape = doublecircle]; Initial;
	node [shape = circle, style=filled, fontcolor=blue fontsize=12];
     
""")

for s in state_machines:
    s.print()

print('}\n')

