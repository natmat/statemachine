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
# file_path = "EvacSM.cpp"
# print(file_path)

with open(file_path, 'r') as f:
    all_lines = f.readlines()

# Remove spaces from line
all_lines = [x.strip() for x in all_lines]

def newStateTransition():
    global end_of_fsm, line, sm
    while end_of_state.match(line) is None:
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


start_of_fsm = re.compile('fsm.addTransitions')
end_of_fsm = re.compile('}\);')
start_of_state = re.compile('{')
end_of_state = re.compile('^}[,]?.*$')

state_machines = []
it = iter(all_lines)
done = False
for line in it:
    # Search for the FSM start
    result = start_of_fsm.search(line)
    if not result:
        continue

    # Skip current, read the next line
    line = next(it)
    while not done and line is not None:
        while not start_of_state.match(line):
            # print("# ", line)
            if end_of_fsm.match(line):
                # print("end of FSM")
                done = True
                break
            line = next(it)

        state_machine = []
        newStateTransition()

print("""
digraph G {
	rankdir=LR;
	node [shape = doublecircle]; Initial;
	node [shape = circle, style=filled, fontcolor=blue fontsize=12];
     
""")

for s in state_machines:
    s.print()

print('}\n')

