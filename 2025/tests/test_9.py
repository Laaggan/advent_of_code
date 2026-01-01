# from day9 import connect_points, generate_area_and_rectangle_points, fill_in_grid, part2_probably_not_works, generate_allowed_points
from day9 import *

# p11 = (0, 0)
# p12 = (3, 0)
# p21 = (1, -1)
# p22 = (1, 2)

# def test_intersecting():
#     assert check_intersecting(p11, p12, p21, p22) == True

# def test_intersecting_inverse():
#     assert check_intersecting(p21, p22, p11, p12) == True

# p11 = (0, 0)
# p12 = (3, 0)
# p21 = (4, -1)
# p22 = (4, 2)

# def test_not_intersecting():
#     assert check_intersecting(p11, p12, p21, p22) == False

# def test_not_intersecting_inverse():
#     assert check_intersecting(p21, p22, p11, p12) == False

def test_rectangle_points_generated_correctly():
    point1 = (1, 1)
    point2 = (3, 3)
    area_and_points = []
    ground_truth_area = 9 # Because there are nine marks in the below pattern
    generate_area_and_rectangle_points(area_and_points, point1, point2)
    ground_truth_points = set([(1, 1), (1, 2), (1, 3), 
                                      (3, 1), (3, 2), (3, 3),
                                      (2, 1),
                                      (2, 3)])
    assert area_and_points[0][0] == ground_truth_area
    assert area_and_points[0][1] == ground_truth_points

#TODO: move to util
def convert_character_matrix_to_string(character_matrix):
    return "\n".join(map("".join, character_matrix))


def test_connect_points_horizontal():
    string_grid = '''#..#
#..#'''
    target_grid = '''#XX#
#..#'''
    x_min, y_min = 0, 0
    current_point = (0, 0)
    row_idx, col_idx = 0, 0
    connecting_point = (3, 0)
    is_vertical = False

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    connect_points(x_min, y_min, point_grid, current_point, connecting_point, is_vertical)
    result_string_grid = convert_character_matrix_to_string(point_grid)
    assert target_grid == result_string_grid

def test_connect_points_horizontal_with_offset():
    string_grid = '''#..#
#..#'''
    target_grid = '''#XX#
#..#'''
    x_min, y_min = 2, 3
    current_point = (2, 3)
    row_idx, col_idx = 0, 0
    connecting_point = (x_min + 3, y_min + 0)
    is_vertical = False

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    connect_points(x_min, y_min, point_grid, current_point, connecting_point, is_vertical)
    result_string_grid = convert_character_matrix_to_string(point_grid)
    assert target_grid == result_string_grid

def test_connect_points_vertical():
    string_grid = '''#..#
....
#..#'''
    target_grid = '''#..#
X...
#..#'''
    x_min, y_min = 0, 0
    current_point = (0, 0)
    row_idx, col_idx = 0, 0
    connecting_point = (0, 2)
    is_vertical = True

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    connect_points(x_min, y_min, point_grid, current_point, connecting_point, is_vertical)
    result_string_grid = convert_character_matrix_to_string(point_grid)
    assert target_grid == result_string_grid

def test_fill_in_grid():
    string_grid = '''#X#
X.X
#X#'''
    target_grid = '''#X#
XXX
#X#'''

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    fill_in_grid(point_grid)
    result_string_grid = convert_character_matrix_to_string(point_grid)
    print(result_string_grid)
    assert target_grid == result_string_grid

def test_fill_in_grid_multiple_regions():
    string_grid = "\n".join([
        "#XX#..#XX#",
        "X..#..#..X",
        "#XXXXXXXX#",
    ])

    target_grid = "\n".join([
        "#XX#..#XX#",
        "XXX#..#XXX",
        "#XXXXXXXX#",
    ])

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    fill_in_grid(point_grid)
    result_string_grid = convert_character_matrix_to_string(point_grid)
    print(result_string_grid)
    assert target_grid == result_string_grid

def test_generate_allowed_points():
    string_grid = "\n".join([
        "#..#..#..#",
        "...#..#...",
        "#........#",
    ])

    target_grid = "\n".join([
        "#XX#..#XX#",
        "XXX#XX#XXX",
        "#XXXXXXXX#",
    ])

    point_grid = [[c for c in row] for row in string_grid.split("\n")]
    debug_grid = [[c for c in row] for row in string_grid.split("\n")]
    points = [(3,2), (6, 2), (6, 3), (9, 3), (9, 2), (12, 2), (12, 4), (3, 4)]
    x_min, y_min = get_min_from_points(points, 0), get_min_from_points(points, 1)
    target_points=set([(3,2), (4,2), (5,2), (6, 2), (9, 2), (10, 2), (11, 2), (12, 2),
                       (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (9,3), (10,3), (11,3), (12,3),
                       (3,4), (4,4), (5,4), (6,4), (7,4), (8,4), (9,4), (10,4), (11,4), (12,4),])
    allowed_points = generate_allowed_points(points, x_min, y_min, point_grid, debug_grid)
    assert target_points == allowed_points

def test_full_solution():
    """
    Emulate test case above multiple regions
    """
    points = [(3,2), (6, 2), (9, 2), (12, 2), (3, 3), (12, 3)]
    max_area = 8
    result = part2_probably_not_works(points)
    assert max_area == result