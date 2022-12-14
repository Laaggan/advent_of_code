data = open("data/10_small_data.txt").read()
data = open("data/10_real_data.txt").read()
data = data.split("\n")

NUM_CYCLES = {
    "addx": 2,
    "noop": 1
}

def solution_part_1():
    registry = 1
    clock_cycles = 0

    result = []
    for op in data:
        if op == "noop":
            value = None
        else:
            op, value = op.split(" ")
            value = int(value)
        
        for i in range(NUM_CYCLES[op]):
            clock_cycles += 1

            if (clock_cycles == 20):
                result.append(clock_cycles * registry)
            elif ((clock_cycles + 20) % 40 == 0):
                result.append(clock_cycles * registry)
        if (value):
            registry += value
        elif (clock_cycles > 220):
            break

    print(sum(result))

def logic_sprite_visibility(sprite_pos, clock_cycles):
    x = clock_cycles % 40
    if sprite_pos == x:
        return "#"
    elif sprite_pos == x - 1:
        return "#"
    elif sprite_pos == x + 1:
        return "#"
    else:
        return "."

def solution_part_2():
    registry = 1
    clock_cycles = 0

    result = ""
    current_crt_row = ""
    for op in data:
        if op == "noop":
            value = None
        else:
            op, value = op.split(" ")
            value = int(value)
        
        for _ in range(NUM_CYCLES[op]):
            current_crt_row += logic_sprite_visibility(registry, clock_cycles)
            clock_cycles += 1
            if (clock_cycles % 40 == 0):
                result += current_crt_row + "\n"
                current_crt_row = ""
        if (value):
            registry += value

    print(result)

solution_part_2()