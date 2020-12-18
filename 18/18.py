import re
from functools import reduce

small_input = "2 * 3 + (4 * 5)"
basic_input = "1 + 2 * 3 + 4 * 5 + 6"


def get_operator(_c):
    if _c == '+':
        return lambda a, b: a + b
    elif _c == '*':
        return lambda a, b: a * b

def sol_basic(_input):
    prev = []
    for c in _input:
        if bool(re.search("\d+", c)):
            prev.append(int(c))
            if len(prev) >= 2:
                prev = [reduce(f, prev)]
        elif bool(re.search("[*+]", c)):
            f = get_operator(c)
    return prev

def sol(_input):
    prev = []
    i = 0
    while i < len(_input):
        c = _input[i]
        if bool(re.search("\d+", c)):
            prev.append(int(c))
            if len(prev) >= 2:
                prev = [reduce(f, prev)]
        elif bool(re.search("[*+]", c)):
            f = get_operator(c)
        elif bool(re.search("[(]", c)):
            print(c, "left bracket")
            local_ind = re.search("[)]", _input[i:]).start()
            global_ind = i + local_ind
            print(i, local_ind, global_ind)
            new_exprs = _input[(i+1):global_ind]
            sub_sol = sol(new_exprs)
            new_input = _input[:i] + str(sub_sol) + _input[(global_ind+1):]
            _input = new_input
        i += 1
    value = prev[0]
    return value

#print(sol_basic(basic_input))
print(sol(small_input))