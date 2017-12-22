from termcolor import colored, cprint

def print_(a):
    print(a, end='')

class BrainfuckState:
    def __init__(self, print_and_wait = False):
        self.print_and_wait = print_and_wait

    def execute(self, text):
        self.size = 20
        self.ptr = 0
        self.data = [0 for _ in range(self.size)]
        self.pos = 0
        self.text = text
        if self.print_and_wait:
            self.print_state()
            input()
        while self.pos < len(text):
            {
                '+' : self.plus,
                '-' : self.minus,
                '.' : self.opt,
                ',' : self.ipt,
                '>' : self.right,
                '<' : self.left,
                '[' : self.start_loop,
                ']' : self.end_loop
            }[text[self.pos]]()
            self.pos += 1
            if self.print_and_wait:
                self.print_state()
                input()


    def print_state(self):
        print_('[')
        first = True
        for i in range(self.size):
            if not first:
                print_(', ')
            first = False
            if self.ptr == i:
                cprint(str(self.data[i]), 'red', 'on_white', end='')
            else:
                print_(str(self.data[i]))
        print(']')

    def incr_cur(self, incr):
        self.data[self.ptr] += incr

    def incr_ptr(self, incr):
        self.ptr += incr

    def cur(self):
        return self.data[self.ptr]

    def plus(self):
        self.incr_cur(1)

    def minus(self):
        self.incr_cur(-1)

    def opt(self):
        print(chr(self.cur()), end='')

    def ipt(self):
        self.data[self.ptr] = input()

    def left(self):
        self.incr_ptr(-1)

    def right(self):
        self.incr_ptr(+1)

    def start_loop(self):
        if self.cur() == 0:
            while self.text[self.pos] != ']':
                self.pos += 1

    def end_loop(self):
        if self.cur() != 0:
            while self.text[self.pos] != '[':
                self.pos -= 1


if __name__ == '__main__':
    bf = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    state = BrainfuckState()
    state.execute(bf)
