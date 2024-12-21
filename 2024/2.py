data = open("data/test_2.txt", 'r').read()
reports = [[int(y) for y in x.split()] for x in data.split("\n")]

num_safe = 0
for report in reports:
    prev_level = report[0]
    safe = False
    for i in range(1, len(report)):
        curr_level = report[i]
        if i == 1:
            if prev_level < curr_level:
                descending = False
                safe = True
            elif prev_level > curr_level:
                descending = True
                safe = True
            elif prev_level == curr_level:
                break
        else:
            if descending:
                if prev_level < curr_level:
                    print("desc")
                    continue
                else:
                    safe = False
                    break
            else:
                if prev_level > curr_level:
                    print("asc")
                    continue
                else:
                    safe = False
                    break
        prev_level = curr_level
    if safe:
        num_safe += 1

print(num_safe)


    
