import numpy as np
import matplotlib.pyplot as plt
path = 'input/test_input_day_15.txt'

small_data = """19999
19111
11191"""

data = np.array([[int(c) for c in a] for a in open(path).read().split('\n')])
#data = np.array([[int(c) for c in a] for a in small_data.split('\n')])

total_risk = data[0, 0]
table = dict()
table["0, 0"] = {"done": False, "dist": 0, "last_visited": None}

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if i == 0 and j == 0:
            continue
        else:
            table[f"{i}, {j}"] = {"done": False, "dist": np.Inf, "last_visited": None}
print(data)
print(table)


def get_neighborhood(i, j, shape, table):
    neighborhood = []
    if i - 1 > 0 and not table[f'{i - 1}, {j}']["done"]:
        neighborhood.append((i - 1, j))
    if i + 1 < shape[0] and not table[f'{i + 1}, {j}']["done"]:
        neighborhood.append((i + 1, j))
    if j - 1 > 0 and not table[f'{i}, {j - 1}']["done"]:
        neighborhood.append((i, j - 1))
    if j + 1 < shape[1] and not table[f'{i}, {j + 1}']["done"]:
        neighborhood.append((i, j + 1))
    return neighborhood


def all_nodes_visited(table):
    for key, value in table.items():
        if value['done'] is False:
            return False
    return True


def find_next_node(table):
    min_dist = np.Inf
    min_id = None
    for key, value in table.items():
        if value['dist'] < min_dist and not value['done']:
            min_dist = value['dist']
            min_id = key
    if min_id == None:
        return None, None
    i, j = map(int, min_id.split(', '))
    return i, j


def reconstruct_path(table, shape):
    i, j = shape[0] - 1, shape[1] - 1
    result = [(i, j)]
    while not (i == 0 and j == 0):
        prev_i, prev_j = map(int, table[f'{i}, {j}']['last_visited'].split(', '))
        result.append((prev_i, prev_j))
        i, j = prev_i, prev_j
    return result



count = 0
i, j = 0, 0
while not all_nodes_visited(table):
    neighborhood = get_neighborhood(i, j, data.shape, table)
    for neighbor in neighborhood:
        if i == 0 and j == 0:
            current_distance = data[neighbor[0], neighbor[1]]
        else:
            added_dist = table[f'{i}, {j}']['dist']
            current_distance = data[neighbor[0], neighbor[1]] + added_dist
        if current_distance < table[f'{neighbor[0]}, {neighbor[1]}']['dist']:
            table[f'{neighbor[0]}, {neighbor[1]}']['dist'] = data[neighbor[0], neighbor[1]]
            table[f'{neighbor[0]}, {neighbor[1]}']['last_visited'] = f'{i}, {j}'
    table[f'{i}, {j}']['done'] = True
    i, j = find_next_node(table)

shortest_path = reconstruct_path(table, data.shape)

visual = np.zeros(data.shape)
value = 0
for y, x in shortest_path:
    value += data[y, x]
    visual[y, x] = 1

print(value)
plt.imshow(visual)
plt.show()