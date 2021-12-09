import numpy as np

#file = open("input/test_input_day_9.txt").read()
file = open("input/real_input_day_9.txt").read()
data = np.array([[int(c) for c in row] for row in file.split("\n")])

low_points = 0
low_points_matrix = np.zeros(data.shape)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        surrounding_values = []

        if i > 0:
            above = data[i - 1, j]
            surrounding_values.append(above)

        if i < data.shape[0] - 1:
            below = data[i + 1, j]
            surrounding_values.append(below)

        if j > 0:
            left = data[i, j - 1]
            surrounding_values.append(left)

        if j < data.shape[1] - 1:
            right = data[i, j + 1]
            surrounding_values.append(right)

        res = 0
        for value in surrounding_values:
            if data[i, j] < value:
                res += 1

        if res == len(surrounding_values):
            low_points += data[i, j] + 1
            low_points_matrix[i, j] = 1

print(low_points)
