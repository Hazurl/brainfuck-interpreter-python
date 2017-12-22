def plus(data, ptr, text, pos):
    data[ptr] = data[ptr] + 1
    return data, ptr, pos

def minus(data, ptr, text, pos):
    data[ptr] = data[ptr] - 1
    return data, ptr, pos

def opt(data, ptr, text, pos):
    print(chr(data[ptr]), end='')
    return data, ptr, pos

def ipt(data, ptr, text, pos):
    data[ptr] = input()
    return data, ptr, pos

def left(data, ptr, text, pos):
    return data, ptr - 1, pos

def right(data, ptr, text, pos):
    return data, ptr + 1, pos

def start_loop(data, ptr, text, pos):
    if data[ptr] == 0:
        while text[pos] != ']':
            pos = pos + 1
    return data, ptr, pos

def end_loop(data, ptr, text, pos):
    if data[ptr] != 0:
        while text[pos] != '[':
            pos = pos - 1
    return data, ptr, pos

def execute (text):
    data = [0 for _ in range(100)]
    ptr = 10
    pos = 0

    while pos < len(text):
        data, ptr, pos = {
            '+' : plus,
            '-' : minus,
            '.' : opt,
            ',' : ipt,
            '>' : right,
            '<' : left,
            '[' : start_loop,
            ']' : end_loop
        }[text[pos]](data, ptr, text, pos)
        pos = pos + 1


if __name__ == '__main__':
    bf = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    execute(bf)
