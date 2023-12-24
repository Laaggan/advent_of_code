data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

data = open("data/8.txt", 'r').read()

instructions, positions = data.split("\n\n")
positions = positions.split("\n")

dict_positions = dict()
for position in positions:
    key, pos = position.split(" = ")
    L = pos[1:4]
    R = pos[6:9]
    dict_positions[key] = (L, R)

current_position = "AAA"
i = 0
while current_position != "ZZZ":
    current_instruction = instructions[i % len(instructions)]
    
    if current_instruction == "R":
        current_position = dict_positions[current_position][1]
    else:
        current_position = dict_positions[current_position][0]
    
    i += 1

print(i)
