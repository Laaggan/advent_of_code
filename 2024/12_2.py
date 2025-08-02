data = '''AAAA
BBCD
BBCC
EEEC'''

data = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''

data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

data = open("2024/data/12.txt").read()

data = [[c for c in row] for row in data.split("\n")]

# Create grid
grid = dict()

for i, row in enumerate(data):
    for j, c in enumerate(row):
        grid[i, j] = c

def check_neighbourhood(data, i, j):
    neighbours = []
    c = data[i][j]
    if i - 1 >= 0 and data[i - 1][j] == c:
        neighbours.append((i - 1, j))
    if i + 1 < len(data) and data[i + 1][j] == c:
        neighbours.append((i + 1, j))
    if j - 1 >= 0 and data[i][j - 1] == c:
        neighbours.append((i, j - 1))
    if j + 1 < len(data[0]) and data[i][j + 1] == c:
        neighbours.append((i, j + 1))
    return neighbours

seen = set()
regions = set()
for (point, value) in grid.items():
    if point in seen:
        continue
    else:
        seen.add(point)

    queue = [point]
    region = set()
    region.add(point)

    while queue:
        current = queue.pop()
        neighbours = check_neighbourhood(data, current[0], current[1])
        neighbours = (set(neighbours)).difference(seen)
        seen |= neighbours
        region.update(neighbours)
        queue.extend(neighbours)
    
    regions.add(frozenset(region))
    seen |= region

result = 0
for region in regions:
    region_perimeter = 0
    region_area = len(region)
    for point in region:
        neighbours = check_neighbourhood(data, point[0], point[1])
        region_perimeter += 4 - len(neighbours)
    
    result += region_area*region_perimeter

print(result)
    


