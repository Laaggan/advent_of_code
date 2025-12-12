import copy

data = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

data = open("2025/data/4.txt").read()

def pretty_print_character_matrix(character_matrix):
    print("\n".join(map("".join, character_matrix)) + "\n")

data_result = [[c for c in x] for x in data.split("\n")]
neigh_vis = [[c for c in x] for x in data.split("\n")]
# data = data.split("\n")
data = [[c for c in x] for x in data.split("\n")]

NEIGHBOURHOOD = [(1,0),(1,1),(1,-1),
                 (0,1),(0,-1),
                 (-1,0),(-1,1),(-1,-1)]
N, M = len(data), len(data[0])

def is_paper_roll_accessible(data, row, col):
    result = 0
    neigh_vis[row][col] = "X"
    for diff in NEIGHBOURHOOD:
        curr_row = row + diff[0]
        curr_col = col + diff[1]

        if curr_row >= 0 and curr_row < N and curr_col >= 0 and curr_col < M:
            neigh_vis[curr_row][curr_col] = "o"
            if data[curr_row][curr_col] == "@":
                result += 1
        else:
            continue

    # pretty_print_character_matrix(neigh_vis)
    return result < 4

total_result = 0
intermediate_result = 1 # just to initialize the while loop
pretty_print_character_matrix(data)
while intermediate_result != 0:
    intermediate_result = 0
    mod_data = copy.deepcopy(data)
    for i in range(N):
    # for i in range(1, 2):
        for j in range(M):
        # for j in range(8, 9):
            if data[i][j] == "@":
                # Is paper roll
                if is_paper_roll_accessible(data, i, j):
                    mod_data[i][j] = "."
                    intermediate_result += 1
            else:
                continue
    data = mod_data
    total_result += intermediate_result
    # pretty_print_character_matrix(data)

# pretty_print_character_matrix(data_result)
print(total_result)