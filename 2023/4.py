data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

data = open("data/4.txt", 'r').read()

# data = [[list(map(str.strip, y.split(" "))) for y in row.split(":")[1].split("|")] for row in data.split('\n')]
data = [row.split(":")[1].split("|") for row in data.split('\n')]
scratch_card = [row.strip().split() for row in map(lambda x: x[0], data)]
winning_numbers = [row.strip().split() for row in map(lambda x: x[1], data)]

total_points = 0
for i, (sc, wn) in enumerate(zip(scratch_card, winning_numbers)):
    # print(i + 1, sc, wn)
    # num_matches = 0
    added_points = 0
    for c1 in sc:
        for c2 in wn:
            if c1 == c2:
                if added_points == 0:
                    added_points = 1
                else:
                    added_points *= 2
    
    total_points += added_points

print(total_points)

    