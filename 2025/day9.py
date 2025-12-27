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

def calculate_rectangle(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)

max_rect = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]

        rect_area = calculate_rectangle(point1, point2)

        if rect_area > max_rect:
            max_rect = rect_area

print(max_rect)


