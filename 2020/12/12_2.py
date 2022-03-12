input_string = "input.txt"
data = open(input_string).read().split()
import matplotlib.pyplot as plt
import math


def parse_instruction(instruction):
    instruction_type = instruction[0]
    numeric_value = int(instruction[1:])
    return instruction_type, numeric_value


data = [parse_instruction(x) for x in data]

b_x, b_y = 0, 0
w_x, w_y = 10, 1
# Maybe one should think in a different coordinate system instead
#rot = math.tan(1/10)
rot = 0
b_xs, b_ys = [b_x], [b_y]
w_xs, w_ys = [w_x], [w_y]
res = []
for inst in data:
    # east will be positive and west will be negative
    # north will be positive and south will be negative
    w_t_2 = math.pow(w_x, 2) + math.pow(w_y, 2)
    w_t = int(math.sqrt(w_t_2))

    if inst[0] == 'N':
        w_y += inst[1]
    elif inst[0] == 'S':
        w_y -= inst[1]

    if inst[0] == 'E':
        w_x += inst[1]
    elif inst[0] == 'W':
        w_x -= inst[1]

    # Seems like there is only multiples of 90 in rotation values which will result in integers
    if inst[0] == 'R':
        rot = -math.radians(inst[1])
        rel_w_x = (w_x - b_x)
        rel_w_y = (w_y - b_y)
        #TODO: This could be expressed as a function instead
        dwx = int(math.cos(rot) * rel_w_x - math.sin(rot) * rel_w_y)
        dwy = int(math.cos(rot) * rel_w_y + math.sin(rot) * rel_w_x)
        w_x = b_x + dwx
        w_y = b_y + dwy
    elif inst[0] == 'L':
        rot = math.radians(inst[1])
        rel_w_x = (w_x - b_x)
        rel_w_y = (w_y - b_y)
        dwx = int(math.cos(rot) * rel_w_x - math.sin(rot) * rel_w_y)
        dwy = int(math.cos(rot) * rel_w_y + math.sin(rot) * rel_w_x)
        w_x = b_x + dwx
        w_y = b_y + dwy

    if inst[0] == 'F':
        rel_w_x = (w_x - b_x)
        rel_w_y = (w_y - b_y)
        b_x += int(inst[1] * rel_w_x)
        b_y += int(inst[1] * rel_w_y)
        w_x = b_x + rel_w_x
        w_y = b_y + rel_w_y

    w_xs.append(w_x)
    w_ys.append(w_y)
    b_xs.append(b_x)
    b_ys.append(b_y)

    print("angle in radians: ", rot)
    print("instruction: ", inst)
    print("waypoint position:", w_x, w_y)
    print("boat position:", b_x, b_y)
    print()

# 60267 is too high
print("Manhattan distance: ", abs(b_x) + abs(b_y))
print("Manhattan distance to waypoint?: ", abs(w_x) + abs(w_y))
plt.plot(b_xs, b_ys, color='r')
plt.plot(w_xs, w_ys, color='b')
plt.show()