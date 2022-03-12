#input_path = 'input/test_input_day_6.txt'
input_path = 'input/real_input_day_6.txt'

file = open(input_path).read()
data = list(map(int, file.split(",")))


def star_1(data):
    days = 80
    for i in range(days - 1):
        data = list(map(lambda x: x - 1, data))
        new_fishes = 0
        for i, x in enumerate(data):
            if x == 0:
                new_fishes += 1
                data[i] = 7
        data = data + [9 for _ in range(new_fishes)]
    return len(data)


def star_2(data):
    days = 256
    result = {}
    for i in range(10):
        result[i] = 0

    for x in data:
        result[x] += 1

    fishes_that_multiply = 0
    for j in range(days):
        result[9] = fishes_that_multiply
        result[7] += fishes_that_multiply
        for k in range(9):
            result[k] = result[k+1]
        result[9] = 0
        fishes_that_multiply = result[0]

    number_result = 0
    for key in result:
        number_result += result[key]
    return number_result

#print(star_1(data))
print(star_2(data))