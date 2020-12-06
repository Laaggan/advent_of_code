data = open('input.txt').read().split("\n\n")
data = [x.split() for x in data]

res = []
for group in data:
    unique = set()
    curr_res = 0
    for person in group:
        for c in person:
            if c not in unique:
                curr_res += 1
                unique.add(c)
    res.append(curr_res)
print(sum(res))