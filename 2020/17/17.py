import copy

import numpy as np
data = open('small_input.txt').read().split('\n')
data.pop()

# List comprehensions are cool
data = [[[c for c in x] for x in data]]
data = np.array(data)
data = data == '#'

def create_initial_next_cycle(prev_data):
    layers, rows, cols = prev_data.shape
    next_cycle = np.zeros((layers + 2, rows + 2, cols + 2))
    layers, rows, cols = next_cycle.shape
    next_cycle[1:(layers-1), 1:(rows-1), 1:(cols-1)] = data
    return next_cycle

def truncate_indices(ind, n):
    if ind < 0:
        ind = 0
    elif ind >= n:
        ind = n - 1
    return ind


def create_neighbourhood():
    pass


def set_center_value(tensor, val):
    # Assuming 3D-tensors
    i1 = tensor.shape[0] / 2
    i2 = tensor.shape[1] / 2
    i3 = tensor.shape[2] / 2
    tensor[i1, i2, i3] = val
    return tensor

def count_neighbours(data, param):
    rows, cols, layers = len(data[0]), len(data[0][0]), len(data)
    num_neighbours = 0
    active, inactive = '#', '.'
    vals = (-1, 0, 1)
    i, j, k = param
    for l in vals:
        for m in vals:
            for n in vals:
                # Handles first cycle when it is two dimensional
                if layers == 1:
                    l == 0
                z = i + l
                y = j + m
                x = k + n

                # This solution will over count
                z = truncate_indices(z, layers)
                y = truncate_indices(y, rows)
                x = truncate_indices(x, cols)

                if z == i and y == j and z == k:
                    # We do not count the cell under evalutation
                    continue

                cell_value = data[z][y][x]
                if cell_value == active:
                    num_neighbours += 1
                elif cell_value == inactive:
                    pass
    pass


_iter = 0
data = create_initial_next_cycle(data)
while _iter < 6:
    next_data = copy.deepcopy(data)
    temp_data = copy.deepcopy(data)
    layers, rows, cols = data.shape
    for i in range(layers):
        for j in range(rows):
            for k in range(cols):
                #param = [[layers, i-1, i + 1], [rows, j-1, j + 1], [cols, k - 1, k + 1]]
                i1 = max(0, i-1)
                i2 = min(layers - 1, i + 1)
                j1 = max(0, j - 1)
                j2 = min(rows - 1, j + 1)
                k1 = max(0, k - 1)
                k2 = min(cols - 1, k + 1)

                cell_value = temp_data[i, j, k]
                # To not count the cell itself
                temp_data[i, j, k] = 0
                neighbourhood = temp_data[(i1):(i2+1), (j1):(j2+1), (k1):(k2+1)]
                temp_data[i, j, k] = cell_value
                num_neighbours = np.sum(neighbourhood)

                if cell_value == 1 and (num_neighbours == 2 or num_neighbours == 3):
                    next_data[i, j, k] = 1
                else:
                    next_data[i, j, k] = 0

                if cell_value == 0 and num_neighbours == 3:
                    next_data[i, j, k] = 1
    _iter += 1
    data = create_initial_next_cycle(next_data)

print(next_data.shape)
print(np.sum(np.sum(next_data)))