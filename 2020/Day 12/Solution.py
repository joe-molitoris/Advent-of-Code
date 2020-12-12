from typing import List

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def find_distance(data:List[str]) -> int:
    direction_multiplier = {"N":1,"S":-1,"E":1, "W":-1}
    current_direction = 'E'
    # Starting rotation dict from perspective of E and clockwise rotation
    rotations = {0:"E", 90:"S", 180:"W", 270:"N"}
    # Tuple of directions
    directions = ("E", "S", "W", "N")
    # Starting Position [x,y]
    position = [0, 0]
    # Loop through each instruction
    for i in data:
        # If instruction states to move forward, it either adds to x or y
        # depending on current direction
        if i[0]=="F":
            if current_direction in ["E", "W"]:
                position[0]+=int(i[1:])*direction_multiplier[current_direction]
            elif current_direction in ["N", "S"]:
                position[1]+=int(i[1:])*direction_multiplier[current_direction]
        # If instruction states E or W shift, add to the x position
        elif i[0] in ["W", "E"]:
            position[0]+= int(i[1:])*direction_multiplier[i[0]]
        # If instruction states a N or S shift, add to y position
        elif i[0] in ["N", "S"]:
            position[1]+= int(i[1:])*direction_multiplier[i[0]]
        # If instruction indicates a rotation, get the index of the current direction
        # from the direction tuple. 
        ## Then, re-order the keys of the rotations dict so that
        ## the degrees are relative to the current direction (i.e. current direction = 0)
        elif i[0] in ["R", "L"]:
            direction_ix = directions.index(current_direction)
            if i[0]=="R":
                rotations_r = list(directions)[direction_ix:]+list(directions)[:direction_ix]
                rotations_r = dict(zip(rotations.keys(), rotations_r))
                rotations2 = rotations_r
            # When rotation direction is LEFT, rotation keys will be 360 - rotation key
            # This signifies the counter-clockwise degrees of rotation.
            else:
                rotations_l = list(directions)[direction_ix:]+list(directions)[:direction_ix]
                rotations_l = dict(zip([360-i for i in rotations.keys()], rotations_l))
                rotations2 = rotations_l
            # Assign current direction to be equal to the newly determined direction
            current_direction = rotations2[int(i[1:])]
    # Return the sum of the absolute values of x and y
    return abs(position[0]) + abs(position[1])

# Solution pt. 1
find_distance(data)