from termcolor import cprint

def if_char(char):
    def decorator(func):
        def get_char(_state):
            if char == _state.current_char():
                func(_state)
            return _state
        return get_char
    return decorator

@if_char('+')
def plus(_state):
    _state.set_value(_state.get_value() + 1)

@if_char('-')
def minus(_state):
    _state.set_value(_state.get_value() - 1)

@if_char('<')
def left(_state):
    _state.move(-1)

@if_char('>')
def right(_state):
    _state.move(1)

@if_char('.')
def out(_state):
    _state.print_value()

@if_char(',')
def ipt(_state):
    _state.set_value(int(input()))

@if_char('[')
def start_loop(_state):
    if _state.get_value() == 0:
        while _state.current_char() != ']':
            _state.advance(1)

@if_char(']')
def end_loop(_state):
    if _state.get_value()!= 0:
        while _state.current_char() != '[':
            _state.advance(-1)

def print_state_and_wait(_state):
    print(_state.current_char() + " : ", end='')
    _state.print_state()
    input()

def until_EOF(call, _state):
    if not _state.is_EOF():
        call(_state)
        _state.advance()
        until_EOF(call, state)

def chain(*funcs):
    def args(*a):
        for f in funcs:
            f(*a)
    return args

class State:
    def __init__(self, size, text):
        self.size = size
        self.ptr = 0
        self.data = [0 for _ in range(self.size)]
        self.pos = 0
        self.text = text

    def print_state(self):
        print('[', end='')
        first = True
        for i in range(self.size):
            if not first:
                print(', ', end='')
            first = False
            if self.ptr == i:
                cprint(str(self.data[i]), 'red', 'on_white', end='')
            else:
                print(str(self.data[i]), end='')
        print(']')

    def set_value(self, value):
        self.data[self.ptr] = value

    def get_value(self):
        return self.data[self.ptr]

    def move(self, delta):
        self.ptr += delta

    def print_value(self):
        print(chr(self.get_value()), end='')
        #print(str(self.get_value()), end='')

    def advance(self, delta=1):
        self.pos += delta

    def current_char(self):
        return self.text[self.pos]

    def is_EOF(self):
        return self.pos >= len(self.text)

if __name__ == '__main__':
    state = State(50, "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
    until_EOF(chain(start_loop, end_loop, plus, minus, left, right, out, ipt), state)
