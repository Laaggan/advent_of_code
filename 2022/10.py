data = open("data/10_small_data.txt").read()
data = open("data/10_real_data.txt").read()
# data = """noop
# addx 3
# addx -5"""
data = data.split("\n")

NUM_CYCLES = {
    "addx": 2,
    "noop": 1
}

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