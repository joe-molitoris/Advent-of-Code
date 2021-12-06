import typing

with open("input.txt", "r") as f:
    input_data = f.readlines()
    input_data = [i.strip("\n") for i in input_data]

sample_input = ["forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]

# Part 1
def find_coords(l:list) -> int:
    x,y = 0,0
    for i in l:
        direction = i.split(" ")
        direction[1] = int(direction[1])
        if direction[0] == "forward":
            x+=direction[1]
        elif direction[0] == "down":
            y+=direction[1]
        else:
            y-=direction[1]
    return x*y

# Sample validation
find_coords(sample_input)
# Solution
find_coords(input_data)

#  Part 2
def new_coord_system(l:list) -> int:
    x,y,aim = 0,0,0
    for i in l:
        direction = i.split(" ")
        direction[1] = int(direction[1])
        if direction[0] == "forward":
            x+=direction[1]
            y+=aim*direction[1]
        elif direction[0]=="down":
            aim+=direction[1]
        else:
            aim-=direction[1]
        print(direction, x,y,aim, x*y)
    return x*y

# Sample data validation
new_coord_system(sample_input)
# Solution
new_coord_system(input_data)