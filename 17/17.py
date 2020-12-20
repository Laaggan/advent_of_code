data = open('small_input.txt').read().split('\n')
data.pop()

# List comprehensions are cool
data = [[[c for c in x] for x in data]]

rows, cols, layers = len(data[0]), len(data[0][0]), len(data)


def truncate_indices(ind, n):
    if ind < 0:
        ind = 0
    elif ind >= n:
        ind = n - 1
    return ind


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


for i in range(layers):
    for j in range(rows):
        for k in range(cols):
            print(data[i][j][k])
            count_neighbours(data, (i, j, k))


