from math import floor
import numpy as np
input_path = "input.txt"
data = open(input_path).read().split("\n")
data.pop()
time_stamp = int(data[0])
org_ids = data[1].split(",")
ids = [int(id) for id in org_ids if id != 'x']
offset = [i for i, id in enumerate(org_ids) if id != 'x']
n = len(offset)

print(offset)

def sol(ids, time_stamp):
    sol_found = False
    curr_time_stamp = time_stamp
    num_true = 0
    while not sol_found:
        if curr_time_stamp % 1e5 == 0:
            print(curr_time_stamp)
        for id, off in zip(ids, offset):
            if (curr_time_stamp + off) % id == 0:
                num_true += 1
        if num_true == n:
            return curr_time_stamp
        curr_time_stamp += 1
        num_true = 0

this_sol = sol(ids, 100000000000000)
print(this_sol)
