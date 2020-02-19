import re

class SM:

    def __init__(self):
        self.this_state = ''
        self.next_state = ''
        self.event = ''
        self.guard = ''
        self.trigger = ''
        self.ternal = ''

    def init_sm(self, transitions):
        self.this_state = transitions[0]
        self.next_state = transitions[1]
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
        print("{} -> {} [label=\"{}\"];".format(self.this_state, self.next_state, self.guard))
