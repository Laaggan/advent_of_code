from math import floor, log, log2

data = open("data/7.txt").read()
data = [(int(row[0]), list(map(int, row[1].split()))) for row in list(map(lambda x: x.split(": "), data.splitlines()))]

def solution_part_1(data):
    solution = set()
    for i, row in enumerate(data):
        total_sum = row[0]
        values = row[1]

        if len(values) == 1:
            if total_sum == values[0]:
                solution.add(values[0])
            continue

        n = 2**len(values)
        binary_tree = [0 for _ in range(n)]
        binary_tree[0] = values[0]
        for i in range(1, n):
            value_index = floor(log2(i))
            if i > 1:
                if i % 2 == 0:
                    binary_tree[i-1] = binary_tree[i//2-1] + values[value_index]
                else:
                    binary_tree[i-1] = binary_tree[i//2-1] * values[value_index]
            else:
                binary_tree[i-1] = values[0]
        for i in range(n//2-1, n):
            if binary_tree[i] == total_sum:
                solution.add(total_sum)
    return solution

def do_calc(t_sum, values):
    if len(values) == 1:
        if values[0] == t_sum:
            return True
        else:
            return False
    
    curr_val = values[-1]
    multiplication_condition = t_sum % curr_val == 0
    if multiplication_condition:
        if do_calc(t_sum//curr_val, values[:len(values)-1]):
            return True
    
    str_t_sum = str(t_sum)
    concatenation_condition = str_t_sum.endswith(str(curr_val))
    if concatenation_condition:
        if len(str_t_sum) > len(str(curr_val)) and do_calc(int(str_t_sum[:len(str_t_sum)-len(str(curr_val))]), values[:len(values)-1]):
            return True
    
    addition_condition = t_sum > values[-1]
    if addition_condition:
        if do_calc(t_sum-curr_val, values[:len(values)-1]):
            return True
    
    return False

def solution_part_2(data):
    solution = set()
    for i, row in enumerate(data):
        total_sum = row[0]
        values = row[1]
        # do_calc(total_sum, values, path=[])
        if do_calc(total_sum, values):
            solution.add(total_sum)
    return solution


def solution_part_2_ternary_tree(data): #this approach does not work since concatenation modifies the number of elements
    solution = set()
    for i, row in enumerate(data):
        total_sum = row[0]
        values = row[1]

        if len(values) == 1:
            if total_sum == values[0]:
                solution.add(values[0])
            continue

        n = 3**len(values)
        binary_tree = [0 for _ in range(n)]
        binary_tree[0] = values[0]
        for i in range(1, n):
            value_index = floor(log(i, 3))
            if i > 1:
                if i % 3 == 0:
                    binary_tree[i-1] = binary_tree[i//3-1] + values[value_index]
                elif i % 3 == 1:
                    binary_tree[i-1] = binary_tree[i//3-1] * values[value_index]
                else:
                    if value_index < len(values)-1:
                        binary_tree[i-1] = int(str(values[value_index]) + str(values[value_index+1]))
            else:
                binary_tree[i-1] = values[0]
        
        print(total_sum, binary_tree)
        for i in range(n//3-1, n):
            if binary_tree[i] == total_sum:
                solution.add(total_sum)
    return solution

def solution_part_2_not_working(data):
    solution_1 = set()
    new_data = []
    for row in data:
        total_sum = row[0]
        values = row[1]
        for i in range(len(values) - 1):
            new_values = [*values[:i], int(str(values[i]) + str(values[i+1])), *values[i+2:]]
            new_data.append([total_sum, new_values])
    solution_2 = solution_part_1(new_data)
    print(solution_2)
    return solution_1.union(solution_2)

print(sum(solution_part_1(data)))    

sol_3 = solution_part_2(data)
print(sum(sol_3))
