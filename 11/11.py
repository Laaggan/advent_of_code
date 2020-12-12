import copy


def split_string(word):
    return [char for char in word]


def min_boundary(i):
    return max(0, i)


def max_boundary(i, n):
    return min(i, n - 1)


def generate_indices(p, num_rows, num_cols):
    row = p[0]
    col = p[1]

    points = []
    # horizontal line
    temp_points = []
    for i in range(0, num_cols):
        if i != col:
            temp_p = (row, i)
            temp_points.append(temp_p)
        else:
            temp_points.reverse()
            points.append(temp_points)
            temp_points = []
    points.append(temp_points)

    # vertical line
    temp_points = []
    for i in range(0, num_rows):
        if i != row:
            temp_p = (i, col)
            temp_points.append(temp_p)
        else:
            temp_points.reverse()
            points.append(temp_points)
            temp_points = []
    points.append(temp_points)

    # Quadrant 1
    i = 1
    temp_points = []
    while (row - i) >= 0 and (col + i) < num_cols:
        p_new = (row - i, col + i)
        temp_points.append(p_new)
        i += 1
    points.append(temp_points)

    # Quadrant 2
    i = 1
    temp_points = []
    while (row + i) < num_rows and (col + i) < num_cols:
        p_new = (row + i, col + i)
        temp_points.append(p_new)
        i += 1
    points.append(temp_points)

    # Quadrant 3
    i = 1
    temp_points = []
    while (col - i) >= 0 and (row + i) < num_rows:
        p_new = (row + i, col - i)
        temp_points.append(p_new)
        i += 1
    points.append(temp_points)

    # Quadrant 4
    i = 1
    temp_points = []
    while (col - i) >= 0 and (row - i) >= 0:
        p_new = (row - i, col - i)
        temp_points.append(p_new)
        i += 1
    points.append(temp_points)
    return points

data = open('input.txt').read().split()
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

                # punkterna kommer i fel ordning
                indices = generate_indices((i, j), h, w)
                for_debug = []
                for line_seg in indices:
                    for p in line_seg:
                        #assert p[0] != i and p[1] != j, 'Cant see yourself'
                        if temp_data[p[0]][p[1]] == 'L':
                            num_empty += 1
                            break
                        elif temp_data[p[0]][p[1]] == '#':
                            num_occupied += 1
                            break
                if data[i][j] == '.':
                    continue
                else:
                    if num_occupied == 0:
                        result[i][j] = '#'
                    elif num_occupied >= 5:
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

        for x in result:
            print(*x)

    tot_num_occupied = 0
    for i in range(h):
        for j in range(w):
            if result[i][j] == '#':
                tot_num_occupied += 1
    return tot_num_occupied


h = len(data)
w = len(data[0])
p_test = (4, 3)


points = generate_indices(p_test, h, w)
'''
for p in points:
    if data[p[0]][p[1]] != '#':
        data[p[0]][p[1]] = '*'

for x in data:
    print(x)
'''

# 2923 is too high
print("Number of occupied seats: ", new_sol(data))