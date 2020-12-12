import copy


def split_string(word):
    return [char for char in word]


def min_boundary(i):
    return max(0, i)


def max_boundary(i, n):
    return min(i, n - 1)


data = open('input.txt').read().split()
data = [split_string(x) for x in data]

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

print("Number of occupied seats: ", tot_num_occupied)