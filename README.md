# brainfuck-interpreter-python

This is a simple brainfuck program

## Usage

`python3 ./src/main.py <file>`

## Instructions

- `+`: Add 1 to the current cell
- `-`: Subtract 1 to the current cell
- `.`: Print the current value as a character encoded in ASCII
- `,`: Read from the input and write it to the current cell
- `>`: Move the pointer to the right
- `<`: Move the pointer to the left
- `[`: If the current cell is 0, jump to the corresponding closing bracket
- `]`: If the current cell is not 0, jump to the corresponding opening bracket
- `#`: Ignore instructions until next line
- `#:`: Ignore instructions until a `:#`
- `@`: Print the current value and the pointer
- `$`: Print the current state
- `%`: Start the step by step mode
- `!`: Stop the step by step mode
