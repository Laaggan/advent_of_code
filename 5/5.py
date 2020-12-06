from math import floor
data = open('input.txt').read().split()

n_rows = 128
n_cols = 8
res = []
for x in data:
    curr_ind_1 = n_rows/2
    range_size_1 = n_rows/2

    curr_ind_2 = n_cols/2
    range_size_2 = n_cols/2
    for c in x:
        if c == 'F':
            range_size_1 = range_size_1 / 2
            curr_ind_1 = curr_ind_1 - range_size_1
        elif c == 'B':
            range_size_1 = range_size_1 / 2
            curr_ind_1 = curr_ind_1 + range_size_1
        if c == 'L':
            range_size_2 = range_size_2 / 2
            curr_ind_2 = curr_ind_2 - range_size_2
        elif c == 'R':
            range_size_2 = range_size_2 / 2
            curr_ind_2 = curr_ind_2 + range_size_2
    row = floor(curr_ind_1)
    col = floor(curr_ind_2)
    curr_res = row*8 + col
    res.append(curr_res)
print(max(res))