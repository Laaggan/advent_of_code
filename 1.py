#input_path="input/test_input_day_1.txt"
input_path="input/real_input_day_1.txt"
file = open(input_path).read().split()
input_data = list(map(lambda x: int(x), file))

result = 0
for i in range(1, len(input_data)):
    if input_data[i - 1] - input_data[i] < 0:
        result += 1

print(result)