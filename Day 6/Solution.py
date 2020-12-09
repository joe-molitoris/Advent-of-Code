from typing import List
with open("input.txt") as f:
    answers = f.read()

def find_number_answers(answers:str)->int:
    '''
    Finds the number of answers indicating a 'yes' on the customs form 
    provided within each group.
    '''
    split_answers = answers.split("\n\n")
    clean_answers = [i.replace("\n", "") for i in split_answers]
    num_unique_answers = [len(set(i)) for i in clean_answers]
    return sum(num_unique_answers)

def everyone_answered(answers:str)->int:
    '''
    For each passenger group, this function finds the total number
    of questions that were answered by all members of the group.
    Then, it sums those numbers across all groups on the plane.
    '''
    group_answers = answers.split("\n\n")
    passenger_answers = [i.split("\n") for i in group_answers]
    unique_answers = [set(i.replace("\n", "")) for i in group_answers]

    result = []
    for un,pas in zip(unique_answers, passenger_answers):
        temp_result = []
        for u in un:
            temp_result.append(all([u in i for i in pas]))
        result.append(sum(temp_result))

    return sum(result)

# Solution pt. 1
find_number_answers(answers)

# Solution pt. 2
everyone_answered(answers)
