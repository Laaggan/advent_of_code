#input_path="input/test_input_day_1.txt"
input_path="input/real_input_day_1.txt"
file = open(input_path).read().split()
input_data = list(map(lambda x: int(x), file))

def star_1(input_data):
    result = 0
    for i in range(1, len(input_data)):
        if input_data[i - 1] - input_data[i] < 0:
            result += 1
    return result


def star_2(input_data, n):
    result = 0
    for i in range(0, len(input_data)-n):
        if (sum(input_data[i:i+n]) - sum(input_data[(i+1):(i+n+1)])) < 0:
            result += 1
    return result


print(star_2(input_data, 1))
print(star_2(input_data, 3))