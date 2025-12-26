text = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

with open("2025/data/6.txt") as file:
    text = file.read()

data = [x.split() for x in text.split("\n")]
N = len(data)
M = len(data[0])

data2 = text.split("\n")
N2 = len(data2)
M2 = len(data2[0])

new_data1 = []
for j in range(M):
    number_sequence = []
    row = {}
    for i in range(N):
        if i != N - 1:
            number_sequence.append(int(data[i][j]))
        else:
            row["operator"] = data[i][j]
    row["number_sequence"] = number_sequence
    new_data1.append(row)

def get_numbers_from_data(data, j0, j1, is_last):
    numbers = []
    if is_last:
        j1 = j1 + 1

    for j in range(j0, j1):
        partial_result = ""
        for i in range(N2-1):
            partial_result += data[i][j]
        numbers.append(int(partial_result.strip()))
    return numbers

new_data2 = []
j0 = 0
is_last = False
for j in range(M2):
    found_spacing = True
    row = {}
    for i in range(N2):
        c = data2[i][j]
        if c != " ":
            found_spacing = False
            break
    if j == M2 - 1:
        is_last = True
    if found_spacing or is_last:
        row["number_sequence"] = get_numbers_from_data(data2, j0, j, is_last)
        row["operator"] = data2[N2-1][j0]
        new_data2.append(row)
        j0 = j + 1
    else:
        continue
            

# data = new_data1
print(new_data2)
data = new_data2

result = 0
for row in data:
    if row["operator"] == '*':
        partial_result = 1
        for x in row["number_sequence"]:
            partial_result *= x
    elif row["operator"] == '+':
        partial_result = 0
        for x in row["number_sequence"]:
            partial_result += x
    else:
        raise "Not a defined operator"
    result += partial_result

print(result)

