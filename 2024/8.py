from collections import defaultdict
from copy import deepcopy

data = open("data/8.txt").read()
data = [[c for c in row] for row in data.splitlines()]

frequency_positions = defaultdict(list)
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c != ".":
            frequency_positions[c].append((i,j))

def solution_1(data):
    anti_nodes = set()
    for frequency in frequency_positions.keys():
        positions = frequency_positions[frequency]
        for i, position_1 in enumerate(positions):
            for position_2 in positions:
                if position_1 == position_2:
                    continue

                diff = (position_1[0]-position_2[0], position_1[1]-position_2[1])
                
                anti_node_pos_1 = (position_1[0] + diff[0], position_1[1] + diff[1])
                if anti_node_pos_1[0] >= 0 and anti_node_pos_1[0] < len(data) and anti_node_pos_1[1] >= 0 and anti_node_pos_1[1] < len(data[0]):
                    anti_nodes.add(anti_node_pos_1)
                
                anti_node_pos_2 = (position_2[0] - diff[0], position_2[1] - diff[1])
                if anti_node_pos_2[0] >= 0 and anti_node_pos_2[0] < len(data) and anti_node_pos_2[1] >= 0 and anti_node_pos_2[1] < len(data[0]):
                    anti_nodes.add(anti_node_pos_2)
    return anti_nodes

def solution_2(data):
    anti_nodes = set()
    for frequency in frequency_positions.keys():
        positions = frequency_positions[frequency]
        for i, position_1 in enumerate(positions):
            anti_nodes.add(position_1)
            for position_2 in positions:
                if position_1 == position_2:
                    continue

                diff = (position_1[0]-position_2[0], position_1[1]-position_2[1])
                
                anti_node_pos_1 = (position_1[0] + diff[0], position_1[1] + diff[1])
                while anti_node_pos_1[0] >= 0 and anti_node_pos_1[0] < len(data) and anti_node_pos_1[1] >= 0 and anti_node_pos_1[1] < len(data[0]):
                    anti_nodes.add(anti_node_pos_1)
                    anti_node_pos_1 = (anti_node_pos_1[0] + diff[0], anti_node_pos_1[1] + diff[1])
                
                anti_node_pos_2 = (position_2[0] - diff[0], position_2[1] - diff[1])
                while anti_node_pos_2[0] >= 0 and anti_node_pos_2[0] < len(data) and anti_node_pos_2[1] >= 0 and anti_node_pos_2[1] < len(data[0]):
                    anti_nodes.add(anti_node_pos_2)
                    anti_node_pos_2 = (anti_node_pos_2[0] - diff[0], anti_node_pos_2[1] - diff[1])
    return anti_nodes

print(len(solution_1(data)))
anti_nodes = solution_2(data)
print(len(anti_nodes)) # 901 is too low

# mod_data = deepcopy(data)
# for node in anti_nodes:
#     if mod_data[node[0]][node[1]] == ".":
#         mod_data[node[0]][node[1]] = "#"

# for row in mod_data:
#     print("".join(row))
