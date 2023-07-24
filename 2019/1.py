from math import floor

data = open("data/1_r.txt", "r").read()
data = list(map(int, data.split("\n")))

def fuel_calculation(x):
    return floor(x/3) - 2

def solve_part_1():
    result = []
    for x in data:
        result.append(fuel_calculation(x))
    print(sum(result))

def solve_part_2():
    result = []
    for x in data:
        intermediate_result = 0
        value = fuel_calculation(x)
        intermediate_result += value
        while fuel_calculation(value) >= 0:
            value = fuel_calculation(value)
            intermediate_result += value
        result.append(intermediate_result)
    print(sum(result))

solve_part_2()
