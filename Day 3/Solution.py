from typing import Tuple, List

with open("input.txt") as f:
    layout = f.read().splitlines()

given_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def trees_encountered(l:List[str], slope:Tuple[int])  -> int:
    '''
    Count the number of trees, denoted as "#" one would encounter if
    one would descend the terrain with a given slope.

    Slope is a tuple of the form (x, y).
    '''
    new_layout = [i*5 for i in l]
    encountered = []
    x=0

    for i in range(0, len(new_layout), slope[1]):
        n = 1
        encountered.append(new_layout[i][x])
        x+=slope[0]
        try:
            while len(new_layout[i+slope[1]])<=x+slope[0]:
                new_layout[i+slope[1]] = new_layout[i+slope[1]]*2
        except:
            continue
    return encountered.count("#")


def find_product(x:List[int])  -> int:
    result = 1
    for i in x:
        result *= i
    return result

#Solution Pt. 1
trees_encountered(layout, (3,1))

#Solution Pt. 2
find_product([trees_encountered(layout, s) for s in given_slopes])