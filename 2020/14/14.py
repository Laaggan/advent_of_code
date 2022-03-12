import re
from functools import reduce

input_path = "input.txt"
data = open(input_path).read().split("\n")
data.pop()
data = [x.split(" = ") for x in data]


def bin_to_int(string):
    return int(string, 2)


def int_to_bin(integer):
    return "{0:b}".format(integer)


def int_to_bin_const_bits(integer, num_bits):
    return format(integer, "b").zfill(num_bits)


result = {}
i_m = 0
for x in data:
    if x[0] == 'mask':
        mask = x[1]
        continue
    else:
        adress = x[0]
        value = int(x[1])

    curr_val = [c for c in int_to_bin_const_bits(value, len(mask))]
    for i, c in enumerate(mask):
        if c == '1':
            curr_val[i] = '1'
        elif c == '0':
            curr_val[i] = '0'
    curr_val = reduce(lambda a, b: a+b, curr_val)
    result[adress] = bin_to_int(curr_val)

_sum = 0
for key in result:
    _sum += result[key]

print(_sum)

