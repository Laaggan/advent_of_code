# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
from functools import reduce
import astar
import math

data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

data = open("data/12_real_data.txt").read()
data = data.split("\n")
n, m = len(data), len(data[0])

# Find start and end position
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if (c == 'S'):
            start_pos = (i, j)
        elif (c == 'E'):
            end_pos = (i, j)

# translate into numeric
numeric = [[0 for _ in range(m)] for _ in range(n)]
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if (i == start_pos[0] and j == start_pos[1]):
            numeric[i][j] = 0
        elif (i == end_pos[0] and j == end_pos[1]):
            numeric[i][j] = -1
        else:
            numeric[i][j] = ord(c) - ord('a')

num_max = max(list(map(max, numeric)))
numeric[end_pos[0]][end_pos[1]] = num_max

def generate_possible_point(row, col, row_count, col_count):
    possible_points = []
    if (row > 0):
        possible_points.append((row - 1, col))
    if (row < row_count - 1):
        possible_points.append((row + 1, col))
    if (col > 0):
        possible_points.append((row, col - 1))
    if (col < col_count - 1):
        possible_points.append((row, col + 1))
    return possible_points

def calculate_node_number(i, j, n, m):
    if (i > n or j > m):
        raise
    return i * m + j

# graph = [{str(a):{"neighbours": []}} for a in range(n*m)]
nodes = {}
for a in range(n*m):
    nodes[a] = {"neighbours": []}
for i, line in enumerate(numeric):
    for j, x in enumerate(line):
        possible_points = generate_possible_point(i, j, n, m)
        seq_num = calculate_node_number(i, j, n, m)
        for k, l in possible_points:
            if (numeric[k][l] - numeric[i][j] <= 1):
                neigh_num = calculate_node_number(k, l, n, m)
                nodes[seq_num]['neighbours'].append(neigh_num)
                nodes[seq_num]['row-col'] = (i, j)

def neighbors(n):
    return nodes[n]['neighbours']

def distance(n1, n2):
    if n2 in nodes[n1]['neighbours']:
        return 1
    else:
        return math.inf
        
start_node = calculate_node_number(start_pos[0], start_pos[1], n, m)
end_node = calculate_node_number(end_pos[0], end_pos[1], n, m)
path = list(astar.find_path(start=start_node, goal=end_node, neighbors_fnct=neighbors, distance_between_fnct=distance))
print(len(path)-1)

# print(path)
# def calculate_row(k, n, m):
#     return math.floor(k/m)

# def calculate_col(k, n, m):
#     return (k % m) - 1

# inc = 0
# pretty = [["." for _ in range(m)] for _ in range(n)]
# for k in path:
#     row = calculate_row(k, n, m)
#     col = calculate_col(k, n, m)
#     # pretty[row][col] = str(inc)
#     # inc += 1
#     pretty[row][col] = "*"

# for i in range(n):
#     temp = ""
#     for j in range(m):
#         temp += pretty[i][j]
#     print(temp)
# print(reduce(lambda a, b: a + b, pretty, ""))