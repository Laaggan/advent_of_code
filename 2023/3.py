data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

data = open("data/3.txt", 'r').read()

def is_digit(c):
    nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    return c in nums

def check_neighbourhood(data, i, j):
    pass

data = data.split("\n")

temp_number = ''
temp_number_positions = []
number_positions = []
symbol_positions = []
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if is_digit(c):
            temp_number += c
            temp_number_positions.append((i, j))
        elif len(temp_number) > 0 and c == '.':
            number = int(temp_number)
            temp_number = ''
            for pos in temp_number_positions:
                number_positions.append((number, pos))
            temp_number_positions = []
        elif c != '.':
            symbol_positions.append((c, (i, j)))

has_adjacent_symbol = set()
x = 0
for symbol in symbol_positions:
    y = 0
    print("Symbol: ", x)
    x += 1
    symbol_position = symbol[1]
    for number_position in number_positions:
        sym_i, sym_j = symbol_position
        for number in number_positions:
            number_value, number_position = number
            if (sym_i - 1, sym_j + 1) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i, sym_j + 1) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i + 1, sym_j + 1) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i - 1, sym_j) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i + 1, sym_j) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i - 1, sym_j - 1) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i, sym_j - 1) == number_position:
                has_adjacent_symbol.add(number_value)
            elif (sym_i + 1, sym_j - 1) == number_position:
                has_adjacent_symbol.add(number_value)

# all_numbers = set(map(lambda x: x[0], number_positions))
# no_adjacent_symbol = all_numbers - has_adjacent_symbol

print(sum(has_adjacent_symbol))
