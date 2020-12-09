from typing import List

with open("input.txt") as f:
    moves = f.read().splitlines()

def clean_data(moves:List[str]) -> List[str]:
    '''
    Parse string into a list of lists and convert string integers to ints
    '''
    clean_moves = [i.split() for i in moves]
    for n in range(len(clean_moves)):
        clean_moves[n][1] = int(clean_moves[n][1].strip("+"))
    return clean_moves

# Setup data
clean_moves = clean_data(moves)

def accumulator_fill(moves:List[str]) -> int:
    '''
    Based on command rules: determine how much accumulator value is before any
    command is executed a second time.
    `nop`: no operation. Complete operation and move to next line.
    `acc`: add or subtract from accumulator. Complete and move to next line.
    `jmp`: jump to new line indicated by jump value.
    '''
    # Sets accumulator to 0 to start
    accumulator = 0
    # Creates a list of indices that will be used to determine exiting infinite loop
    ix = [0]
    # `N` is the current index
    N=0
    # An infinte loop that will append current indices to `ix` as long as
    # the number of elements in `ix` is unique (i.e. the loop has not repeated)
    while len(set(ix)) == len(ix):
        if clean_moves[N][0] == "jmp":
            N += clean_moves[N][1]
            ix += [N]
        elif clean_moves[N][0] == "acc":
            accumulator += clean_moves[N][1]
            N += 1
            ix += [N]
        elif clean_moves[N][0] == "nop":
            N+=1
            ix += [N]
    return accumulator


# Solution pt. 1
accumulator_fill(clean_moves)

# Solution pt.2
