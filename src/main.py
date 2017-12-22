class BrainfuckState:
    def __init__(self):
        self.ptr = 0
        self.data = [0 for _ in range(100)]
        self.pos = 0
    
    def execute(self, text):
        self.text = text
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
