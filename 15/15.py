import copy

small_input = [0, 3, 6]
small_input = [1, 3, 2]
_input = [0, 14, 1, 3, 7, 9]
curr_input = _input

iter = len(curr_input)
history = copy.deepcopy(curr_input)
found_match = False
while iter <= 2019:
    if iter % 100 == 0:
        print(iter)
    ind1 = iter - 1
    curr_number1 = history[ind1]
    for i in range(2, len(history) + 1):
        ind2 = len(history) - i
        curr_number2 = history[ind2]
        if curr_number2 == curr_number1:
            found_match = True
            break
    if found_match:
        history.append((ind1 + 1) - (ind2 + 1))
        found_match = False
    else:
        history.append(0)
    iter += 1

print("result:", history[-1])