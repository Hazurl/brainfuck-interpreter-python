from BrainfuckState import BrainfuckState

if __name__ == '__main__':
    bf = open("olc_challenge_9.bf").read()
    state = BrainfuckState()
    state.execute(bf)
