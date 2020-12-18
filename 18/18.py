import re
from functools import reduce

small_input = "2 * 3 + (4 * 5)"
basic_input = "1 + 2 * 3 + 4 * 5 + 6"


def get_operator(_c):
    if _c == '+':
        return lambda a, b: a + b
    elif _c == '*':
        return lambda a, b: a * b


prev = []
for c in basic_input:
    if bool(re.search("\d+", c)):
        prev.append(int(c))
        if len(prev) >= 2:
            prev = [reduce(f, prev)]
    elif bool(re.search("[*+]", c)):
        f = get_operator(c)
    if c != ' ':
        print(prev)