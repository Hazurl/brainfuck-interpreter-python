from BrainfuckState import BrainfuckState

if __name__ == '__main__':
    bf = open("test.bf").read()
    state = BrainfuckState()
    state.execute(bf)
    print()
