# X = Rock, Y = Paper, Z = Scissor
shape_values = {"X": 1, "Y": 2, "Z": 3}
translation = {"A": "X", "B": "Y", "C": "Z"}
rules = {"X": "Z", "Y": "X", "Z": "Y"}
win_rules = {"X": "Y", "Y": "Z", "Z": "X"}
lose_rules = {"X": "Z", "Y": "X", "Z": "Y"}

def solve_part_1():
    f = open("data/2_real_data.txt")
    data = list(map(lambda x: x.split(" "), f.read().split("\n")))

    score = 0
    for them, you in data:
        them = translation[them]
        if (you == them):
            score += shape_values[you] + 3
        elif rules[you] == them:
            score += shape_values[you] + 6
        else:
            score += shape_values[you]
    print(score)

def solve_part_2():
    f = open("data/2_real_data.txt")
    data = list(map(lambda x: x.split(" "), f.read().split("\n")))

    score = 0 
    for i, (them, you) in enumerate(data):
        them = translation[them]
        
        if (you == 'Y'):
            #draw
            you = them
            score += shape_values[you] + 3
        elif (you == 'X'):
            #lose
            you = lose_rules[them]
            score += shape_values[you]
        elif (you == 'Z'):
            #win
            you = win_rules[them]
            score += shape_values[you] + 6
    print(score)

solve_part_1()
solve_part_2()