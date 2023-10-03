data = "130254-678275"

pw_min, pw_max = tuple(map(int, data.split("-")))

result = 0
for x in range(pw_min, pw_max + 1):
    num_list = list(map(int, str(x)))
    has_adjacent_digits = False
    has_increasing_digits = True
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i + 1]:
            has_increasing_digits = False
            break
        if num_list[i] == num_list[i + 1]:
            has_adjacent_digits = True
    
    if (has_adjacent_digits and has_increasing_digits):
        result += 1
    
print(result)
