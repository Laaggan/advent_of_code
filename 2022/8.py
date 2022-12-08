import numpy as np
input = """30373
25512
65332
33549
35390"""
input = open("data/8_real_data.txt").read()

data = [[c for c in x] for x in input.split("\n")]
data = np.array(data)

def solve_part_1():
    visible_trees_from_inside = 0
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            current_tree_height = data[i,j]
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

    visible_from_outside = 2*data.shape[0] + 2*(data.shape[1]-2)
    visible_trees = visible_from_outside + visible_trees_from_inside
    print(visible_trees)

def solve_part_2():
    result = []
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            scenic_score = 1
            current_tree_height = data[i, j]
            # visible from left
            left_max = np.argmax(data[i, :j])
            if data[i, left_max] >= current_tree_height:
                scenic_score *= len(data[i, left_max:j])
            else:
                scenic_score *= len(data[i, :j])

            # visible from right
            right_max = np.argmax(data[i, j+1:])
            if data[i, (j + right_max + 1)] >= current_tree_height:
                scenic_score *= len(data[i, j:(j+right_max+1)])
            else:
                scenic_score *= len(data[i, j+1:])
            
            # visible from top            
            top_max = np.argmax(data[:i, j])
            if data[top_max, j] >= current_tree_height:
                scenic_score *= len(data[top_max:i, j])
            else:
                scenic_score *= len(data[:i, j])
            
            
            # visibile from bottom
            bottom_max = np.argmax(data[i+1:, j])
            if data[(i+bottom_max+1), j] >= current_tree_height:
                scenic_score *= len(data[(j + top_max + 1):j, j])
            else:
                scenic_score *= len(data[i+1:, j])
            
            
            result.append(scenic_score)
    print(max(result))

# solve_part_1()
solve_part_2()