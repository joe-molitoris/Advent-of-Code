from typing import List
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def arrange_seating(data:List[str]) -> int:
    clean_data = ["."*len(data[0])]+data
    clean_data.append("."*len(data[0]))
    for i in range(len(clean_data)):
        clean_data[i] = "."+clean_data[i]+"."

    clean_data = [list(i) for i in clean_data]
    DATA_WIDTH = len(clean_data[1][:-1])

    while True:
        modified_data = deepcopy(clean_data)
        for i in range(1, len(clean_data)-1):
            for n in range(1, DATA_WIDTH):
                adjascent_status = [clean_data[i-1][n-1]!="#",
                                    clean_data[i-1][n]!="#",
                                    clean_data[i-1][n+1]!="#",
                                    clean_data[i][n-1]!="#",
                                    clean_data[i][n+1]!="#",
                                    clean_data[i+1][n-1]!="#",
                                    clean_data[i+1][n]!="#",
                                    clean_data[i+1][n+1]!="#"]
                if all(adjascent_status) and clean_data[i][n]=="L":
                    modified_data[i][n]="#"
                elif adjascent_status.count(False)>=4 and clean_data[i][n]=="#":
                    modified_data[i][n]="L"
        if modified_data == clean_data:
            break
        clean_data = deepcopy(modified_data)
    return len([s for sublist in modified_data for s in sublist if s == "#"])

# Solution pt. 1
arrange_seating(data)

