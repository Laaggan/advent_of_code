from collections import defaultdict
import copy

data = '''AAAA
BBCD
BBCC
EEEC'''

data = '''AACA
BAAA
BCAC'''

data = data.split("\n")

# region_counter = 0
# areas=defaultdict(set)
# symbols=defaultdict(str)
# perimeters=defaultdict(set)
# i, j = 0, 0
# N, M = len(data), len(data[0])
# continuation_index = [0 for _ in range(len(data))]

# def determine_perimeter(c, i, j):
#     pass

# while True:
#     current_symbol = data[i][j]
#     symbols[region_counter] = current_symbol
    
#     # Add perimeter when out of bounds
#     if i - 1 < 0:
#         perimeters[region_counter].add((i - 1, j))
#     elif i + 1 > N - 1:
#         perimeters[region_counter].add((i + 1, j))
#     if j - 1 < 0:
#         perimeters[region_counter].add((i, j - 1))
#     elif j + 1 > M - 1:
#         perimeters[region_counter].add((i, j + 1))
    
#     # Row handling
#     if i - 1 >= 0 and current_symbol != data[i - 1][j]:
#         perimeters[region_counter].add((i - 1, j))
#     elif i - 1 >= 0 and current_symbol == data[i - 1][j]:
#         areas[region_counter].add((i - 1, j))
#     if i + 1 <= N - 1 and current_symbol != data[i + 1][j]:
#         perimeters[region_counter].add((i + 1, j))
#     elif i + 1 <= N - 1 and current_symbol == data[i + 1][j]:
#         areas[region_counter].add((i + 1, j))
    
#     # Column handling
#     if j - 1 >= 0 and current_symbol != data[i][j - 1]:
#         perimeters[region_counter].add((i, j - 1))
#     elif j - 1 >= 0 and current_symbol == data[i][j - 1]:
#         areas[region_counter].add((i, j - 1))
    
#     if j + 1 <= M - 1 and current_symbol != data[i][j + 1]:
#         perimeters[region_counter].add((i, j + 1))
#         # If the next one is not the same we should go to next row and keep track of what column on current row we ended at
#         restart = j + 1
#     elif j + 1 <= M - 1 and current_symbol == data[i][j + 1]:
#         areas[region_counter].add((i, j + 1))

# print(areas)

class Interval:
    def __init__(self, character, row, start, end):
        self.character = character
        self.row = row
        self.start = start
        self.end = end
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
for i, row in enumerate(data):
    start, end = 0, 0
    for j, c in enumerate(row):
        if j == len(row) - 1 or (j + 1 <= len(row) - 1 and row[j + 1] != c):
            end = j
            intervals.append(Interval(c, i, start, end))
            result[i].append(Interval(c, i, start, end))
            start = j + 1
    
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

region_counter = 0
seen = set()
def count_area(interval):
    if (len(interval.parents) > 0):
        for parent in interval.parents:
            if parent not in seen:
                intermediate_sum += count_area(parent)
    if (len(interval.children) > 0):
        for child in interval.children:
            if child not in seen:
                intermediate_sum += count_area(child)
    else:
        region_counter += 1
        return interval.end - interval.start

for row in result:
    for interval in row:


