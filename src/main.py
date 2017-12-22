from BrainfuckState import BrainfuckState

if __name__ == '__main__':
    bf = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    state = BrainfuckState()
    state.execute(bf)
