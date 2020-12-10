with open("input.txt", "r") as f:
    data = f.read()

def count_unique_deliveries(directions:str)->int:
    '''
    Count number of houses that receive a package from Santa.
    '''
    # Sets starting coordinates at 0,0
    x,y = 0,0
    # Initialize a list that will contain sets of tuples including coordinates
    # Each tuple represents the house that recieved the delivery at direction[n]
    houses = [(x,y)]
    # Create a dict to decode the direction values as integers
    decode = {"^":1, "v":-1, "<":-1, ">":1}
    # For each direction, add a set of coordinates to the houses list
    for i in directions:
        if i in ["^", "v"]: 
            y+=decode[i]
            houses += [(x,y)]
        else:
            x+=decode[i]
            houses += [(x,y)]
    # Get number of houses by taking the length of the unique houses
    return len(set(houses))

def santa_robosanta(directions:str) -> int:
    santa_x,santa_y = 0,0
    robo_x,robo_y = 0,0
    santa_houses, robo_houses = [(santa_x,santa_y)], [(robo_x,robo_y)]
    decode = {"^":1, "v":-1, "<":-1, ">":1}
    for x,i in enumerate(directions, start=0):
        if x%2==0:
            if i in ["^", "v"]:
                santa_y+=decode[i]
                santa_houses += [(santa_x,santa_y)]
            else:
                santa_x+=decode[i]
                santa_houses += [(santa_x,santa_y)]
        else:
            if i in ["^", "v"]:
                robo_y+=decode[i]
                robo_houses += [(robo_x,robo_y)]
            else:
                robo_x+=decode[i]
                robo_houses += [(robo_x,robo_y)]
    return len(set(santa_houses+robo_houses))


# Solution pt. 1
count_unique_deliveries(data)

# Solution pt. 2
santa_robosanta(data)
