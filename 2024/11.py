from collections import defaultdict
from math import floor

data = "0 1 10 99 999"
data = "125 17"
data = "2 72 8949 0 981038 86311 246 7636740"
data = data.split(" ")

NUM_BLINKS = 75


result = defaultdict(int)
for stone in data:
    result[stone] += 1

for _ in range(NUM_BLINKS):
    updates = defaultdict(int)
    for stone, num_stones in result.items():
        if stone == "0":
            updates["1"] += num_stones
        elif len(stone) % 2 == 0:
            middle_stone = floor(len(stone)/2)
            left = str(int(stone[:middle_stone]))
            right = str(int(stone[middle_stone:]))

            updates[left] += num_stones
            updates[right] += num_stones
        else:
            updates[str(int(stone)*2024)] += num_stones
        
        # A stone will never not be transformed so we can safely always remove 1
        updates[stone] -= num_stones
    
    for update_key, update_value in updates.items():
        result[update_key] += update_value

sum = 0
for value in result.values():
    sum += value

print(sum)
