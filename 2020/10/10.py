import copy

data = list(map(lambda a: int(a), open('input.txt').read().split()))

temp_data = copy.deepcopy(data)
start_valid = [1, 2, 3]
print(temp_data)


def set_of_valid_values(_x, _valid):
    new_valid = set(map(lambda a: _x + a, _valid))
    return new_valid


def remove_data_point(data, value):
    x_ind = data.index(value)
    data.pop(x_ind)
    return data

_1jolt = 0
_3jolt = 0

sol_found = False
i = 0
x_curr = 0
for x in range(len(data)):
    valid = set_of_valid_values(x_curr, start_valid)
    candidates = valid.intersection(temp_data)

    if len(candidates) == 1:
        new_x = next(iter(candidates))
        i_val = new_x - x_curr
        x_curr = new_x
        remove_data_point(temp_data, new_x)
    elif len(candidates) > 1:
        new_x = min(candidates)
        i_val = new_x - x_curr
        x_curr = new_x
        remove_data_point(temp_data, new_x)
    else:
        raise Exception('something went wrong')

    if i_val == 1:
        _1jolt += 1
    elif i_val == 3:
        _3jolt += 1
    else:
        raise Exception('Something went wrong')

print(temp_data)
# Why do I under count 1?
print(_1jolt, _3jolt + 1)
print(_1jolt*(_3jolt + 1))