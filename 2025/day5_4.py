from enum import Enum
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
# import numpy as np

with open("2025/data/5.txt") as file:
    real_data = file.read()

# real_data = '''3-5
#     10-14
#     16-20
#     12-18

#     1
#     5
#     8
#     11
#     17
#     32'''

class Range:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
    
    def __str__(self):
        return f"({self.lower},{self.upper})"
    
    def __eq__(self, value):
        return self.lower == value.lower and self.upper == value.upper

def is_subset(compared_to: Range, potential_subset: Range):
    return compared_to.lower <= potential_subset.lower and potential_subset.upper <= compared_to.upper

def calculate_where_to_merge(i: int, ranges: list[Range]) -> tuple[int, int]:
    if i == len(ranges) - 1:
        return (ranges[i].upper, i + 1) # Need to add here to break the outer while loop
    next_i = i+1
    next_range = ranges[i+1]
    current_range = ranges[i]
    if current_range.upper < next_range.lower:
        return (current_range.upper, next_i)
    else:
        return calculate_where_to_merge(next_i, ranges)    
    

def pretty_print_ranges(ranges: list[Range]):
    print([str(x) for x in ranges])

def solution(data):
    ranges, ids = data.split("\n\n")
    ranges = [Range(*list(map(int, rang.split("-")))) for rang in ranges.split("\n")]
    
    # sort ranges
    ranges = sorted(ranges, key=lambda range: range.lower)

    # Drop all subsets
    subset_indices = set()
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if is_subset(ranges[i], ranges[j]):
                subset_indices.add(j)
    
    ranges_without_subsets: list[Range] = []
    for i in range(len(ranges)):
        if i not in subset_indices:
            ranges_without_subsets.append(ranges[i])

    ranges = ranges_without_subsets
    if len(ranges) == 1:
        return ranges
    
    i = 0
    result = []
    while i <= len(ranges) - 1:
        current_range = ranges[i]
        upper_next, i = calculate_where_to_merge(i, ranges)
        result.append(Range(current_range.lower, upper_next))

    return result

def calculate_result(result: list[Range]):
    calc = 0
    for rang in result:
        calc += rang.upper - rang.lower + 1
    return calc

print(calculate_result(solution(real_data)))

#356838475474683 is too high
#345821388687084 same as the one below but added 1 in the end calculation
#345821388686992 is too low
#300243640854356 is too low are you kidding me