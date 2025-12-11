data = '''987654321111111
811111111111119
234234234234278
818181911112111'''

with open("2025/data/3.txt") as file:
    data = file.read()

data = data.split("\n")

row_result = []
# for row in data: 
#     all_comb = []
#     for i, c1 in enumerate(row):
#         for j in range(i+1, len(row)):
#             c2 = row[j]
#             all_comb.append(int(c1 + c2))
#     result.append(max(all_comb))

result=[]
for row in data:
    remaining_picks = 12
    most_recently_used_index = 0
    row_result = ""
    while remaining_picks > 0:
        last_allowed_index = len(row) - remaining_picks + 1
        max_in_range = 0
        for i in range(most_recently_used_index, last_allowed_index):
            if int(max_in_range) < int(row[i]):
                max_in_range = row[i]
                max_index = i
        # print("val:", max_in_range, "i:", max_index)
        row_result += max_in_range
        most_recently_used_index = max_index + 1
        remaining_picks -= 1
    result.append(row_result)

print(result)
print(sum(map(int, result)))

# print(result)
# print(sum(result))
    