import copy

def split_string(word):
    return [char for char in word]

data = open('small_input.txt').read().split()
data = [split_string(x) for x in data]

# One can index into strings like below
# print(data[0][1])

h = len(data)
w = len(data[0])

print(h, w)
def min_boundary(i):
    return max(0, i)

def max_boundary(i, n):
    return min(i, n - 1)

temp_data = copy.deepcopy(data)
result = copy.deepcopy(data)
sol_found = False
while not sol_found:
    alike = 0
    for i in range(h):
        for j in range(w):
            num_empty, num_occupied = 0, 0
            h_i1, h_i2 = min_boundary(i-1), max_boundary(i+1, h)
            w_i1, w_i2 = min_boundary(j-1), max_boundary(j+1, w)

            for k in range(h_i1, h_i2):
                for l in range(w_i1, w_i2):
                    if k == i and l == j:
                        continue
                    else:
                        if temp_data[k][l] == 'L':
                            num_empty += 1
                        elif temp_data[k][l] == '#':
                            num_occupied += 1

            if num_occupied == 0:
                result[i][j] = '#'
            elif num_occupied >= 4:
                result[i][j] = 'L'
    temp_data = copy.deepcopy(result)
    for i in range(h):
        for j in range(w):
            if data[i][j] == result[i][j]:
                alike += 1
            print(result[i][j])
        print("\n")
    print("\n")

    if alike == w*h:
        sol_found = True