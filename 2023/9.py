data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# data = """18 -125 -268 -411"""

data = open("data/9.txt", "r").read()

data = [[int(y) for y in x.split()] for x in data.split("\n")]

def check_end_condition(lines):
    last_line = lines[-1]
    return all(x == 0 for x in last_line)

total = 0
for line in data:
    report = [line]
    while len([n for n in report[-1] if n == 0]) < len(report[-1]):
        report.append([report[-1][i + 1] - report[-1][i] for i in range(len(report[-1]) - 1)])
    for i in range(len(report) - 2, -1, -1):
        report[i].append(report[i][-1] + report[i + 1][-1])
    total += report[0][-1]
print(total)

# result = []
# for input_line in data:
#     lines = [input_line]
#     while check_end_condition(lines):
#         new_line = []
#         current_line = lines[-1]
#         for j in range(1, len(current_line)):
#             a = current_line[j]
#             b = current_line[j - 1]
#             new_value = max(a, b) - min(a, b)
#             # new_value = a - b
#             new_line.append(new_value)
#         lines.append(new_line)

#     # for z in reversed(range(1, len(lines))):
#     for z in range(len(lines) - 2, -1, -1):
#         last_value = lines[z][-1]
#         second_to_last = lines[z - 1][-1]
#         lines[z - 1].append(second_to_last + last_value)

#     # print(lines[0][-1]) 994315045 
#     # print(lines)
#     result.append(lines[0][-1])

# print(sum(result))
