import math
data = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

data = open("data/5.txt", "r").read()

data = data.split("\n\n")
seeds = list(map(int, data[0].split(":")[1].split()))
mappings = list(map(lambda x: x.split(":"), data[1:]))
mappings = [(x[0], list(map(str.split, x[1].strip().split("\n")))) for x in mappings]

def create_map(values, dic):
    for value in values:
        destination, source, rang = list(map(int, value))
        for d, s in zip(range(destination, destination + rang), range(source, source + rang)):
            dic[s] = d
    return dic

class ThisDict:
    def __init__(self):
        self.internal_dict = dict()

    def __setitem__(self, key, value):
        self.internal_dict[key] = value

    def __getitem__(self, i):
        try:
            return self.internal_dict[i]
        except:
            return i

seed_to_soil_map = ThisDict()
soil_to_fertilizer_map = ThisDict()
fertilizer_to_water_map = ThisDict()
water_to_light_map = ThisDict()
light_to_temperature_map = ThisDict()
temperature_to_humidity_map = ThisDict()
humidity_to_location_map = ThisDict()
for ma in mappings:
    name, values = ma
    print(name)
    
    if name == 'seed-to-soil map':
        seed_to_soil_map = create_map(values, seed_to_soil_map)
    elif name == 'soil-to-fertilizer map':
        soil_to_fertilizer_map = create_map(values, soil_to_fertilizer_map)
    elif name == 'fertilizer-to-water map':
        fertilizer_to_water_map = create_map(values, fertilizer_to_water_map)
    elif name == 'water-to-light map':
        water_to_light_map = create_map(values, water_to_light_map)
    elif name == 'light-to-temperature map':
        light_to_temperature_map = create_map(values, light_to_temperature_map)
    elif name == 'temperature-to-humidity map':
        temperature_to_humidity_map = create_map(values, temperature_to_humidity_map)
    elif name == 'humidity-to-location map':
        humidity_to_location_map = create_map(values, humidity_to_location_map)

min_location = math.inf
for i, seed in enumerate(seeds):
    print(i, seed)
    soil = seed_to_soil_map[seed]
    fertilizer = soil_to_fertilizer_map[soil]
    water = fertilizer_to_water_map[fertilizer]
    light = water_to_light_map[water]
    temperature = light_to_temperature_map[light]
    humidity = temperature_to_humidity_map[temperature]
    location = humidity_to_location_map[humidity]
    
    if location < min_location:
        min_location = location

print(min_location)
