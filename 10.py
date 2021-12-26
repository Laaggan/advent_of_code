#input_path = 'input/test_input_day_10.txt'
input_path = 'input/real_input_day_10.txt'

data = open(input_path).read().split("\n")
opening_chars = set(('(', '[', '{', '<'))
closing_chars = set((')', ']', '}', '>'))
char_connections = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

result = []
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
                break

final_result = 0
for x in result:
    final_result += points[x]

print(final_result)