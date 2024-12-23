data = open("2024/data/6.txt", 'r').read()
data = [[c for c in row] for row in data.splitlines()]

def find_startpoint(data):
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "^":
                return (i, j)
            
row,col = find_startpoint(data)

def calculate_next_direction(current_direction):
    if current_direction == 'UP':
        return 'RIGHT'
    elif current_direction == 'DOWN':
        return 'LEFT'
    elif current_direction == 'RIGHT':
        return 'DOWN'
    elif current_direction == 'LEFT':
        return 'UP'

def calculate_next_position(row, col, current_direction, data):
    terminated = False
    new_row, new_col = row, col
    if current_direction == 'UP':
        new_row -= 1
    elif current_direction == 'DOWN':
        new_row += 1
    elif current_direction == 'RIGHT':
        new_col += 1
    elif current_direction == 'LEFT':
        new_col -= 1
    
    if new_row < 0 or new_row > len(data) - 1 or new_col < 0 or new_col > len(data[0]) - 1:
        terminated = True
        return (new_row, new_col, current_direction, terminated)

    if data[new_row][new_col] == "#":
        current_direction = calculate_next_direction(current_direction)
        new_row, new_col, current_direction, terminated = calculate_next_position(row, col, current_direction, data)
    
    return (new_row, new_col, current_direction, terminated)

terminated = False
current_direction = 'UP'
visited_positions = set()
visited_positions.add((row, col))
mod_data = data
while not terminated:
    new_row, new_col, current_direction, terminated = calculate_next_position(row, col, current_direction, data)
    
    if not terminated:
        visited_positions.add((new_row, new_col))
        mod_data[new_row][new_col] = "X"
        row, col = new_row, new_col
    
for x in mod_data:
    print(str.join("", x))
    print("\n")

print(len(visited_positions))
    

        
