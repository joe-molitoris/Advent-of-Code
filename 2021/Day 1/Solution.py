import typing

with open('Input.txt', "r") as f:
    supplied_input = f.readlines()
    supplied_input = [int(i.strip("\n")) for i in supplied_input]

sample_input = [199,200,208,210,200,207,240,269,260,263]

# Part 1
def count_increases(l:list) -> int:
    result = sum([True for i in range(1, len(l)) if l[i]>l[i-1]])
    return result

# Sample input validation
count_increases(sample_input)
# Solution
count_increases(supplied_input)

# Part 2
def count_increases3(l:list) -> int:
    sliding_window = [sum(l[i:i+3]) for i in range(len(l)-2)]
    return count_increases(sliding_window)

# Sample input validation
count_increases3(sample_input)
# Solution
count_increases3(supplied_input)

