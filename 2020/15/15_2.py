import copy

small_input = [0, 3, 6]
small_input = [1, 3, 2]
_input = [0, 14, 1, 3, 7, 9]
curr_input = small_input

iter = len(curr_input)
history = {'0': 1, '3': 2, '6': 3}
history = {'0': 1, '14': 2, '1': 3, '3': 4, '7': 5, '9': 6}
found_match = False
next_val = 0
while iter <= 3000:
    last_iter = history.get(str(next_val))
    prev_val = next_val

    iter += 1
    if last_iter == None:
        next_val = 0
        history[str(prev_val)] = iter
    else:
        next_val = iter - last_iter
        history[str(prev_val)] = iter
    print(prev_val)
    #if iter == 2020 or prev_val == 763:
    #    print(prev_val)
        #break

