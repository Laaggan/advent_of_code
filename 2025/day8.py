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
    for j in range(i+1, len(boxes)):
        dist = calc_dist(boxes[i], boxes[j])
        distances.append((i, j, dist))

distances.sort(key=lambda x: x[2]) # sort on distance

def create_adjacency_matrix(num_nodes: int, distances: list[int]):
    adjacency = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for distance in distances:
        adjacency[distance[0]][distance[1]] = 1
        adjacency[distance[1]][distance[0]] = 1 # Do I need both pairs here? Yes!
    return adjacency

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

def part1(adjacency, calculate_group):
    groups = []
    seen = set()
    for i, row in enumerate(adjacency):
        if not any(row):
            continue
        if i in seen:
            continue
        group = set()
        seen.add(i)
        group.add(i)
        group = calculate_group(adjacency, row, group, seen)
        groups.append(group)

    result = list(map(len, groups))
    result.sort(reverse=True)
    return result
 
def update_adjacency(adjacency, distance):
    adjacency[distance[0]][distance[1]] = 1
    adjacency[distance[1]][distance[0]] = 1

# part 2
result2 = [None] #dummy value
i = NUM_DISTANCES + 1
adjacency2 = create_adjacency_matrix(len(boxes), distances[:NUM_DISTANCES])
while result2[0] != len(boxes):
    potential_solution = distances[i]
    update_adjacency(adjacency2, distances[i])
    i += 1
    result2 = part1(adjacency2, calculate_group)
    print(i, result2)

print(boxes[potential_solution[0]][0]*boxes[potential_solution[1]][0])
# part 1
# adjacency = create_adjacency_matrix(len(boxes), distances[:NUM_DISTANCES])
# result = part1(adjacency, calculate_group)
# final_result = 1
# for x in result[:3]:
#     final_result *= x
# print(final_result)

# 48 is not correct