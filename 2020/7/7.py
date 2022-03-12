import re

data = open('input.txt').read().split("\n")
data.pop()
n = len(data)
#expr = "(\d+ \w+ \w+|\w+ \w+)(?:( bags| bag))"
expr = "(\w+ \w+)(?:( bags| bag))"

start = 'shiny gold'
test = {'shiny gold': {}}
#sol = [['shiny gold'], ['muted yellow', 'bright white'], ['light red', 'dark orange']]
sol = [['shiny gold']]
sol_set2 = set()
found = False
k = 0
while not found:
    temp_sol = []
    children = sol[k]
    for i, child in enumerate(children):
        for j, y in enumerate(data):
            res = re.findall(expr, y)
            res = [y[0] for y in res]
            parent = res[0]

            if child in set(res[1:]):
                print(parent + " can hold " + child)
                temp_sol.append(parent)
                sol_set2.add(parent)
    if len(temp_sol) == 0:
        found = True
    else:
        sol.append(temp_sol)
        k += 1

sol_set = set()
res = 0
for x in sol[1:]:
    res += len(set(x))
    #sol_set.union(set(x))

# 181 is too high
print(res)
print(len(sol_set2))
