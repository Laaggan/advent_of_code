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

data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

data = open("data/8.txt", 'r').read()

instructions, positions = data.split("\n\n")
positions = positions.split("\n")

dict_positions = dict()
for position in positions:
    key, pos = position.split(" = ")
    L = pos[1:4]
    R = pos[6:9]
    dict_positions[key] = (L, R)

def solution_part_1():
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

def find_all_starting_positions(dict_positions: dict):
    result = []
    for key in dict_positions:
        if key[2] == "A":
            result.append(key)
    return result

def check_end_condition(current_positions):
    for position in current_positions:
        if position[2] != "Z":
            return True
    return False

def solution_part_2():
    current_positions = find_all_starting_positions(dict_positions)
    i = 0
    while check_end_condition(current_positions):
        if (i % 100 == 0):
            print("step:", i)
        current_instruction = instructions[i % len(instructions)]
        
        temp_current_positions = []
        for current_position in current_positions:
            if current_instruction == "R":
                temp_current_positions.append(dict_positions[current_position][1])
            else:
                temp_current_positions.append(dict_positions[current_position][0])
        current_positions = temp_current_positions
        i += 1
    print(i)

solution_part_2()