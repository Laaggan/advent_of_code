from enum import Enum
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
# import numpy as np

with open("2025/data/5.txt") as file:
    real_data = file.read()

# LEFT_OVERLAP = 1
# RIGHT_OVERLAP = 2
# CONTAINED = 3
# FULLY_LEFT = 4
# FULLY_RIGHT = 5
VERBOSE = True
DATA_PLOT = True

class Overlap(Enum):
    LEFT = 1
    RIGHT = 2
    SUBSET = 3
    FULLY_LEFT = 4
    FULLY_RIGHT = 5
    SUPERSET = 6


class Range:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
    
    def __str__(self):
        return f"({self.lower},{self.upper})"
    
    def __eq__(self, value):
        return self.lower == value.lower and self.upper == value.upper

def determine_overlap_type(compared_to: Range, potential_overlap: Range):
    if compared_to.upper < potential_overlap.lower:
        return Overlap.FULLY_RIGHT
    else:
        return Overlap.RIGHT

def is_subset(compared_to: Range, potential_subset: Range):
    return compared_to.lower <= potential_subset.lower and potential_subset.upper <= compared_to.upper

def find_merge_candidate(i: int, merges: list[(int, int)], already_merged: set[int]):
    for j in range(i + 1, len(merges)):
        if merges[i][1] == merges[j][0]:
            already_merged.add(j)
            return find_merge_candidate(j, merges, already_merged)
    return i

def pretty_print_ranges(ranges: list[Range]):
    print([str(x) for x in ranges])

def ranges_to_line_collection(ranges: list[Range]):
    lines = []
    for i, range in enumerate(ranges):
        lines.append([(range.lower, i), (range.upper, i)])
    return mc.LineCollection(lines, linewidths=2)

def solution(data):
    ranges, ids = data.split("\n\n")
    ranges = [Range(*list(map(int, rang.split("-")))) for rang in ranges.split("\n")]
    
    # sort ranges
    ranges = sorted(ranges, key=lambda range: range.lower)

    # with open("2025/data/5_subset.txt", 'w+') as file:
    #     for range in ranges[23:33]:
    #         file.write(f"{range.lower}-{range.upper}\n")
                       
    if VERBOSE:
        print("Global min:", min(map(lambda x: x.lower, ranges)))
        print("Global max:", max(map(lambda x: x.upper, ranges)))
        
        print("Number of initial ranges:", len(ranges))
    
    if DATA_PLOT:
        fig, ax = plt.subplots()
        lc = ranges_to_line_collection(ranges)
        # ax.add_collection(lc)
        # ax.autoscale()
        # ax.margins(0.1)
        # plt.show()
    
    
    # Drop all subsets
    subset_indices = set()
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if is_subset(ranges[i], ranges[j]):
                subset_indices.add(j)
    if VERBOSE:
        print("Number of subsets to remove:", len(subset_indices))
    
    ranges_without_subsets: list[Range] = []
    for i in range(len(ranges)):
        if i not in subset_indices:
            ranges_without_subsets.append(ranges[i])
    
    if DATA_PLOT:
        lc2 = ranges_to_line_collection(ranges_without_subsets)
        # ax.add_collection(lc2)
        # ax.autoscale()
        # ax.margins(0.1)
        # plt.show()
        

    if len(ranges_without_subsets) == 1:
        return ranges_without_subsets

    merges = []
    for i in range(len(ranges_without_subsets)):
        for j in range(i + 1, len(ranges_without_subsets)):
            if determine_overlap_type(ranges_without_subsets[i], ranges_without_subsets[j]) == Overlap.FULLY_RIGHT:
                continue
            else:
                merges.append((i, j))
    if VERBOSE:
        print("Number merges to perform:", len(merges))
    
    # Reduce merges
    if len(merges) > 0:
        already_merged = set()
        reduced_merges = []
        for i in range(len(merges)):
            if i not in already_merged:
                merge_candidate = find_merge_candidate(i, merges, already_merged)

                if merge_candidate == i:
                    # means no merge found
                    reduced_merges.append(merges[i])
                else:
                    already_merged.add(merge_candidate)
                    reduced_merges.append((merges[i][0], merges[merge_candidate][1]))
        if VERBOSE:
            print("Number of merges to reduce:", len(reduced_merges))

        result = []
        for i in range(len(reduced_merges)):
            current_reduced_merge = reduced_merges[i]
            if i == 0:
                until_current = ranges_without_subsets[:current_reduced_merge[0]]
            else:
                previous_reduced_merge = reduced_merges[i-1]
                until_current = ranges_without_subsets[previous_reduced_merge[1]+1:current_reduced_merge[0]]
            
            reduced_range = Range(ranges_without_subsets[current_reduced_merge[0]].lower, ranges_without_subsets[current_reduced_merge[1]].upper)
            result.extend(until_current)
            result.append(reduced_range)

            if i == len(reduced_merges) - 1:
                until_end = ranges_without_subsets[current_reduced_merge[1]+1:]
                result.extend(until_end)
                
    else:
        result = ranges_without_subsets
    
    # pretty_print_ranges(result)
    if DATA_PLOT:
        lc3 = ranges_to_line_collection(ranges)
        # ax.add_collection(lc3)
        # ax.autoscale()
        # ax.margins(0.1)
        # plt.show()
    
    # Drop all subsets a second time which should not be needed
    # subset_indices = set()
    # for i in range(len(result)):
    #     for j in range(i + 1, len(result)):
    #         if is_subset(result[i], result[j]):
    #             subset_indices.add(j)
    # if VERBOSE:
    #     print("Number of subsets to remove:", len(subset_indices))
    
    # final_result: list[Range] = []
    # for i in range(len(result)):
    #     if i not in subset_indices:
    #         final_result.append(result[i])
    if DATA_PLOT:
        lc4 = ranges_to_line_collection(result)
        ax.add_collection(lc4)
        ax.autoscale()
        ax.margins(0.1)
        plt.show()

    return result

def calculate_result(result: list[Range]):
    calc = 0
    for rang in result:
        calc += rang.upper - rang.lower
    return calc

# print(calculate_result(solution(real_data)))

#356838475474683 is too high
#345821388686992 is too low
#300243640854356 is too low are you kidding me