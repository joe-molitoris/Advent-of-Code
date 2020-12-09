from typing import List

with open("input.txt") as f:
    l = f.read().splitlines()

def find_valid(l:List[str]) -> int:
    """
    Checks if password matched rule for given day. The rule states that the
    given letter should occur between x and y times in a password.

    Returns number of passwords matching criteria.
    """
    split_input = [i.split() for i in l]
    ranges = [split_input[n][0].split("-") for n in range(len(split_input))]

    for i in range(len(split_input)):
        split_input[i][0] = ranges[i]
        split_input[i][1] = split_input[i][1].strip(":")

    count = 0
    for i in split_input:
        if (i[2].count(i[1]) < int(i[0][0])) | (i[2].count(i[1]) > int(i[0][1])):
            count+=1

    return len(l)-count


def find_valid_new_rule(l:List[str]) -> int:
    """
    Checks if password matched rule for given day. The rule states that the
    given letter should occur at the xth or yth position, but not both.

    Returns number of passwords matching criteria.
    """
    split_input = [i.split() for i in l]
    ranges = [split_input[n][0].split("-") for n in range(len(split_input))]

    for i in range(len(split_input)):
        split_input[i][0] = ranges[i]
        split_input[i][1] = split_input[i][1].strip(":")

    count = 0
    for i in split_input:
        try:
            if ((i[2][int(i[0][0])-1]==i[1]) | (i[2][int(i[0][1])-1]==i[1])) & (i[2][int(i[0][1])-1] != i[2][int(i[0][0])-1]):
                count+=1
        except:
            continue
    return count

find_valid(l)
find_valid_new_rule(l)


