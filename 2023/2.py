from enum import Enum

data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

data = open("data/2.txt", 'r').read()

games = [x.split(":") for x in data.split("\n")]
games = [x[1].split(";") for x in games]
games = [[[z.split(" ") for z in list(map(str.strip, y.split(",")))] for y in x] for x in games]

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

max_values = dict({
    "red": 12,
    "green": 13,
    "blue": 14
})

def solution_part_1(data):
    result = set()
    for i, game in enumerate(games):
        index = i + 1
        possible = True
        for draw in game:
            for value in draw:
                number = int(value[0])
                color = value[1]
                if number > max_values[color]:
                    possible = False
        if possible:
            result.add(index)
    print(sum(result))

def solution_part_2(data):
    result = []
    for i, game in enumerate(games):
        index = i + 1
        max_red = 0
        max_green = 0
        max_blue = 0
        for draw in game:
            for value in draw:
                number = int(value[0])
                color = value[1]
                if color == 'red' and number > max_red:
                    max_red = number
                elif color == 'green' and number > max_green:
                    max_green = number
                elif color == 'blue' and number > max_blue:
                    max_blue = number
        result.append(max_red*max_green*max_blue)
    print(sum(result))

solution_part_2(data)