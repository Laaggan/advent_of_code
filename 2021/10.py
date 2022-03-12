from math import floor
#input_path = 'input/test_input_day_10.txt'
input_path = 'input/real_input_day_10.txt'

data = open(input_path).read().split("\n")
opening_chars = set(('(', '[', '{', '<'))
closing_chars = set((')', ']', '}', '>'))
char_connections = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {')': 1, ']': 2, '}': 3, '>': 4}

def star_1(data):
    result = []
    corrupted_rows = []
    for i, row in enumerate(data):
        char_dict = {'(': 0, '[': 0, '{': 0, '<': 0}
        opened_sequence = ''
        for j, c in enumerate(row):
            if c in opening_chars:
                char_dict[c] += 1
                last_opened = c
                opened_sequence = opened_sequence + c
            else:
                if len(opened_sequence) > 0 and c == char_connections[opened_sequence[-1]]:
                    opened_sequence = opened_sequence[0:(len(opened_sequence) - 1)]
                else:
                    result.append(c)
                    corrupted_rows.append(i)
                    break
    final_result = 0
    for x in result:
        final_result += points[x]
    return final_result, corrupted_rows

_, corrupted_rows = star_1(data)
rows_to_handle = set(range(0, len(data))).difference(corrupted_rows)

def star_2(data, rows_to_handle):
    result = []
    for i in rows_to_handle:
        row = data[i]
        opened_sequence = ''
        for j, c in enumerate(row):
            if c in opening_chars:
                opened_sequence = opened_sequence + c
            else:
                if len(opened_sequence) > 0 and c == char_connections[opened_sequence[-1]]:
                    opened_sequence = opened_sequence[0:(len(opened_sequence) - 1)]

        new_row = ''
        for c in opened_sequence[::-1]:
            new_row = new_row + char_connections[c]
        result.append(new_row)
    return result

star_2_result = star_2(data, rows_to_handle)

scores = []
for x in star_2_result:
    score = 0
    for c in x:
        score = score*5 + points2[c]
    scores.append(score)

scores.sort()
i = floor(len(scores)/2)
print(scores[i])