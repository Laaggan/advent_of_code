from math import sqrt

data = '''Time:      7  15   30
Distance:  9  40  200'''

data = '''Time:        44     89     96     91
Distance:   277   1136   1890   1768'''

data = '''Time:        44899691
Distance:   277113618901768'''

data = data.split("\n")
times = list(map(int, data[0].split()[1:]))
distances = list(map(int, data[1].split()[1:]))

result = []
for total_time, distance in zip(times, distances): 
    a = 1
    number = 0
    for charging_time in range(1, total_time):
        velocity = a*charging_time
        race_time = total_time - charging_time
        race_dist = velocity*race_time

        if race_dist > distance:
            number += 1
    result.append(number)

# t_ch = time/2 + sqrt(time**2/4 - distance/a)
# print(t_ch)

mult_result = 1
for num in result:
    mult_result *= num

print(mult_result)