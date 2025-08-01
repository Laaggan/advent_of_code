from collections import defaultdict
import copy

data = '''AAAA
BBCD
BBCC
EEEC'''

# data = '''AACA
# BAAA
# BCAC'''

data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

# data = open("2024/data/12.txt").read()
data = data.split("\n")

class Interval:
    def __init__(self, character, row, enumeration, start, end):
        self.character = character
        self.row = row
        self.start = start
        self.end = end
        self.enumeration = enumeration
        self.parents = []
        self.children = []
    
    def __str__(self):
        return "Character: " +  self.character + ", Row: " + str(self.row) + ", Start: " + str(self.start) + ", End: " + str(self.end) + "\n Parents: " + str(self.parents) + "\n Children: " + str(self.children)

    def add_child(self, interval):
        self.children.append(interval)
    
    def add_parent(self, interval):
        self.parents.append(interval)


previous_intervals = None
region_interator = 0
result = [[] for _ in range(len(data))] # As many empty lists as rows

intervals = []
interval_enumerator = 0
for i, row in enumerate(data):
    start, end = 0, 0
    for j, c in enumerate(row):
        if j == len(row) - 1 or (j + 1 <= len(row) - 1 and row[j + 1] != c):
            end = j
            intervals.append(Interval(c, i, interval_enumerator, start, end))
            result[i].append(Interval(c, i, interval_enumerator, start, end))
            start = j + 1
            interval_enumerator += 1
    
    if i != 0:
        for v, interval1 in enumerate(result[i-1]):
            for q, interval2 in enumerate(result[i]):
                if interval1.character == interval2.character and not (interval1.start > interval2.end or interval1.end < interval2.start):
                    # If we have a match we want to set children to
                    interval1.add_child(interval2)
                    interval2.add_parent(interval1)

# for row in result:
#     for interval in row:
#         print(interval)

def count_area(interval, intermediate_sum, seen):
    if interval.enumeration in seen:
        return intermediate_sum
    else:
        seen.add(interval.enumeration)
    
    child_contribution, parent_contribution = 0, 0
    if (len(interval.parents) > 0):
        for parent in interval.parents:
            if parent.enumeration not in seen:
                parent_contribution += count_area(parent, intermediate_sum, seen)
    if (len(interval.children) > 0):
        for child in interval.children:
            if child.enumeration not in seen:
                child_contribution += count_area(child, intermediate_sum, seen)
    
    return interval.end - interval.start + 1 + intermediate_sum + parent_contribution + child_contribution

def count_perimeter(interval, previous_interval, intermediate_sum, seen):
    if interval.enumeration in seen:
        return intermediate_sum
    else:
        seen.add(interval.enumeration)
    
    child_contribution, parent_contribution = 0, 0
    if (len(interval.parents) > 0):
        for parent in interval.parents:
            if parent.enumeration not in seen:
                parent_contribution += count_perimeter(parent, interval, intermediate_sum, seen)
    if (len(interval.children) > 0):
        for child in interval.children:
            if child.enumeration not in seen:
                child_contribution += count_perimeter(child, interval, intermediate_sum, seen)
    
    s3 = set()
    if (previous_interval is not None):
        s1 = set(range(previous_interval.start, previous_interval.end + 1))
        s2 = set(range(interval.start, interval.end + 1))
        s3 = s1.intersection(s2)

    return 2*(interval.end - interval.start + 1) + 2 - 2*len(s3) + intermediate_sum + parent_contribution + child_contribution

roots = []
for row in result:
    for root in row:
        if len(root.parents) == 0:
            roots.append(root)

areas = [0 for _ in range(len(roots))]
global_seen = set()
true_roots = set()
for i, root in enumerate(roots):
    seen = set()
    if root.enumeration not in global_seen:
        print(root)
        areas[i] = count_area(root, 0, seen)
        global_seen = global_seen.union(seen)
        if (len(root.parents) == 0):
            true_roots.add(root.enumeration)
    else:
        print("Has already been seen")
        print(root)

perimeters = [0 for _ in range(len(roots))]
global_seen = set()
for i, root in enumerate(roots):
    seen = set()
    if root.enumeration not in global_seen:
        print(root)
        perimeters[i] = count_perimeter(root, None, 0, seen)
        global_seen = global_seen.union(seen)
    else:
        print("Has already been seen")
        print(root)

final_result = 0
for area, perimeter in zip(areas, perimeters):
    final_result += area*perimeter

print(final_result)
