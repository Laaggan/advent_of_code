data = '''0123
1234
8765
9876'''

data = '''...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9'''

data = '''..90..9
...1.98
...2..7
6543456
765.987
876....
987....'''

data = '''10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01'''

data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

data = open("2024/data/10.txt").read()

# data = [[int(x) for x in row] for row in data.split("\n")]
temp = []
for row in data.split("\n"):
    temp_row = []
    for c in row:
        if c.isnumeric():
            temp_row.append(int(c))
        else:
            temp_row.append(-1)
    temp.append(temp_row)

data = temp

N = len(data)
M = len(data[0])

def stringify(list_of_lists):
    return "\n".join(["".join(inner_list) for inner_list in list_of_lists])

def check_paths(data, i, j, v):
    next_val = v + 1
    continues = []

    #Debugging
    # print(next_val)
    # print(stringify(pretty_print))
    # print()

    if i + 1 < N:
        if data[i + 1][j] == next_val:
            if next_val == 9:
                trail_heads.add((i + 1, j))
            else:
                continues.append((i + 1, j))
        
    if i - 1 >= 0:
        if data[i - 1][j] == next_val:
            if next_val == 9:
                trail_heads.add((i - 1, j))
            else:
                continues.append((i - 1, j))
        
    if j + 1 < M:
        if data[i][j + 1] == next_val:
            if next_val == 9:
                trail_heads.add((i, j + 1))
            else:
                continues.append((i, j + 1))
        
    if j - 1 >= 0:
        if data[i][j - 1] == next_val:
            if next_val == 9:
                trail_heads.add((i, j - 1))
            else:
                continues.append((i, j - 1))
    
    for k, l in continues:
        pretty_print[k][l] = str(next_val)
    
    # Recursion is guaranteed to bottom out since data will contain values of maximum 9
    for k, l in continues:
        check_paths(data, k, l, next_val)

# Find starting points
result = 0
pretty_print=[["." for _ in range(M)] for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            trail_heads = set()
            pretty_print[i][j] = "0"
            check_paths(data, i, j, 0)
            result += len(trail_heads)

# print(stringify(pretty_print))

print(result)