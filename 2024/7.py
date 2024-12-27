from math import floor, log2

data = open("data/7.txt").read()
data = [(int(row[0]), list(map(int, row[1].split()))) for row in list(map(lambda x: x.split(": "), data.splitlines()))]

solution = set()
for i, row in enumerate(data):
    total_sum = row[0]
    values = row[1]
    n = 2**len(values)
    binary_tree = [0 for _ in range(n)]
    binary_tree[0] = values[0]
    for i in range(1, n):
        value_index = floor(log2(i))
        if i > 1:
            if i % 2 == 0:
                binary_tree[i-1] = binary_tree[i//2-1] + values[value_index]
            else:
                binary_tree[i-1] = binary_tree[i//2-1] * values[value_index]
        else:
            binary_tree[i-1] = values[0]
    for i in range(n//2-1, n):
        if binary_tree[i] == total_sum:
            solution.add(total_sum)

print(sum(solution))