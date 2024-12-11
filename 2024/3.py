data = open("2024/data/3.txt", 'r').read()

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
sequence_ind = 0

def validate_number_section(i, sub_string):
    j = 0
    num = ""
    while sub_string[j] in digits:
        num += sub_string[j]
        j += 1

    if len(num) > 3:
        i += j
        return (i, None, None)
    else:
        num1 = int(num)
    
    if sub_string[j] != ",":
        return (i, None, None)
    j += 1
    
    num = ""
    while sub_string[j] in digits and j < len(sub_string) - 1:
        num += sub_string[j]
        j += 1


    if len(num) > 3:
        i += j
        return (i, None, None)
    else:
        num2 = int(num)
    
    return (i+j, num1, num2)

def calculate_sum(data):
    total_sum = 0
    i = 0
    sequence_ind = 0
    
    while i < len(data):
        if sequence_ind == 0:
            if data[i:i+len("mul")] == "mul":
                sequence_ind += 1
                i += len("mul")
            else:
                i += 1
        elif sequence_ind == 1:
            if data[i] == "(":
                sequence_ind += 1
                i += 1
            else:
                sequence_ind = 0
                i += 1
        elif sequence_ind == 2:
            (i, num1, num2) = validate_number_section(i, data[i:])

            if num1 is None or num2 is None:
                sequence_ind = 0
            else:
                sequence_ind = 3
        elif sequence_ind == 3:
            if data[i] == ")":
                total_sum += num1*num2
                i += 1
            else:
                i += 1
            sequence_ind = 0
    print(total_sum)

def find_do_and_dont(data):
    i = 0
    sequence_ind = 0
    on = True
    indices_to_keep = [0]
    while i < len(data):
        if data[i:i+len("do()")] == "do()":
            if not on:
                indices_to_keep.append(i)
            on = True
        elif data[i:i+len("don't()")] == "don't()":
            if on:
                indices_to_keep.append(i)
            on = False
        i += 1
    
    if len(indices_to_keep) % 2 != 0:
        indices_to_keep.append(len(data)-1)

    new_data = ""
    for i in range(0, len(indices_to_keep), 2):
        new_data += data[indices_to_keep[i]:indices_to_keep[i+1]]
    return new_data
            
data = find_do_and_dont(data)
calculate_sum(data)

        
