import numpy as np
import matplotlib.pyplot as plt

#file = open("input/test_input_day_9.txt").read()
file = open("input/real_input_day_9.txt").read()
data = np.array([[int(c) for c in row] for row in file.split("\n")])

def star_1(data):
    low_points = 0
    low_points_matrix = np.zeros(data.shape)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            surrounding_values = []

            if i > 0:
                above = data[i - 1, j]
                surrounding_values.append(above)

            if i < data.shape[0] - 1:
                surrounding_values.append([i + 1, j])

            if j > 0:
                surrounding_values.append([i, j - 1])

            if j < data.shape[1] - 1:
                surrounding_values.append([i, j + 1])
    return surrounding_values


def get_neighborhood(i, j, data):
    surrounding_indices = []
    if i > 0:
        surrounding_indices.append([i - 1, j])

    if i < data.shape[0] - 1:
        surrounding_indices.append([i + 1, j])

    if j > 0:
        surrounding_indices.append([i, j - 1])

    if j < data.shape[1] - 1:
        surrounding_indices.append([i, j + 1])
    return surrounding_indices

def calc_basin(point, data, mask, enumeration):
    i, j = point
    neighborhood = get_neighborhood(i, j, data)

    for n_point in neighborhood:
        i1, j1 = n_point
        if data[i1, j1] == 9:
            continue
        elif data[i1, j1] > data[i, j]:
            mask[i1, j1] = enumeration
            calc_basin((i1, j1), data, mask, enumeration)

def star_2(data):
    mask = np.zeros(data.shape)
    low_points = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            neighborhood = get_neighborhood(i, j, data)

            larger_in_neighborhood = 0
            for point in neighborhood:
                i1, j1 = point
                if data[i, j] < data[i1, j1]:
                    larger_in_neighborhood += 1
            if larger_in_neighborhood == len(neighborhood):
                low_points.append((i, j))
                mask[i, j] = 1
    low_points = set(tuple(low_points))
    for i, point in enumerate(low_points):
        mask[point[0], point[1]] = i + 1
        calc_basin(point, data, mask, i + 1)

    result = []
    for i in range(len(low_points)):
        result.append(np.sum(np.sum(mask == i + 1)))

    result.sort(reverse=True)
    final_number = 1
    for i in range(3):
        final_number *= result[i]
    return final_number




print(star_2(data))
