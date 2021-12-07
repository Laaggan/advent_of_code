from functools import reduce
import numpy as np
#input_path = "input/test_input_day_5.txt"
input_path = "input/real_input_day_5.txt"
input_data = open(input_path).read().split("\n")
input_data = [x.split(" -> ") for x in input_data]
input_data = [[list(map(int, y.split(","))) for y in x] for x in input_data]

x_max, y_max = 0, 0
for points in input_data:
    for point in points:
        if point[0] > x_max:
            x_max = point[0]
        if point[1] > y_max:
            y_max = point[1]

result = np.zeros((x_max, y_max))

for point in input_data:
    x1, y1 = point[0]
    x2, y2 = point[1]
    x_max, x_min = max(x1, x2), min(x1, x2)
    y_max, y_min = max(y1, y2), min(y1, y2)

    if y1 == y2:
        result[y1, x_min:(x_max+1)] += 1
    if x1 == x2:
        result[y_min:(y_max+1), x1] += 1

print(len(result[result >= 2]))