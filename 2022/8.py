import numpy as np
input = """30373
25512
65332
33549
35390"""
input = open("data/8_real_data.txt").read()

data = [[c for c in x] for x in input.split("\n")]
data = np.array(data)

visible_trees_from_inside = 0
for i in range(1, data.shape[0] - 1):
    for j in range(1, data.shape[1] - 1):
        current_tree_height = data[i][j]
        # visible from left
        if max(data[i, :j]) < current_tree_height:
            visible_trees_from_inside += 1
            continue
        # visible from right
        if max(data[i, j+1:]) < current_tree_height:
            visible_trees_from_inside += 1
            continue
        # visible from top
        if max(data[:i, j]) < current_tree_height:
            visible_trees_from_inside += 1
            continue
        # visibile from bottom
        if max(data[i+1:, j]) < current_tree_height:
            visible_trees_from_inside += 1
            continue
        # print(data[i, :j], current_tree_height, data[i, j+1:])
        # print(data[:i, j], current_tree_height, data[i+1:, j])

visible_from_outside = 2*data.shape[0] + 2*(data.shape[1]-2)
visible_trees = visible_from_outside + visible_trees_from_inside
print(visible_trees)