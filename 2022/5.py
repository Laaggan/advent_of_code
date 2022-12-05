from math import floor
import re

def stack_pop(array):
    return (array[1:], array[0])

def stack_add(array, value):
    return [value, *array]

f = open("data/5_real_data.txt")
data = f.read()

data = data.split("\n\n")
stack = data[0]
instructions = data[1]
stack = stack.split("\n")
n = floor(len(stack[0])/4) + 1
stack_structure = [[] for _ in range(n)]
for x in stack[:-1]:
    iter = 0
    for i in range(n):
        stack_value = x[iter:(iter + 4)]
        iter += 4        
        if (stack_value[1] == " "):
            continue
        else:
            stack_structure[i].append(stack_value[1])
instructions = instructions.split("\n")

for instruction in instructions:
    numbers = list(map(int, re.findall(r'(\d+)', instruction)))
    
    num = numbers[0]
    i = numbers[1] - 1
    j = numbers[2] - 1

    new_i = stack_structure[i]
    new_j = stack_structure[j]
    for _ in range(num):
        new_i, moved_value = stack_pop(new_i)
        new_j = stack_add(new_j, moved_value)

    stack_structure[i] = new_i
    stack_structure[j] = new_j
        
print(*[x[0] for x in stack_structure])