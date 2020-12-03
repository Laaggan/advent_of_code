data = open('input.txt').read().split("\n")
data.pop()

width = len(data[0])
x = 0
y = 0
hit_trees = 0
while 0 < len(data):
    if y >= len(data) - 1:
        break

    y += 1
    x += 3
    ind = x % width

    if data[y][ind] == '#':
        hit_trees += 1

print(hit_trees)