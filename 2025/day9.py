import copy
def pretty_print_character_matrix(character_matrix):
    print("\n".join(map("".join, character_matrix)) + "\n")

text = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

# with open("2025/data/9.txt") as file:
#     text = file.read()

points = [list(map(int, x.split(","))) for x in text.split("\n")]

def calculate_rectangle(p1: tuple[int, int], p2: tuple[int, int]):
    return (abs(p1[0] - p2[0])+ 1) * (abs(p1[1] - p2[1]) + 1)

# def calculate_rectangle(p1: tuple[int, int], p2: tuple[int, int]):
#     return abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])

def part1(points):
    max_rect = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]

            rect_area = calculate_rectangle(point1, point2)

            if rect_area > max_rect:
                max_rect = rect_area
    print(max_rect)

# def check_intersecting(p11, p12, p21, p22):
#     if p11[0] == p12[0]:
#         pp11 = (p11[0], p12[0]) if p11[0] > p12[0] else p11
#     else:
#         pass # is horisontal

#     if p21[0] == p22[0]:
#         pass # is vertical
#     else:
#         pass # is horisontal

#     if p11[0] <= p21[0] <= p12[0] and p11[1] <= p21[1] <= p12[1]:
#         return True
#     elif p21[0] <= p11[0] <= p22[0] and p21[1] <= p11[1] <= p22[1]:
#         return True
#     else:
#         return False

def part2(points): 

    max_rect = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]

            rect_area = calculate_rectangle(point1, point2)

            if rect_area > max_rect:
                max_rect = rect_area
    print(max_rect)

def get_max_from_points(points: list[tuple[int, int]], idx: int) -> int:
    return max(map(lambda point: point[idx], points))

def get_min_from_points(points: list[tuple[int, int]], idx: int) -> int:
    return min(map(lambda point: point[idx], points))

def part2_probably_not_works(points: list[tuple[int, int]]):
    max_rect = 0
    max_x, max_y = get_max_from_points(points, 0), get_max_from_points(points, 1)
    min_x, min_y = get_min_from_points(points, 0), get_min_from_points(points, 1)
    # max_x, max_y = max(map(lambda point: point[0], points)), max(map(lambda point: point[1], points))
    # min_x, min_y = min(map(lambda point: point[0], points)), min(map(lambda point: point[1], points))

    x_range = max_x - min_x + 1
    y_range = max_y - min_y + 1
    # grid_size = (max_x - min_x + 1)*(max_y - min_y + 1)
    
    grid = [["." for _ in range(x_range)] for _ in range(y_range)]
    debug_grid = [["." for _ in range(x_range)] for _ in range(y_range)]
    
    rect_areas = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]
            generate_area_and_rectangle_points(rect_areas, point1, point2)
    
    rect_areas.sort(key=lambda x: x[0], reverse=True)

    allowed_points = generate_allowed_points(points, min_x, min_y, grid, debug_grid)
    i = 0
    for (rect_area, rect_points) in rect_areas:
        print(i, rect_area)
        debug_grid2 = copy.deepcopy(debug_grid)
        i += 1
        for point in rect_points:
            debug_grid2[point[1] - min_y][point[0] - min_x] = "O"
        pretty_print_character_matrix(debug_grid2)
        if rect_points.issubset(allowed_points):
            print("max area:", rect_area)
            break
    
    return rect_area

def generate_allowed_points(points: list[tuple[int, int]], min_x: int, min_y: int, grid: list[list[str]], debug_grid: list[list[str]]) -> set[tuple[int, int]]:
    for i, current_point in enumerate(points):
        if i == 0:
            prev_point = points[-1]
            next_point = points[i + 1]
        elif i == len(points) - 1:
            prev_point = points[i - 1]
            next_point = points[0]
        else:
            prev_point = points[i - 1]
            next_point = points[i + 1]
        col_idx = current_point[0] - min_x
        row_idx = current_point[1] - min_y
        grid[row_idx][col_idx] = "#"
        
        prev_is_vertical = current_point[0] == prev_point[0]
        next_is_vertical = current_point[0] == next_point[0]

        connect_points(min_x, min_y, grid, current_point, prev_point, prev_is_vertical)
        connect_points(min_x, min_y, grid, current_point, next_point, next_is_vertical)
    
    fill_in_grid(grid)
    pretty_print_character_matrix(grid)
    allowed_points = set()
    for j, row in enumerate(grid):
        for i, val in enumerate(row):
            if val == "X" or val == "#":
                allowed_points.add((i + min_x, j + min_y))
                # debug_grid[i][j] = "X"
    return allowed_points

def generate_area_and_rectangle_points(rect_areas, point1, point2):
    rect_area = calculate_rectangle(point1, point2)
    rect_points = set()
    for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
        rect_points.add((x, point1[1]))
        rect_points.add((x, point2[1]))
            
    for y in range(min(point1[1], point2[1]) + 1, max(point1[1], point2[1])):
        rect_points.add((point1[0], y))
        rect_points.add((point2[0], y))
    rect_areas.append((rect_area, rect_points))

    # pretty_print_character_matrix(grid)

def fill_in_grid(grid):
    for i in range(len(grid)):
        filling = False
        for j in range(len(grid[0]) - 1): # We don't check last because we assume nice data
            if j == len(grid[0]) - 1:        
                break
            # elif (grid[i][j] == "X" or grid[i][j] == "#") and (grid[i][j + 1] == 'X' or grid[i][j + 1] == '#'):
            #     filling = True # Can this hack fix it
            #     continue
            elif (grid[i][j] == "X" or grid[i][j] == "#") and grid[i][j + 1] == '.':
                if j > 1 and (grid[i][j - 1] == "X" or grid[i][j - 1] == "#"):
                    filling = False
                else:
                    filling = True
                continue
            
            if filling and (grid[i][j] != "X" and grid[i][j] != "#"):
                grid[i][j] = "X"

def connect_points(min_x: int, min_y: int, grid: list[list[tuple[int, int]]], current_point: tuple[int, int], connecting_point: tuple[int, int], line_is_vertical: bool):
    col_idx = current_point[0] - min_x
    row_idx = current_point[1] - min_y
    if line_is_vertical:
        for y_p in range(min(current_point[1], connecting_point[1]) + 1, max(current_point[1], connecting_point[1])):
            grid[y_p - min_y][col_idx] = "X"
    else:
        for x_p in range(min(current_point[0], connecting_point[0]) + 1, max(current_point[0], connecting_point[0])):
            grid[row_idx][x_p - min_x] = "X"
    

# part2_probably_not_works(points)
