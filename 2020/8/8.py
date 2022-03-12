import copy

data = open('input.txt').read().split("\n")
data.pop()
data = [x.split() for x in data]

for i, x in enumerate(data):
    data[i][1] = int(x[1])


def old_solution(data):
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

        if ind in indices_visited or ind > (len(data) - 1):
            terminated = True
        else:
            indices_visited.add(ind)
    return accumulator, ind > (len(data) - 1)

def new_solution(data):
    i_res = -1
    for i, x in enumerate(data):
        split_data = copy.deepcopy(data)
        if x[0] == 'nop':
            split_data[i][0] = 'jmp'
            acc, res = old_solution(split_data)
        elif x[0] == 'jmp':
            split_data[i][0] = 'nop'
            acc, res = old_solution(split_data)
        else:
            continue
        if res:
            return acc, i


print(old_solution(data))
# index was 408 but accumulator was 1033
print(new_solution(data))