from math import floor
import matplotlib.pyplot as plt
data = open("data/14_small_data.txt", 'r').read()
data = open("data/14_real_data.txt", 'r').read()
data = [[list(map(int, y.split(","))) for y in x.split(" -> ")] for x in data.split("\n")]

walls = set()
sand_pebbles = set()

for segment in data:
    for i in range(1, len(segment)):
        point1 = segment[i - 1]
        point2 = segment[i]

        # True -> move horizontally, False -> move vertically
        is_horizontal = None
        value1, value2 = None, None
        if point1[0] != point2[0]:
            is_horizontal = True
            value1, value2 = point1[0], point2[0]
        elif point1[1] != point2[1]:
            is_horizontal = False
            value1, value2 = point1[1], point2[1]
        
        line_length = value2 - value1
        # True -> move right, False -> move left or True -> move up, False -> move down
        move_positive = None
        if line_length > 0:
            move_positive = True
        else:
            move_positive = False

        new_point = point1
        for j in range(abs(line_length) + 1):
            
            if move_positive:
                step = j
            else:
                step = -j

            if is_horizontal:
                new_point = (point1[0] + step, point1[1])
            else:
                new_point = (point1[0], point1[1] + step)
            
            walls.add(new_point)

def sand_move_logic(pebble, pebbles, walls):
    new_pebble = (pebble[0], pebble[1] + 1)
    
    if new_pebble in pebbles or new_pebble in walls:
        left_pebble = (pebble[0] - 1, pebble[1] + 1)
        right_pebble = (pebble[0] + 1, pebble[1] + 1)

        if left_pebble not in pebbles and left_pebble not in walls:
            return left_pebble
        elif right_pebble not in pebbles and right_pebble not in walls:
            return right_pebble
        else:
            return pebble
    else:
        #This means that the pebble has stopped
        return new_pebble

def get_y_max(walls):
    return max(map(lambda x: x[1], walls))

def add_infinite_floor(walls, y_max):
    #TODO: This 300 is just arbitrary and could probably be smaller
    max_width = 300 + 2*y_max
    for x in range(max_width):
        walls.add((500 + (x - floor(max_width/2)), y_max + 2))
    return walls

def draw_state(walls, pebbles):
    xs = [p[0] for p in walls]
    ys = [p[1] for p in walls]
    plt.scatter(xs, ys)
    xs = [p[0] for p in pebbles]
    ys = [p[1] for p in pebbles]
    plt.scatter(xs, ys)
    plt.gca().invert_yaxis()
    plt.show()

def solve_part_1():
    y_max = get_y_max(walls)
    i = 0
    out_of_bounds = False
    while not out_of_bounds:
        new_pebble = (500, 0)
        while True:
            returned_pebble = sand_move_logic(new_pebble, sand_pebbles, walls)
            if (new_pebble == returned_pebble):
                sand_pebbles.add(returned_pebble)
                break
            else:
                new_pebble = returned_pebble
                if (new_pebble[1] > y_max):
                    out_of_bounds = True
                    break
        
        i += 1

    print("final", len(sand_pebbles))

def solve_part_2():
    INITIAL_PEBBLE = (500, 0)
    y_max = get_y_max(walls)
    walls_with_floor = add_infinite_floor(walls, y_max)
    
    i = 0
    room_is_full = False
    while not room_is_full:
        new_pebble = INITIAL_PEBBLE
        while True:
            returned_pebble = sand_move_logic(new_pebble, sand_pebbles, walls_with_floor)

            if (new_pebble == returned_pebble):
                sand_pebbles.add(returned_pebble)
                if returned_pebble == INITIAL_PEBBLE:
                    room_is_full = True
                break
            else:
                new_pebble = returned_pebble        
        i += 1
    draw_state(walls_with_floor, sand_pebbles)
    print("final", len(sand_pebbles))

solve_part_2()

