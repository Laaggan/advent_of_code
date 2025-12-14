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

# Case merge 2 ranges
data = '''3-5
4-10

1'''

# case add a non-intersecting range
data = '''3-5
6-10

1'''

# with open("2025/data/5.txt") as file:
#     data = file.read()

ranges, ids = data.split("\n\n")

ranges = [list(map(int, rang.split("-"))) for rang in ranges.split("\n")]
ids = list(map(int, ids.split("\n")))

def is_in_range(val, range):
    return val <= range[1] and val >= range[0]

# result = set()
# for id in ids:
#     for range in ranges:
#         if is_in_range(id, range):
#             print("id " + str(id) + " in " + str(range))
#             result.add(id)

# print(len(result))

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
                
                # if we cant just naively merge the intersecting ranges start with the current ranges end
                # we must loop forward and see in what range it ends
                for k in range(j+1, len(ordered_ranges)):
                    if is_in_range(rang[1], ordered_ranges[k]):
                        # This means range j and k should become one
                        ordered_ranges = [*ordered_ranges[:j], [ordered_range[0], ordered_ranges[k][1]], *ordered_range[k:]]
        
    else:    
        ordered_ranges = [rang]


print(ordered_ranges)
# Then we need to merge somehow
                # which we do by finding the intersecting end of the max
            
            #         elif range[1] <= ordered_ranges[k][0]:
            #             # this means that we get a new end of the range
            #             ordered_ranges = [*ordered_ranges[:j], range, *ordered_range[k:]]
            # elif range[0] > ordered_range[1] and range[1] < ordered_ranges[j + 1][0]:
            #     # Then we don't need to merge and just put it in between
            #     ordered_ranges = [*ordered_ranges[:j], range, *ordered_range[k:]]