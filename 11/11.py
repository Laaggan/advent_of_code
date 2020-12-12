import copy


def split_string(word):
    return [char for char in word]


def min_boundary(i):
    return max(0, i)


def max_boundary(i, n):
    return min(i, n - 1)


data = open('small_input2.txt').read().split()
data = [split_string(x) for x in data]

def old_sol(data):
    h = len(data)
    w = len(data[0])
    temp_data = copy.deepcopy(data)
    result = copy.deepcopy(data)
    sol_found = False
    _iter = 0
    while not sol_found:
        alike = 0
        for i in range(h):
            for j in range(w):
                num_empty, num_occupied = 0, 0
                h_i1, h_i2 = min_boundary(i-1), max_boundary(i+1, h)
                w_i1, w_i2 = min_boundary(j-1), max_boundary(j+1, w)

                for k in range(h_i1, h_i2 + 1):
                    for l in range(w_i1, w_i2 + 1):
                        if k == i and l == j:
                            continue
                        else:
                            if temp_data[k][l] == 'L':
                                num_empty += 1
                            elif temp_data[k][l] == '#':
                                num_occupied += 1
                if data[i][j] == '.':
                    continue
                else:
                    if num_occupied == 0:
                        result[i][j] = '#'
                    elif num_occupied >= 4:
                        result[i][j] = 'L'

        for i in range(h):
            for j in range(w):
                if temp_data[i][j] == result[i][j]:
                    alike += 1

        if alike == w*h:
            sol_found = True

        temp_data = copy.deepcopy(result)
        print("iteration: ", _iter)
        _iter += 1

    tot_num_occupied = 0
    for i in range(h):
        for j in range(w):
            if result[i][j] == '#':
                tot_num_occupied += 1
    return tot_num_occupied

def new_sol(data):
    h = len(data)
    w = len(data[0])
    temp_data = copy.deepcopy(data)
    result = copy.deepcopy(data)
    sol_found = False
    _iter = 0
    while not sol_found:
        alike = 0
        for i in range(h):
            for j in range(w):
                num_empty, num_occupied = 0, 0
                h_i1, h_i2 = min_boundary(i-1), max_boundary(i+1, h)
                w_i1, w_i2 = min_boundary(j-1), max_boundary(j+1, w)

                # Loop over a pre-created list of indices instead?
                for k in range(h_i1, h_i2 + 1):
                    for l in range(w_i1, w_i2 + 1):
                        if k == i and l == j:
                            continue
                        else:
                            if temp_data[k][l] == 'L':
                                num_empty += 1
                            elif temp_data[k][l] == '#':
                                num_occupied += 1
                if data[i][j] == '.':
                    continue
                else:
                    if num_occupied == 0:
                        result[i][j] = '#'
                    elif num_occupied >= 4:
                        result[i][j] = 'L'

        for i in range(h):
            for j in range(w):
                if temp_data[i][j] == result[i][j]:
                    alike += 1

        if alike == w*h:
            sol_found = True

        temp_data = copy.deepcopy(result)
        print("iteration: ", _iter)
        _iter += 1

    tot_num_occupied = 0
    for i in range(h):
        for j in range(w):
            if result[i][j] == '#':
                tot_num_occupied += 1
    return tot_num_occupied


h = len(data)
w = len(data[0])
p_test = (4, 3)


def generate_indices(p, num_rows, num_cols):
    row = p[0]
    col = p[1]

    points = []
    # horizontal line
    for i in range(0, num_cols):
        if i != col:
            temp_p = (row, i)
            points.append(temp_p)

    # vertical line
    for i in range(0, num_rows):
        if i != row:
            temp_p = (i, col)
            points.append(temp_p)

    # Quadrant 1
    i = 1
    while (row - i) > 0 and (col + i) < num_cols:
        p_new = (row - i, col + i)
        points.append(p_new)
        i += 1

    # Quadrant 2
    i = 1
    while (row + i) < num_rows and (col + i) < num_cols:
        p_new = (row + i, col + i)
        points.append(p_new)
        i += 1

    # Quadrant 3
    i = 1
    while (col - i) > 0 and (row + i) < num_rows:
        p_new = (row + i, col - i)
        points.append(p_new)
        i += 1

    # Quadrant 4
    i = 1
    while (col - i) > 0 and (row - i) > 0:
        p_new = (row - i, col - i)
        points.append(p_new)
        i += 1
    return points

points = generate_indices(p_test, h, w)

for p in points:
    if data[p[0]][p[1]] != '#':
        data[p[0]][p[1]] = '*'

for x in data:
    print(x)

#print("Number of occupied seats: ", old_sol(data))