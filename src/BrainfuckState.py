from termcolor import colored, cprint

def print_(a):
    print(a, end='')

class BrainfuckState:
    def __init__(self, print_and_wait = False):
        self.print_and_wait = print_and_wait

    def execute(self, text):
        self.line = 1
        self.size = 2000
        self.size_used = 0
        self.ptr = 0
        self.data = [0 for _ in range(self.size)]
        self.pos = 0
        self.text = text
        if self.print_and_wait:
            self.print_state()
            input()
        while not self.is_EOF():
            self.need_stop = True
            {
                '+' : self.plus,
                '-' : self.minus,
                '.' : self.opt,
                ',' : self.ipt,
                '>' : self.right,
                '<' : self.left,
                '[' : self.start_loop,
                ']' : self.end_loop,
                '#' : self.comment,
                '@' : self.dump_value,
                '$' : self.print_state,
                '%' : self.start_step_by_step,
                '!' : self.stop_step_by_step
            }.get(text[self.pos], self.pass_it)()
            self.advance()
            if self.print_and_wait and self.need_stop:
                self.print_state()
                input()

    def start_step_by_step(self):
        self.need_stop = False
        print('step by step ON')
        self.print_and_wait = True

    def stop_step_by_step(self):
        self.need_stop = False
        print('step by step OFF')
        self.print_and_wait = False

    def print_state(self):
        self.need_stop = False
        print_(str(self.line) + '> [')
        first = True
        for i in range(self.size_used + 1):
            if not first:
                print_('|')
            first = False
            s = str(self.data[i])
            while len(s) < 3 and i >= 39:
                s = ' ' + s
            if self.ptr == i:
                cprint(s, 'red', 'on_white', end='')
            else:
                print_(s)
        print(']')

    def set_value(self, value):
        self.data[self.ptr] = value
        self.clamp()

    def get_value(self):
        return self.data[self.ptr]

    def move(self, delta):
        self.ptr += delta
        self.size_used = max(self.ptr, self.size_used)

    def advance(self, delta=1):
        if delta > 0:
            for _ in range(delta):
                if self.is_EOF():
                    break
                if self.current_char() == '\n':
                    self.line += 1
                self.pos += 1
        elif delta < 0:
            for _ in range(-delta):
                if self.is_EOF():
                    break
                if self.current_char() == '\n':
                    self.line -= 1
                self.pos -= 1

    def current_char(self):
        return self.text[self.pos]

    def is_EOF(self):
        return self.pos >= len(self.text) or self.pos < 0

    def clamp(self):
        if self.get_value() < 0:
            self.set_value(0)
        if  self.get_value() > 255:
            self.set_value(255)

    def incr_value(self, incr):
        self.set_value(self.get_value() + incr)

    def plus(self):
        self.incr_value(1)

    def minus(self):
        self.incr_value(-1)

    def opt(self):
        print(chr(self.get_value()), end='')

    def ipt(self):
        i = input()
        if len(i) == 0:
            i = chr(0)
        self.set_value(ord(i[0]))

    def left(self):
        self.move(-1)

    def right(self):
        self.move(+1)

    def start_loop(self):
        if self.get_value() == 0 and not self.is_EOF():
            indent = 1
            while self.current_char() != ']' or indent > 0:
                self.advance()
                if self.is_EOF():
                    break
                if self.current_char() == '[':
                    indent += 1
                if self.current_char() == ']':
                    indent -= 1

    def end_loop(self):
        if self.get_value() != 0 and not self.is_EOF():
            indent = 1
            while self.current_char() != '[' or indent > 0:
                self.advance(-1)
                if self.is_EOF():
                    break
                if self.current_char() == '[':
                    indent -= 1
                if self.current_char() == ']':
                    indent += 1

    def comment(self):
        self.need_stop = False
        self.advance()
        if not self.is_EOF() and self.current_char() == ':':
            self.advance()
            while True:
                c = self.current_char()
                self.advance()
                if self.is_EOF() or (c == ':' and self.current_char() == '#'):
                    break
            return

        while not self.is_EOF() and self.current_char() != '\n':
            self.advance()

    def dump_value(self):
        self.need_stop = False
        print(self.line, '> At', self.ptr, ':', self.data[self.ptr])

    def pass_it(self):
        self.need_stop = False
        c = self.current_char()
        if c == ' ' or c == '\n' or c == '\t':
            return
        print("error at ", self.line, '(' + str(self.pos) + ')', " : ", c)
