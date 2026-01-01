import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.plotting import plot_polygon, plot_points

text = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

with open("2025/data/9.txt") as file:
    text = file.read()

points = [list(map(int, x.split(","))) for x in text.split("\n")]

# Data exploration:
# fig = plt.figure(1, dpi=90)

# This shows that I was trying to solve a much more general problem than existed in the data
# ax = fig.add_subplot(111)

# plot_polygon(polygon, ax=ax, add_points=False)
# plot_points(polygon, ax=ax, alpha=0.7)

# ax.set_title('Death star')
# plt.savefig('2025/misc/deathstar.jpg')
# plt.show()

def calculate_rectangle(p1: tuple[int, int], p2: tuple[int, int]):
    return (abs(p1[0] - p2[0])+ 1) * (abs(p1[1] - p2[1]) + 1)

def create_rectangle_polygon(point1: tuple[int, int], point2: tuple[int, int]):
    return Polygon([point1, (point1[0], point2[1]), point2, (point2[0], point1[1])])

def part2(points):
    polygon = Polygon(points)

    max_rect = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]

            rect_area = calculate_rectangle(point1, point2)
            rect = create_rectangle_polygon(point1, point2)

            if polygon.contains(rect) and rect_area > max_rect:
                max_rect = rect_area
    print(max_rect)

part2(points)