input_path = "small_input.txt"
data = open(input_path).read().split("\n\n")

data = [block.split("\n") for block in data]

# Parse rules
rules = {}
for rule in data[0]:
    _rule = rule.split(": ")
    rule_name = _rule[0]
    rules[rule_name] = []

    ranges = _rule[1].split(" or ")
    ranges = [_range.split("-") for _range in ranges]

    set_ranges = [set(range(int(_range[0]), int(_range[1]) + 1)) for _range in ranges]
    print(set_ranges)
