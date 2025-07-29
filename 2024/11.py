import copy
from math import floor

data = "0 1 10 99 999"
data = "125 17"
data = "2 72 8949 0 981038 86311 246 7636740"
data = data.split(" ")

NUM_BLINKS = 25

for _ in range(NUM_BLINKS):
    new_data = copy.deepcopy(data)
    i = 0
    while i < len(new_data):
        stone = new_data[i]

        if stone == "0":
            new_data[i] = "1"
        elif len(stone) % 2 == 0:
            middle_stone = floor(len(stone)/2)
            left = str(int(stone[:middle_stone]))
            right = str(int(stone[middle_stone:]))

            # middle_sequence = floor(len(new_data)/2)
            new_data = [*new_data[:i], left, right, *new_data[i+1:]]
            i += 1
        else:
            new_data[i] = str(int(stone)*2024)
        
        i += 1
    data = new_data

print(len(data))
