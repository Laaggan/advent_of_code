input_string = "input.txt"
data = open(input_string).read().split()
import matplotlib.pyplot as plt
import math


def parse_instruction(instruction):
    instruction_type = instruction[0]
    numeric_value = int(instruction[1:])
    return instruction_type, numeric_value


data = [parse_instruction(x) for x in data]

rot = 0
x, y = 0, 0
xs, ys = [x], [y]
res = []
for inst in data:
    # east will be positive and west will be negative
    # north will be positive and south will be negative

    if inst[0] == 'N':
        y += inst[1]
    elif inst[0] == 'S':
        y -= inst[1]

    if inst[0] == 'E':
        x += inst[1]
    elif inst[0] == 'W':
        x -= inst[1]

    # Seems like there is only multiples of 90 in rotation values which will result in integers
    if inst[0] == 'R':
        rot -= math.radians(inst[1])
    elif inst[0] == 'L':
        rot += math.radians(inst[1])

    if inst[0] == 'F':
        x += int(math.cos(rot)*inst[1])
        y += int(math.sin(rot) * inst[1])

    xs.append(x)
    ys.append(y)


print(abs(x) + abs(y))
plt.plot(xs, ys)
plt.show()