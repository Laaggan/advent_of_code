from math import floor


data = open("2024/data/5.txt", 'r').read()

rules, updates = data.split("\n\n")

rules = [x.split("|") for x in rules.split("\n")]
updates = [x.split(",") for x in updates.split("\n")]

priorities = {}
for value, rule in rules:
    if value in priorities.keys():
        value_set = priorities[value]
        value_set.add(rule)
        priorities[value] = value_set
    else:
        priorities[value] = set([rule])

result = []
for update in updates:
    not_allowed = set()
    seen = set()
    succesful = True
    for page_number in update:
        if page_number in priorities.keys():
            not_allowed_before = priorities[page_number]
        else:
            seen.add(page_number)
            continue

        intersection = seen.intersection(not_allowed_before)
        if len(intersection) > 0:
            result.append(False)
            succesful = False
            break

        seen.add(page_number)
    if succesful:
        result.append(True)

sum = 0
for i in range(len(result)):
    if result[i]:
       middle = floor(len(updates[i]) / 2)
       sum += int(updates[i][middle])
    else:
        continue

print(sum)