from functools import reduce
import matplotlib.pyplot as plt

data = """R8,U5,L5,D3
U7,R6,D4,L4"""

data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""

# data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

data = list(map(lambda x: x.split(","), data.split("\n")))

def add_point_to_dict(point, dic):
    if point in dic:
        dic[point] += 1
    else:
        dic[point] = 1

result = dict()
for row in data:
    x, y = 0, 0
    for instruction in row:
        direction = instruction[0]
        distance = int(instruction[1:])
        point = (x, y)
        add_point_to_dict(point, result)

        for i in range(distance):
            if direction == "U":
                y = y + 1
                point = (x, y)
            elif direction == "D":
                y = y - 1
                point = (x, y)
            elif direction == "R":
                x = x + 1
                point = (x, y)
            elif direction == "L":
                x = x - 1
                point = (x, y)

            add_point_to_dict(point, result)

crosses = [key for key in result if result[key] > 1]
crosses.remove((0,0))
cross_xs = [point[0] for point in crosses]
cross_ys = [point[1] for point in crosses]

all_xs = [point[0] for point in result]
all_ys = [point[1] for point in result]
plt.scatter(all_xs, all_ys, c="blue")
plt.scatter(cross_xs, cross_ys, c="red")
plt.show()

distances = [reduce(lambda a, b: a + abs(b), cross, 0) for cross in crosses]
idx_max = min(enumerate(crosses), key=lambda x:x[1])[0]
print(len(result))
print(crosses)
print(sum(crosses[idx_max]))
        