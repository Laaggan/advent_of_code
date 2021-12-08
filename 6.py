#input_path = 'input/test_input_day_6.txt'
input_path = 'input/real_input_day_6.txt'

file = open(input_path).read()
data = list(map(int, file.split(",")))

days = 80
print("Initial data: ", data)
for i in range(days):
    data = list(map(lambda x: x - 1, data))
    print(len(data))
    new_fishes = 0
    for i, x in enumerate(data):
        if x == 0:
            new_fishes += 1
            data[i] = 7
    data = data + [9 for _ in range(new_fishes)]