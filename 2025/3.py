data = '''987654321111111
811111111111119
234234234234278
818181911112111'''

with open("2025/data/3.txt") as file:
    data = file.read()

data = data.split("\n")

result = []
for row in data: 
    # first_max = 0
    # second_max = 0
    # for i, c in enumerate(row):
    #     if first_max < int(c):
    #         first_max = int(c)
    #         first_max_i = i
    
    # for i, c in enumerate(row[(first_max_i+1):]):
    #     if second_max < int(c):
    #         second_max = int(c)
    
    # result.append(int(str(first_max) + str(second_max)))
    all_comb = []
    for i, c1 in enumerate(row):
        for j in range(i+1, len(row)):
            c2 = row[j]
            all_comb.append(int(c1 + c2))
    result.append(max(all_comb))

print(result)
print(sum(result))
    