from enum import Enum

# data = '''3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32'''

# data = '''3-5
# 10-14
# 1-2
# 1-4
# 4-6
# 3-4
# 3-5

# 1'''

# with open("2025/data/5.txt") as file:
#     data = file.read()

# LEFT_OVERLAP = 1
# RIGHT_OVERLAP = 2
# CONTAINED = 3
# FULLY_LEFT = 4
# FULLY_RIGHT = 5

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


def determine_overlap_type(compared: Range, ordered_range: Range):
    # What should happen in these cases if equal?
    if compared.upper < ordered_range.lower:
        return Overlap.FULLY_LEFT
    elif compared.lower > ordered_range.upper:
        return Overlap.FULLY_RIGHT
    elif compared.lower < ordered_range.lower and compared.upper <= ordered_range.upper:
        return Overlap.LEFT
    elif compared.lower >= ordered_range.lower and compared.upper > ordered_range.upper:
        return Overlap.RIGHT
    elif compared.lower >= ordered_range.lower and compared.upper <= ordered_range.upper:
        return Overlap.SUBSET
    elif compared.lower < ordered_range.lower and compared.upper > ordered_range.upper:
        return Overlap.SUPERSET

def is_in_range(val, range):
    return val <= range[1] and val >= range[0]

def solution(data):
    ranges, ids = data.split("\n\n")
    ranges = [Range(*list(map(int, rang.split("-")))) for rang in ranges.split("\n")]

    ordered_ranges = None
    # all ranges must be placed in new list
    for i, rang in enumerate(ranges):
        if ordered_ranges:
            j = 0
            merge_finalized = False
            for j in range(len(ordered_ranges)):
                if merge_finalized: 
                    break
                
                ordered_range = ordered_ranges[j]
                print(rang, ordered_range, determine_overlap_type(rang, ordered_range))
                overlap = determine_overlap_type(rang, ordered_range)

                if overlap == Overlap.SUBSET:
                    continue
                if overlap == Overlap.SUPERSET:
                    if j == len(ordered_ranges) - 1:
                        ordered_ranges = [*ordered_ranges[:j - 1], Range(rang.lower, rang.upper)]
                        break                    
                    ordered_ranges = find_end_range(ordered_ranges, rang, j, ordered_range)
                    merge_finalized = True
                elif overlap == Overlap.FULLY_LEFT:
                    pass
                elif overlap == Overlap.FULLY_RIGHT:
                    if j == len(ordered_ranges) - 1:
                        ordered_ranges.append(rang)
                        break
                    continue
                elif overlap == Overlap.LEFT:
                    ordered_ranges = [*ordered_ranges[:j], Range(rang.lower, ordered_range.upper), *ordered_ranges[j+1:]]
                    break
                elif overlap == Overlap.RIGHT:
                    if j == len(ordered_ranges) - 1:
                        ordered_ranges = [*ordered_ranges[:j], Range(ordered_range.lower, rang.upper)]
                        break
                    
                    ordered_ranges = find_end_range(ordered_ranges, rang, j, ordered_range)
                    merge_finalized = True
        else:
            ordered_ranges = [rang]

    return ordered_ranges

def find_end_range(ordered_ranges: list[Range], rang: Range, j: int, ordered_range: Range):
    for k in range(j + 1, len(ordered_ranges)):
        second_ordered_range = ordered_ranges[k]
        second_overlap = determine_overlap_type(rang, second_ordered_range)

        if second_overlap == Overlap.SUBSET:
            continue
        elif second_overlap == Overlap.SUPERSET:
            if k == len(ordered_ranges) - 1:
                # if previous_overlap == Overlap.RIGHT: # Can anything else happen?
                return [*ordered_ranges[:j], Range(ordered_range.lower, rang.upper)]
            continue
        elif second_overlap == Overlap.FULLY_LEFT:
            raise "A second overlap should not be able to be fully left"
        elif second_overlap == Overlap.FULLY_RIGHT:
            return [*ordered_ranges[:j-1], Range(ordered_range.lower, rang.upper), *ordered_ranges[k:]]
        elif second_overlap == Overlap.LEFT:
            return [*ordered_ranges[:j], Range(ordered_range.lower, second_ordered_range.upper), *ordered_ranges[(k+1):]]
        elif second_overlap == Overlap.RIGHT:
            raise "A second overlap should not be able to be right"

def pretty_print_ranges(ranges: list[Range]):
    print([str(x) for x in ranges])

def calculate_result(result: list[Range]):
    calc = 0
    for rang in result:
        calc += rang.upper - rang.lower
    return calc

calculate_result(solution(rea))
