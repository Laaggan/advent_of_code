data = open('input.txt').read().split()
data = [int(x) for x in data]

n = len(data)

def find_sum_of_num(param, nums, x):
    assert len(nums) == param, 'Input sequence must have 5 elements'
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
        print(curr_num)
        break