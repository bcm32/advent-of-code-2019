import sys


def add(a_idx, b_idx, out_idx):
    program[program[out_idx]] = program[program[a_idx]] + program[program[b_idx]]
    return


def multiply(a_idx, b_idx, out_idx):
    program[program[out_idx]] = program[program[a_idx]] * program[program[b_idx]]
    return


def write(mode, input, address):
    # TODO get correct mode
    program[address] = input


def custom_log(address):
    print("PROGRAM LOG: " + program[address])


def exit_program():
    print("-------- PROGRAM END ---------")
    print("Result: ", program[0], ", Noun & Verb : ", noun, verb)


def run():
    opcodes = {
        1: add,
        2: multiply,
        3: write,
        4: custom_log,
        99: exit_program
    }
    cursor = 0

    print(program)

    while cursor <= len(program):
        if (program[cursor]) == 99:
            exit_program()
            break

        # Pass indexes to operation
        # TODO: parse inputs & operation from program cursor
        operation = opcodes.get(program[cursor])
        try:
            # TODO variable inputs?, take tuple of (function, # input)?
            # TODO increment based on # of input + 1 instead of += 4
            operation(cursor + 1, cursor + 2, cursor + 3)
        except:
            print("An error in the program occurred")
            break
        cursor += 4  # move to the next opcode
    return program[0]


# RUN
fp = open('./input.txt', 'r')
original_state = list(map(lambda x: int(x), fp.read().split(",")))
program = original_state[:]

# Setup program state
program = original_state[:]
program[1] = noun
program[2] = verb

# Run and compare
program_result = run()
if program_result == goal:
    print("---------- MATCH -------------")
    print("Target: ", goal, ", Noun & Verb : ", noun, verb)
    sys.exit()
