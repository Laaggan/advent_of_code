from collections import defaultdict


data = '''AAAA
BBCD
BBCC
EEEC'''

data = data.split("\n")

region_counter = 0
area=defaultdict(set)
symbol=defaultdict(str)
perimeter=defaultdict(set)
i, j = 0, 0
N, M = len(data), len(data[0])
continuation_index = [0 for _ in range(len(data))]

def determine_perimeter(c, i, j):
    pass

while True:
    current_symbol = data[i][j]
    
    # Add perimeter when out of bounds
    if i - 1 < 0:
        perimeter[region_counter].add((i-1, j))
    elif i + 1 > N - 1:
        perimeter[region_counter].add((i+1, j))
    if j - 1 < 0:
        perimeter[region_counter].add((i, j - 1))
    elif j + 1 > M - 1:
        perimeter[region_counter].add((i, j + 1))
    
    # Row handling
    if i - 1 >= 0 and current_symbol != data[i - 1][j]:
        perimeter[region_counter].add((i - 1, j))
    if i + 1 <= N - 1 and current_symbol != data[i + 1][j]:
        perimeter[region_counter].add((i + 1, j))
    
    # Column handling
    if j - 1 >= 0 and current_symbol != data[i][j - 1]:
        perimeter[region_counter].add((i, j - 1))
    elif j - 1 >= 0 and current_symbol == data[i][j - 1]:
        area[region_counter].add((i, j - 1))
    
    if j + 1 <= M - 1 and current_symbol != data[i][j + 1]:
        perimeter[region_counter].add((i, j + 1))

print(area)
        
