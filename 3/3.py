from functools import reduce
data = open('input.txt').read().split("\n")
data.pop()

width = len(data[0])
x = 0
y = 0
curr_hit_trees = 0
hit_trees = []
xs = [1, 3, 5, 7, 1]
ys = [1, 1, 1, 1, 2]

for x_i, y_i in zip(xs, ys):
    while 0 < len(data):
        if y >= len(data) - 1:
            hit_trees.append(curr_hit_trees)
            break
        y += y_i
        x += x_i
        ind = x % width
        if data[y][ind] == '#':
            curr_hit_trees += 1
    curr_hit_trees = 0
    y, x = 0, 0

print(hit_trees)
result = reduce(lambda a, b: a*b, hit_trees)
print(result)