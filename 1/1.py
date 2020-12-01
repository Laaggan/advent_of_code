raw_data = open('input.txt').read().split('\n')
raw_data.pop()
data = list(map(lambda a: int(a), raw_data))

def find_sum_of_two_numbers(data, sum):
    for x in data:
        for y in data:
            if x + y == sum:
                return x*y

def find_sum_of_three_numbers(data, sum):
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == sum:
                    return x*y*z

print("Sum of two numbers:", find_sum_of_two_numbers(data, 2020))
print("Sum of three numbers:", find_sum_of_three_numbers(data, 2020))