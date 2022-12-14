data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
data = open("C:/Users/llag/source/repos/advent_of_code/2022/data/9_real_data.txt").read()

data = [[x.split(" ")[0], int(x.split(" ")[1])] for x in data.split("\n")]

def moving_logic_for_head(x, y, direction):
    if direction == 'U':
        return (x, y + 1)
    elif direction == 'D':
        return (x, y - 1)
    elif direction == 'R':
        return (x + 1, y)
    elif direction == 'L':
        return (x - 1, y)

def moving_logic_for_tail(h_x, h_y, t_x, t_y):
    # If x or y is equal move only in one direction
    if (h_x == t_x and abs(h_y - t_y) > 1):
        if (h_y > t_y):
            return t_x, t_y + 1
        else:
            return t_x, t_y - 1
    elif (h_y == t_y and abs(h_x - t_x) > 1):
        if (h_x > t_x):
            return t_x + 1, t_y
        else:
            return t_x - 1, t_y

    if abs(h_x - t_x) <= 1 and abs(h_y - t_y) <= 1:
        return t_x, t_y

    # Every other case move diagonally
    if (t_x < h_x and t_y < h_y):
        return t_x + 1, t_y + 1
    elif (t_x < h_x and t_y > h_y):
        return t_x + 1, t_y - 1
    if (t_x > h_x and t_y > h_y):
        return t_x - 1, t_y - 1
    elif (t_x > h_x and t_y < h_y):
        return t_x - 1, t_y + 1
    
    return t_x, t_y

def solve_part_1():
    current_direction = None
    x_h, y_h, x_t, y_t = 0, 0, 0, 0

    has_been = set()
    for direction, count in data:
        current_direction = direction
        for i in range(count):
            x_h, y_h = moving_logic_for_head(x_h, y_h, current_direction)
            x_t, y_t = moving_logic_for_tail(x_h, y_h, x_t, y_t)
            has_been.add((x_t, y_t))
        
    print(len(has_been))

def solve_part_2():
    tail_size = 9
    current_direction = None
    x_h, y_h = 0, 0
    tail = [(0, 0) for _ in range(tail_size)]
    has_been = set()
    
    for direction, count in data:
        current_direction = direction
        for i in range(count):
            x_h, y_h = moving_logic_for_head(x_h, y_h, current_direction)
            for i, (x_t_curr, y_t_curr) in enumerate(tail):
                if i == 0:
                    x_t, y_t = moving_logic_for_tail(x_h, y_h, x_t_curr, y_t_curr)
                else:
                    x_t_before, y_t_before = tail[i-1]
                    x_t, y_t = moving_logic_for_tail(x_t_before, y_t_before, x_t_curr, y_t_curr)
                tail[i] = (x_t, y_t)
                if i == len(tail) - 1:
                    has_been.add((x_t, y_t))
    print(len(has_been))
    
solve_part_2()