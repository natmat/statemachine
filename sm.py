import re
import random
import numpy

def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","turquoise","pink"]
    random.shuffle(colors)
    # color = list(numpy.random.choice(range(256), size=3))
    return colors[0]

class SM:

    def __init__(self):
        self.this_state = ''
        self.next_state = ''
        self.event = ''
        self.guard = ''
        self.trigger = ''
        self.ternal = ''

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

        self.trigger = transitions[4]
        self.ternal = transitions[5]

    def print(self):
        colour = pick_color()
        print("\t{} -> {} [color={}, fontcolor={}, label=\"{}\"];".format(self.this_state, self.next_state, colour, colour, self.event))
