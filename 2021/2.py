#input_path = "input/test_input_day_2.txt"
input_path = "input/real_input_day_2.txt"
file = open(input_path).read().split("\n")
input_data = [x.split(" ") for x in file]


def star_1(data):
    x, y = 0, 0
    for row in data:
        direction = row[0]
        value = int(row[1])

        if direction == "forward":
            x += value
        elif direction == "up":
            y -= value
        elif direction == "down":
            y += value
    return x*y


def star_2(data):
    horizontal, depth, aim = 0, 0, 0
    for row in data:
        direction = row[0]
        value = int(row[1])

        if direction == "forward":
            horizontal += value
            depth += value * aim
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
    return horizontal*depth


print(star_1(input_data))
print(star_2(input_data))