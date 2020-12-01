raw_data = open('input.txt').read().split('\n')
raw_data.pop()
data = list(map(lambda a: int(a), raw_data))

def find_2020(data):
    for x in data:
        for y in data:
            if x + y == 2020:
                return x*y
print(find_2020(data))