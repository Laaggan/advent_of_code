data = open('input.txt').read().split()
data = [int(x) for x in data]

n = len(data)

def find_sum_of_num(param, nums, x):
    assert len(nums) == param, 'Input sequence must have ' + str(param) + ' elements'
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return True
    return False

param = 25
for i in range(param, n):
    nums = data[(i-param):i]
    curr_num = data[i]

    if not find_sum_of_num(param, nums, curr_num):
        res1 = curr_num
        i_res = i
        print("Invalid number:", res1)
        print("Index of invalid number:", i_res)
        break

found = False
i_low = 0
i_high = i_res - 1
j, k = 0, 1
while not found:
    if res1 == sum(data[j:k]):
        x_min = min(data[j:k])
        x_max = max(data[j:k])
        print('solution part 2:', x_min + x_max)
        break
    else:
        k += 1
        if k >= i_high:
            j += 1
            k = 0
            if j >= i_res:
                print('No solution was found')
                break