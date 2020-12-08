data = open('input.txt').read().split("\n")
data.pop()
data = [x.split() for x in data]

for i, x in enumerate(data):
    data[i][1] = int(x[1])

indices_visited = set()

terminated = False
accumulator = 0
ind = 0
while not terminated:
    op = data[ind][0]
    val = data[ind][1]

    if op == 'nop':
        ind += 1
    elif op == 'acc':
        accumulator += val
        ind += 1
    elif op == 'jmp':
        ind += val

    if ind in indices_visited:
        terminated = True
    else:
        indices_visited.add(ind)
print(accumulator)