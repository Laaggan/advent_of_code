data = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

data = open('data/1.txt', 'r').read()

data = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
data = data.split("\n")

# result = []
# for row in data:
#     first = None
#     last = None
#     temp = ''
#     for c in row:
#         if first is None and c in nums:
#             temp += c
#             continue
#         elif first is None and c not in nums and len(temp) > 0:
#             first = temp
#             temp = ''
#             continue
        
#         if first is not None and c in nums:
#             temp += c
#             continue
#         elif first is not None and c not in nums and len(temp) > 0:
#             last = temp
#             temp = ''
#             continue
#     if len(temp) > 0:
#         last = temp
    
#     if last is not None:
#         result.append(int(first + last))
#     else:
#         result.append(int(first + first))

result = []
for row in data:
    first = None
    last = None
    temp = ''
    for c in row:
        if first is None and c in nums:
            first = c
            continue
        
        if first is not None and c in nums:
            last = c
            continue
    if last is not None:
        result.append(int(first + last))
    else:
        result.append(int(first + first))

print(sum(result))