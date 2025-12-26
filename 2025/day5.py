data = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

# with open("2025/data/5.txt") as file:
#     data = file.read()

def is_in_range(val, range):
    return val <= range[1] and val >= range[0]

# result = set()
# for id in ids:
#     for range in ranges:
#         if is_in_range(id, range):
#             print("id " + str(id) + " in " + str(range))
#             result.add(id)

# print(len(result))

def solution(data):
    ranges, ids = data.split("\n\n")
    ranges = [list(map(int, rang.split("-"))) for rang in ranges.split("\n")]
    ids = list(map(int, ids.split("\n")))

    ordered_ranges = None
    # all ranges must be placed in new list
    for i, rang in enumerate(ranges):
        if ordered_ranges:
            # therefore we need to loop over all ranges in the ordered list
            for j, ordered_range in enumerate(ordered_ranges):
                if is_in_range(rang[0], ordered_range):
                    # if we find that a range intersects a range in the ordered ranges
                    if j == len(ordered_ranges) - 1:
                        ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], rang[1]]]
                        continue
                    
                    # if we cant just naively merge the intersecting ranges start with the current ranges end
                    # we must loop forward and see in what range it ends
                    for k in range(j+1, len(ordered_ranges)):
                        if is_in_range(rang[1], ordered_ranges[k]):
                            # This means range j and k should become one
                            ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], ordered_ranges[k][1]], *ordered_range[k:]]
                            break
                        elif rang[1] >= ordered_ranges[k][1]:
                            max_merge = None
                        elif rang[1] < ordered_ranges[k][1]:
                            max_merge = k
                    if max_merge:
                        ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], ordered_ranges[max_merge][1]], *ordered_range[max_merge:]]
                    else:
                        ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], rang[1]]]
                # elif rang[1] > ordered_range[1]:
                #     continue
                elif rang[0] > ordered_range[1]:
                    # if we find that a range intersects a range in the ordered ranges
                    if j == len(ordered_ranges) - 1:
                        ordered_ranges = [*ordered_ranges[:j+1], rang]
                        continue
                    
                    # if we cant just naively merge the intersecting ranges start with the current ranges end
                    # we must loop forward and see in what range it ends
                    for k in range(j+1, len(ordered_ranges)):
                        if is_in_range(rang[1], ordered_ranges[k]):
                            # Then we don't need to merge and just put it in between
                            ordered_ranges = [*ordered_ranges[:j], rang, *ordered_range[k:]]
                elif is_in_range(rang[1], ordered_range):
                    # if we find that a range intersects a range in the ordered ranges
                    if j == 0:
                        ordered_ranges = [[rang[0], ordered_range[1]], *ordered_ranges[(j+1):]]
                        continue
                    
                    # if we cant just naively merge the intersecting ranges start with the current ranges end
                    # we must loop forward and see in what range it ends
                    for k in range(j+1, len(ordered_ranges)):
                        if is_in_range(rang[1], ordered_ranges[k]):
                            # This means range j and k should become one
                            ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], ordered_ranges[k][1]], *ordered_range[k:]]
            
        else:    
            ordered_ranges = [rang]

    return ordered_ranges


print(solution(data))
# Then we need to merge somehow
                # which we do by finding the intersecting end of the max
            
            #         elif range[1] <= ordered_ranges[k][0]:
            #             # this means that we get a new end of the range
            #             ordered_ranges = [*ordered_ranges[:j], range, *ordered_range[k:]]
            