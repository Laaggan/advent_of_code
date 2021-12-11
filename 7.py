import math
#input_path = "input/test_input_day_7.txt"
input_path = "input/real_input_day_7.txt"
data = list(map(int, open(input_path).read().split(',')))

result = []
for i in range(max(data)):
    cost = 0
    for x in data:
        cost += abs(i - x)
    result.append((i, cost))

min = math.inf
min_i = -1
for x in result:
    if x[1] < min:
        min = x[1]

print(min)