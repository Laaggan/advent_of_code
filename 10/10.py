import copy

data = list(map(lambda a: int(a), open('small_input.txt').read().split()))

temp_data = copy.deepcopy(data)
valid_below = [3]
valid_above = [1, 2, 3]
print(temp_data)

def set_of_valid_values(x, valid_below, valid_above):
    new_valid_below = set(map(lambda a: x - a, valid_below))
    new_valid_above = set(map(lambda a: x + a, valid_above))
    return new_valid_below, new_valid_above

_1jolt = 0
_3jolt = 0


def remove_data_point(data, value):
    x_ind = data.index(value)
    data.pop(x_ind)
    return data


for i in range(len(data)):
    if i == 0:
        x_curr = min(temp_data)
        assert x_curr in valid_above, "No valid first value"
        remove_data_point(temp_data, x_curr)
        _1jolt += 1
    else:
        valid_above, valid_below = set_of_valid_values(x_curr, valid_below, valid_above)
        for x in valid_above:
            if x in temp_data:
                x_curr = x
                remove_data_point(temp_data, x_curr)
                _1jolt += 1
                break
        for y in valid_below:
            if y in temp_data:
                x_curr = y
                remove_data_point(temp_data, x_curr)
                _3jolt += 1
                break

print(_1jolt, _3jolt)