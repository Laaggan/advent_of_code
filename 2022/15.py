import typing
import matplotlib.pyplot as plt

data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
# data = open("data/15_real_data.txt", 'r').read()
data = [x.split(": ") for x in data.split("\n")]
data = [
    [list(map(int, x[0].replace("Sensor at x=", "").replace("y=", "").split(", "))),
    list(map(int, x[1].replace("closest beacon is at x=", "").replace("y=", "").split(", ")))
] for x in data]

def enumerate_distance(point: typing.Tuple[int, int], distance: int, cant_have_beacons: typing.Set[typing.Tuple[int, int]]):
    added_points = set()
    for i in range(distance + 1):
        for j in range(distance - i + 1):
            # first quadrant, I keep i=0 and j=0 for adding the sensor
            dx = j
            dy = i
            new_point = (point[0] + dx, point[1] + dy)
            cant_have_beacons.add(new_point)
            added_points.add(new_point)
    
            # second quadrant
            dx = j
            dy = -i
            new_point = (point[0] + dx, point[1] + dy)
            cant_have_beacons.add(new_point)
            added_points.add(new_point)
            
            # third quadrant
            dx = -j
            dy = -i
            new_point = (point[0] + dx, point[1] + dy)
            cant_have_beacons.add(new_point)
            added_points.add(new_point)
            
            # fourth quadrant
            dx = -j
            dy = i
            new_point = (point[0] + dx, point[1] + dy)
            cant_have_beacons.add(new_point)
            added_points.add(new_point)
    # for i in range(distance):
    #     for j in range(distance - i):
    
    # for i in range(distance):
    #     for j in range(distance - i):

    # for i in range(distance):
    #     for j in range(distance - i):
    
    return cant_have_beacons, added_points
    
            
    
cant_have_beacons = set()
for points in data:
    sensor = points[0]
    beacon = points[1]

    x_diff = abs(sensor[0] - beacon[0])
    y_diff = abs(sensor[1] - beacon[1])

    distance = x_diff + y_diff

    cant_have_beacons, added = enumerate_distance(sensor, distance, cant_have_beacons)

    # if (sensor[0] == 8 and sensor[1] == 7):
    #     # xs = list(map(lambda x: x[0], cant_have_beacons))
    #     # ys = list(map(lambda x: x[1], cant_have_beacons))
    #     xs = list(map(lambda x: x[0], added))
    #     ys = list(map(lambda x: x[1], added))
    #     plt.scatter(xs, ys)
    #     plt.gca().invert_yaxis()
    #     plt.show()

y_of_row = 10
# y_of_row = 2000000
filtered_cant_have_beacons = [x for x in cant_have_beacons if x[1] == y_of_row]
x_min = min(map(lambda x: x[0], filtered_cant_have_beacons))
x_max = max(map(lambda x: x[0], filtered_cant_have_beacons))

# x_min = min(map(lambda x: x[0], cant_have_beacons))
# x_max = max(map(lambda x: x[0], cant_have_beacons))

count = 0
for x in range(x_min, x_max):
    if (x, y_of_row) in cant_have_beacons:
        count += 1

print(count)