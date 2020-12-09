from typing import List

with open("input.txt" ,"r") as f:
    tickets = f.read().splitlines()


def get_seat_id(ticket_number:str, only_ID:bool = True) -> int:
    '''
    Obtain seat ID number based on the seat location.
    '''
    start, stop = 0, 127
    start_col, stop_col = 0, 7
    row_result, col_result = [], []

    for i in ticket_number:
        if i=="F":
            stop = ((start+stop)//2)
            row_result.append((start,stop))
        if i=="B":
            start = ((start+stop)//2)+1
            row_result.append((start,stop))
        if i=="L":
            stop_col = ((start_col + stop_col)//2)
            col_result.append((start_col, stop_col))
        if i=="R":
            start_col = ((start_col+stop_col)//2)+1
            col_result.append((start_col, stop_col))

    seat_id = row_result[-1][0]*8 + col_result[-1][0]
    if only_ID==False:
        return (row_result[-1][0], col_result[-1][0])
    return seat_id

def find_my_seat(ticket_list:List[str]) -> int:
    '''
    Finds the seat that does not have a ticket assigned to it.
    '''
    all_seat_ids = [r*8+c for c in range(0,7) for r in range(1,127)]
    seats = [get_seat_id(i, only_ID=False) for i in ticket_list]
    rows = {r:sorted([c[1] for c in seats if c[0]==r]) for r in set([i[0] for i in seats])}
    my_row = [i for i in rows if len(rows[i])==7]
    my_seat = [i for i in range(0,8) if i not in rows[my_row[0]]]
    return my_row[0]*8+my_seat[0]

# Solution pt. 1
result = [get_seat_id(i) for i in tickets]
max(result)

# Solution pt .2
seats = [get_seat_id(i) for i in tickets]
my_seat = find_my_seat(tickets)
my_seat
assert (my_seat+1 in seats) and (my_seat-1 in seats)