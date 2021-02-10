import tkinter as tk
from tkinter import filedialog
import re
import sys
from sm import SM

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# file_path = "evacSm.cpp"
# file_path = "dcosm.dat"
# print(file_path)
# file_path = "D:\svn\Gen6\QA\Libraries\TmcStadler\DcoSm.cpp"
with open(file_path, 'r') as f:
    all_lines = f.readlines()

all_lines = [x.strip() for x in all_lines]

state_machines = []

it = iter(all_lines)


def newStateTransition():
    global end_of_fsm_regex, line, sm
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
    end_of_fsm_regex = re.compile('fsm.addTransitions')
    result = end_of_fsm_regex.search(line)
    if not result:
        continue

    line = next(it)
    while not done and line is not None:
        end_of_fsm_regex = re.compile('}\);')
        while line != '{':
            if end_of_fsm_regex.match(line):
                done = True
                break
            line = next(it)

        state_machine = []
        newStateTransition()

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

