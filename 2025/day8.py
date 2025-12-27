# TODO: Move to utils
from functools import reduce


def pretty_print_number_matrix(number_matrix):
    print("\n".join(map("".join, map(str, number_matrix))) + "\n")

text = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

with open("2025/data/8.txt") as file:
    text = file.read()
NUM_DISTANCES = 1000

boxes = [list(map(int, row.split(","))) for row in text.split("\n")]

def calc_dist(p1, p2):
    result = 0
    for x1, x2 in zip(p1, p2):
        result += (x2 - x1)**2
    return result
distances = []
for i in range(len(boxes)):
    # print(i)
    for j in range(i+1, len(boxes)):
        dist = calc_dist(boxes[i], boxes[j])
        distances.append((i, j, dist))

distances.sort(key=lambda x: x[2]) # sort on distance
# print("should be 20^2", len(distances), 20**2)
# print(distances)
adjacency = [[0 for _ in range(len(boxes))] for _ in range(len(boxes))]

for distance in distances[:NUM_DISTANCES]:
    # print("dist:", distance)
    # print("boxes:", boxes[distance[0]], boxes[distance[1]])
    adjacency[distance[0]][distance[1]] = 1
    adjacency[distance[1]][distance[0]] = 1 # Do I need both pairs here?

# pretty_print_number_matrix(adjacency)

# Then we can recursively build the sub graphs?
def calculate_group(adjacency:list[list[int]], incoming: list[int], group: set[int], seen: set[int]):
    for idx, neigh in enumerate(incoming):
        if neigh == 0:
            continue
        
        if idx in seen:
            continue # Do nothing because we know it already exists in a graph
        else:
            seen.add(idx)
            group.add(idx)
            next_incoming = adjacency[idx]
            if not any(next_incoming): # If it has no connections we dont need to calc
                continue
            calculate_group(adjacency, next_incoming, group, seen)
    return group

def debug_groups(boxes, group):
    out = ""
    for idx in group:
        out += f"(idx: {idx}, point: {boxes[idx]}), "
    print(out)

groups = []
seen = set()
for i, row in enumerate(adjacency):
    # print("idx: ", i, [i for i, v in enumerate(row) if v > 0], f"({sum(row)})")
    if not any(row):
        continue
    if i in seen:
        continue
    group = set()
    seen.add(i)
    group.add(i)
    group = calculate_group(adjacency, row, group, seen)
    # debug_groups(boxes, group)
    groups.append(group)

# print(groups)
result = list(map(len, groups))
result.sort(reverse=True)
print(result)

final_result = 1
for x in result[:3]:
    final_result *= x

print(final_result)

# 48 is not correct