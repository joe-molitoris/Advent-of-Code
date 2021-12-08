with open("input.txt", "r") as f:
    input_data = f.readlines()

with open("sample_input.txt","r") as f:
    sample_input = f.readlines()

sample_draws = sample_input[0].strip("\n")
sample_draws = sample_draws.split(",")

sample_boards = sample_input[1:]
for i in range(len(sample_boards)):
    if sample_boards[i]=="\n": continue
    else: sample_boards[i] = sample_boards[i].split("\n")

result = []
for i in range(1, len(sample_boards),6):
    result.append(sample_boards[i:i+5])

