from typing import List

def find_multiply(l:List[int]) -> int:
    """
    Find the product of two numbers of a list that add up to 2020
    """
    a = [2020-i for i in l]
    result = [i for i in l if i in a]
    return result[0]*result[1]

def find_three(l:List[int]) -> int:
    """
    Find the product of three numbers of a list that add up to 2020
    """
    a = [2020 - b - c for b in l for c in l]
    result = [i for i in l if i in a]
    return result[0]*result[1]*result[2]


with open("input.txt", "r") as f:
    supplied_input =f.readlines()
    x=[int(i.strip("\n")) for i in supplied_input]

find_multiply(x)
find_three(x)
