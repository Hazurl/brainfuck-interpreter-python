from BrainfuckState import BrainfuckState
import sys

if __name__ == '__main__':
    bf = open(sys.argv[1]).read()
    state = BrainfuckState()
    state.execute(bf)
