import re
import random
import numpy

def pick_color():
    colors = ["blue","black","brown","red","darkorchid1","green","orange","turquoise","pink"]
    return random.choice(colors)

class SM:

    def __init__(self):
        self.this_state = ''
        self.next_state = ''
        self.event = ''
        self.guard = ''
        self.action = ''
        self.xternal = ''

    def init_sm(self, transitions):
        s = 'State::'
        self.this_state = re.sub(s, '', transitions[0])
        self.next_state = re.sub(s, '', transitions[1])
        self.event = transitions[2]

        regex = re.compile('.*return\s*(.*);')
        result = regex.search(transitions[3], re.DOTALL)
        if result:
            self.guard = result.group(1)
        else:
            self.guard = ''

        regex = re.compile('.*\{(.*)\}')
        result = regex.search(transitions[4], re.DOTALL)
        if result:
            self.action = result.group(1)
        else:
            self.action = ''

        # print(transitions)
        self.xternal = transitions[5]

    def print(self):
        colour = pick_color()
        # print("\t{} -> {} [color={}, fontcolor={}, label=\"{}\n[{}]\"];".
        #       format(self.this_state, self.next_state, colour, colour, self.event, self.guard))
        print("\t{} -> {} [color={}, fontcolor={}, label=\"{} \[{}\]/\\n{}\"];".
              format(self.this_state, self.next_state, colour, colour, self.event, self.guard, self.action.strip(

        ).rstrip(';')))
