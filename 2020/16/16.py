input_path = "input.txt"
data = open(input_path).read().split("\n\n")

data = [block.split("\n") for block in data]

# Parse rules
rules = {}
rules2 = []
for rule in data[0]:
    _rule = rule.split(": ")
    rule_name = _rule[0]
    rules[rule_name] = []

    ranges = _rule[1].split(" or ")
    ranges = [_range.split("-") for _range in ranges]

    set_ranges = [set(range(int(_range[0]), int(_range[1]) + 1)) for _range in ranges]
    rules2.append(set_ranges)

invalid_values = 0
res = []
tickets = data[2][1:]
tickets.pop()
for i, ticket in enumerate(tickets):
    ticket = [int(x) for x in ticket.split(',')]

    for j, param in enumerate(ticket):
        in_num_rules = 0
        for rule in rules2:
            if param in rule[0] or param in rule[1]:
                in_num_rules += 1
        if in_num_rules == 0:
            invalid_values += param
            res.append(param)
print(invalid_values)
print(res)
