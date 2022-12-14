from math import floor


data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

data = open("data/11_real_data.txt").read()
data = data.split("\n\n")

parsed_data = {}
for i, monkey in enumerate(data):
    monkey = monkey.split("\n")
    for j, line in enumerate(monkey):
        if j != 0:
            left, right = line.split(":")
        else:
            parsed_data[i] = {"items_handled": 0}
            continue
        
        left = left.strip()
        if (left == "Starting items"):
            items = list(map(int, right.strip().split(", ")))
            if (len(items) == 1):
                # items = [items]
                pass
            parsed_data[i]["items"] = items
        elif (left == "Operation"):
            _, operation = right.split("=")
            operation = operation.strip().split(" ")
            parsed_data[i]["operation"] = operation
        elif (left == "Test"):
            parsed_data[i]["condition"] = int(right.split(" ")[-1])
        elif (left == "If true"):
            parsed_data[i]["true"] = int(right.split(" ")[-1])
        elif (left == "If false"):
            parsed_data[i]["false"] = int(right.split(" ")[-1])

# print(parsed_data)

def do_operation(operation, current_worry_level):
    operand1, operator, operand2 = operation
    if operand1 == "old":
        operand1 = current_worry_level
    else:
        operand1 = int(operand1)
    
    if operand2 == "old":
        operand2 = current_worry_level
    else:
        operand2 = int(operand2)

    if (operator == "*"):
        return operand1 * operand2
    #okay only since there is only 2 operators
    else:
        return operand1 + operand2

def check_condition(condition, worry_level):
    return worry_level % condition == 0

NUM_ROUNDS = 20
NUM_MONKEYS = len(parsed_data)
for i in range(NUM_ROUNDS):
    for monkey_index in range(NUM_MONKEYS):
        monkey = parsed_data[monkey_index]
        for item in monkey["items"]:
            new_worry_level = do_operation(monkey["operation"], item)
            new_worry_level = floor(new_worry_level / 3)
            condition = check_condition(monkey["condition"], new_worry_level)

            if (condition):
                send_to_monkey = monkey["true"]
            else:
                send_to_monkey = monkey["false"]
            
            parsed_data[monkey_index]["items_handled"] += 1
            parsed_data[send_to_monkey]["items"].append(new_worry_level)
        parsed_data[monkey_index]["items"] = []

handled_items_list = list(map(lambda x: parsed_data[x]["items_handled"], parsed_data))
handled_items_list.sort(reverse=True)
print(handled_items_list[:2][0]*handled_items_list[:2][1])