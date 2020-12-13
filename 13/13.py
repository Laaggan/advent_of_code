from math import floor
input_path = "small_input.txt"
data = open(input_path).read().split("\n")
data.pop()
time_stamp = int(data[0])
ids = data[1].split(",")
ids = [int(id) for id in ids if id != 'x']


print_str0 = "Timestamp, "
for id in ids:
    print_str0 += " bus " + str(id) + ", "
print(print_str0)
n = len(print_str0)
cols = 1 + len(ids)
pad = floor(n/cols)
for i in range(929, 950):
    filler = [i % id == 0 for id in ids]
    print_str1 = ("{:^"+str(pad)+"}")*cols
    print(print_str1.format(*[i, *filler]))