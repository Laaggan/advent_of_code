from collections import defaultdict
from math import floor


data = open("2024/data/5.txt", 'r').read()

rules, updates = data.split("\n\n")

rules = [x.split("|") for x in rules.splitlines()]
updates = [x.split(",") for x in updates.splitlines()]

priorities = defaultdict(list)
for value, rule in rules:
    priorities[value].append(rule)

result = []
sum1 = 0
sum2 = 0
for update in updates:
    not_allowed = set()
    seen = set()
    succesful = True
    
    sorted_update = sorted(update, key=lambda page: -len([order for order in priorities[page] if order in update]))
    if sorted_update == update:
        sum1 += int(sorted_update[len(sorted_update) // 2])
    else:
        sum2 += int(sorted_update[len(sorted_update) // 2])

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

print(sum1)
print(sum2)
