with open("input.txt", "r") as f:
    data = f.read()

def find_floor(data:str) -> int:
    start=0
    return sum([1 if i =="(" else -1 for i in data])

def enters_basement(data:str) -> int:
    '''
    Determine the index of the move in which Santa enters basement.
    '''
    # Keeps track of current floor
    current_floor=0
    # Defines the character values
    code = {"(":1, ")":-1}
    # Creates list of tuples with the position and character value
    translation = list(enumerate([code[i] for i in data], start=1))
    # Loops over characters until the basement is reached
    for i in translation:
        current_floor+=i[1]
        if current_floor<0:
            return i[0]

# Solution pt. 1
find_floor(data)

# Solution pt. 2
enters_basement(data)