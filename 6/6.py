from functools import reduce
data = open('input.txt').read().split("\n\n")
data = [x.split() for x in data]


def first_solution(data):
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
    return res


def second_solution(data):
    res = []
    for group in data:
        uniques = []
        for person in group:
            unique_in_person = set()
            for c in person:
                if c not in unique_in_person:
                    unique_in_person.add(c)
            uniques.append(unique_in_person)
        res_set = reduce(lambda a, b: a.intersection(b), uniques)
        res.append(len(res_set))
    return res

print(sum(first_solution(data)))
print(sum(second_solution(data)))
