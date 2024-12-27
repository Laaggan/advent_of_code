import copy


data = open("2024/data/6_test.txt", 'r').read()
data = [[c for c in row] for row in data.splitlines()]

def find_startpoint(data):
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "^":
                return (i, j)

def find_obstructions(data):
    result = []
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "#":
                result.append((i, j))
    return result

def find_not_obstruction(data):
    result = []
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == ".":
                result.append((i, j))
    return result
            
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

def solve_part_1(row, col):
    terminated = False
    current_direction = 'UP'
    visited_positions = set()
    visited_positions.add((row, col))
    mod_data = copy.deepcopy(data)
    while not terminated:
        new_row, new_col, current_direction, terminated = calculate_next_position(row, col, current_direction, data)
        
        if not terminated:
            visited_positions.add((new_row, new_col))
            mod_data[new_row][new_col] = "X"
            row, col = new_row, new_col
        
    for x in mod_data:
        print(str.join("", x))
        print("\n")
    return visited_positions

# Using modulo of the index in this list should be nice
DIRECTION_CHAIN = ["UP", "RIGHT", "DOWN", "LEFT"]

def check_for_loop(check_row, check_col, loop_positions, dir_index):
    current_direction = DIRECTION_CHAIN[dir_index]
    original_direction = current_direction
    prev_direction = current_direction
    next_row, next_col = check_row, check_col
    change_count = 0
    terminated = False
    mod_data = copy.deepcopy(data)
    if next_row >= 0 and next_col >= 0 and next_row < len(mod_data) and next_col < len(mod_data[0]):
        mod_data[next_row][next_col] = "O"

    while not terminated:
        next_row, next_col, current_direction, terminated = calculate_next_position(next_row, next_col, current_direction, data)
        for x in mod_data:
                print(str.join("", x))
        print("\n")
        
        if not terminated: # just for debugging
            mod_data[next_row][next_col] = "|"

        if terminated:
            return loop_positions
        elif not terminated and current_direction != prev_direction:
            # expected_direction = DIRECTION_CHAIN[(dir_index + 1) % len(DIRECTION_CHAIN)]
            dir_index += 1
            change_count += 1
            prev_direction = current_direction
    
        if next_row == check_row and next_col == check_col and original_direction == current_direction:
            print("FOUND LOOP:", next_row, next_col)
            # print("CHANGE COUNT:", change_count % 3)
            # mod_data[check_row][check_col] = "^"
            # for x in mod_data:
            #     print(str.join("", x))
            # print("\n")
            loop_positions.add((check_row, check_col))
            return loop_positions

def solve_part_2():
    all_obstructions = find_not_obstruction(data)
    loop_positions = set()
    for obstruction in all_obstructions:
        # print("placement", obstruction)
        # guard to right of obstrcution going up
        dir_index = 0
        row, col = obstruction[0], obstruction[1] + 1
        loop_positions = check_for_loop(row, col, loop_positions, dir_index)

        # Guard below obstruction going left
        dir_index = 1
        row, col = obstruction[0] + 1, obstruction[1]
        loop_positions = check_for_loop(row, col, loop_positions, dir_index)
        
        # Guard left of obstruction going down
        dir_index = 2
        row,col = obstruction[0], obstruction[1] -1
        loop_positions = check_for_loop(row, col, loop_positions, dir_index)
        
        # Guard above obstruction going to the right
        dir_index = 3
        row,col = obstruction[0] - 1, obstruction[1]
        loop_positions = check_for_loop(row, col, loop_positions, dir_index)
    return loop_positions
    

# print(len(solve_part_1(row, col)))
print(len(solve_part_2()))
    

        
