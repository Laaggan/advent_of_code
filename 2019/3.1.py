from functools import reduce
import matplotlib.pyplot as plt

data = """R8,U5,L5,D3
U7,R6,D4,L4"""

data = """R2,U8
U7,R3,D1,L2,D1,R2,D1,L2,D1,R2,D1,L2"""

data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""

data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

data = open("data/3_r.txt").read()
data = list(map(lambda x: x.split(","), data.split("\n")))

result = []
point_result = []
for row in data:
    row_result=[]
    points=[(0, 0)]
    x, y = 0, 0
    for instruction in row:
        direction = instruction[0]
        distance = int(instruction[1:])
        point1 = (x, y)
        
        if direction == "U":
            y = y + distance
            point2 = (x, y)
        elif direction == "D":
            y = y - distance
            point2 = (x, y)
        elif direction == "R":
            x = x + distance
            point2 = (x, y)
        elif direction == "L":
            x = x - distance
            point2 = (x, y)
        row_result.append((point1, point2))
        points.append(point2)
    result.append(row_result)
    point_result.append(points)

line_segments_1 = result[0]
line_segments_2 = result[1]

xs, ys = [], []
for point in point_result[0]:
    xs.append(point[0])
    ys.append(point[1])
plt.plot(xs, ys, c="red")
xs, ys = [], []
for point in point_result[1]:
    xs.append(point[0])
    ys.append(point[1])
plt.plot(xs, ys, c="blue")

def add_point_if_line_segments_crosses(point1, point2, point3, point4, crosses):
    min_x = min(point1[0], point2[0])
    max_x = max(point1[0], point2[0])

    min_y = min(point3[1], point4[1])
    max_y = max(point3[1], point4[1])

    if (point3[0] >= max_x or point3[0] <= min_x or point1[1] <= min_y or point1[1] >= max_y):
        return (crosses, None)
    cross = (point3[0], point1[1])
    crosses.add(cross)
    return (crosses, cross)
    
def point_is_on_line_segment(p1, p2, cross):
    if (p1[0] == p2[0] and cross[0] == p1[0]):
        return abs(cross[1] - p1[1])
    elif (p1[1] == p2[1] and cross[1] == p1[1]):
        return abs(cross[0] - p1[0])
    return None

def distance_between_points(p1, p2):
    if (p1[1] == p2[1]):
        return abs(p2[0] - p1[0])
    else:
        return abs(p2[1] - p1[1])

crosses = set()
for line_segment1 in line_segments_1:
    point1, point2 = line_segment1
    is_horizontal_1 = point1[1] == point2[1]
    current_line_length = 0
    for line_segment2 in line_segments_2:
        point3, point4 = line_segment2
        is_horizontal_2 = point3[1] == point4[1]

        if (is_horizontal_1 == is_horizontal_2):
            if (is_horizontal_1):
                current_line_length += abs(point2[0] - point1[0])
            else:
                current_line_length += abs(point2[1] - point1[1])
            continue

        if (is_horizontal_1):
            (crosses, cross) = add_point_if_line_segments_crosses(point1, point2, point3, point4, crosses)
        else:
            (crosses, cross) = add_point_if_line_segments_crosses(point3, point4, point1, point2, crosses)


def calculate_distances_running_distances(line_segments, crosses):
    lengths_until_cross = dict()
    current_line_length = 0
    for line_segment in line_segments:
        on_line_segment = None
        point1, point2 = line_segment
        for cross in crosses:
            on_line_segment = point_is_on_line_segment(point1, point2, cross)
        
            if (on_line_segment is not None):
                lengths_until_cross[cross] = current_line_length + on_line_segment
                continue
        current_line_length += distance_between_points(point1, point2)
    return lengths_until_cross


distances = [abs(cross[0]) + abs(cross[1]) for cross in crosses]
print("Solution part 1: ", min(distances))

length_until_cross_1 = calculate_distances_running_distances(line_segments_1, crosses)
length_until_cross_2 = calculate_distances_running_distances(line_segments_2, crosses)
print("Solution part 2: ", min([length_until_cross_1[cross] + length_until_cross_2[cross] for cross in crosses]))

for cross in crosses:
    plt.scatter(cross[0], cross[1])
# plt.show()

        