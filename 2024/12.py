from collections import defaultdict

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

previous_intervals = None
region_interator = 0
result = defaultdict(list)
for i, row in enumerate(data[:2]):
    intervals = []
    start, end = 0, 0
    for j, c in enumerate(row):
        if j == len(row) - 1 or (j + 1 < len(row) - 1 and row[j + 1] != c):
            end = j
            intervals.append((c, start, end))
            start = j + 1
    
    if previous_intervals is None:
        # If first time just set previous_intervals
        # for c, start, end in intervals:
        #     result[c] = [(i, start, end)]
        previous_intervals = intervals
    else:
        # Merge
        already_merged = [False for _ in range(len(intervals))]
        for c1, start1, end1 in previous_intervals:
            for q, (c2, start2, end2) in enumerate(intervals):
                if c1 == c2 and not (start1 > end2 or end1 < start2):
                    if already_merged[q]:
                        result[c1].append((c2, start2, end2))
                    else:
                        already_merged[q] = True
                        # In this case it shall be added to some other region if it is disjoint
                        result[c1]


print(result)