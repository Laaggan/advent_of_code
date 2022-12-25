data = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
data = open("data/25_real_data.txt", 'r').read()
data = data.split("\n")

CONVERT_CHAR_TO_NUM = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

total_sum = 0
for num in data:
    n = len(num)
    power = reversed(range(n))
    value_sum = 0
    for p, c in zip(power, num):
        base = 5**p
        num = CONVERT_CHAR_TO_NUM[c]
        value_sum += base * num
    total_sum += value_sum
print(total_sum)

max_p = 0
while 2*5**max_p < total_sum:
    max_p += 1
print(max_p)

repr = ""
decimal_repr = 0
remaining = total_sum
for i in reversed(range(max_p + 1)):
    base = 5**i
    if i >= 1:
        remaining_max_size = sum([2*5**j for j in range(i)])
    else:
        remaining_max_size = 0
    
    if (remaining > 0):
        if (abs(remaining - 2*base) <= remaining_max_size):
            remaining = remaining - 2*base
            repr += "2"
        elif (abs(remaining - base) <= remaining_max_size):
            remaining = remaining - base
            repr += "1"
        else:
            repr += "0"
    elif (remaining < 0):
        if (abs(remaining + 2*base) <= remaining_max_size):
            remaining = remaining + 2*base
            repr += "="
        elif (abs(remaining + base) <= remaining_max_size):
            remaining = remaining + base
            repr += "-"
        else:
            repr += "0"
    else:
        repr += "0"

print(repr)