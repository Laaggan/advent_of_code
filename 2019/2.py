data = open("data/2_r.txt", "r").read()
data = list(map(int, data.split(",")))

i = 0
while i + 4 < len(data):
    code = data[i]
    if (code == 1):
        pointer1 = data[i + 1]
        pointer2 = data[i + 2]
        new_value = data[pointer1] + data[pointer2]
    elif (code == 2):
        pointer1 = data[i + 1]
        pointer2 = data[i + 2]
        new_value = data[pointer1] * data[pointer2]
    elif (code == 99):
        break
    else:
        raise "Invalid code"
    destination = data[i + 3]
    data[destination] = new_value
    i += 4

print(data[0])