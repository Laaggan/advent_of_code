data = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

data = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

data = open('data/1.txt', 'r').read()

nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
text_nums = set(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
translate_text_nums = dict({
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'
})
data = data.split("\n")

def solution_part_1(data):
    result = []
    for row in data:
        first = None
        last = None
        for c in row:
            if first is None and c in nums:
                first = c
                continue
            
            if first is not None and c in nums:
                last = c
                continue
        if last is not None:
            result.append(int(first + last))
        else:
            result.append(int(first + first))
    print(sum(result))

def parse_row(row: str):    
    result = []
    for text_num in nums:
        first = True
        while True:
            try:
                if (first):
                    i = row.index(text_num)
                    first = False
                else:
                    i = row.index(text_num, i+1)
                result.append((i, text_num))
                continue
            except ValueError:
                break

    for text_num in text_nums:
        first = True
        while True:
            try:
                if (first):
                    i = row.index(text_num)
                    first = False
                else:
                    i = row.index(text_num, i+len(text_num))
                num = translate_text_nums[text_num]
                result.append((i, num))
                continue
            except ValueError:
                break

    result.sort()
    return int(result[0][1] + result[-1][1])

def solution_part_2(data):
    result = []
    for row in data:
        result.append(parse_row(row))
    print(sum(result))

solution_part_2(data)

