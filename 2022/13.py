from functools import reduce


data = open("data/13_small_data.txt", 'r').read()

data = [x.split("\n") for x in data.split("\n\n")]
parsed_data=[]
i = 0
digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

def parse_brackets(member):
    global i
    number = ''
    intermediate_result = []
    while i < len(member):
        c = member[i]
        if (c == "["):
            i += 1
            bracket = parse_brackets(member)
            intermediate_result.append(bracket)
        elif (c == "]"):
            i += 1
            return intermediate_result
        elif (c == ','):
            i += 1
        else:
            while c in digits:
                number += c
                i += 1
                c = member[i]
            intermediate_result.append(int(number))
            number = ''
    
    i = 0
    # TODO: fix extra bracket in a nicer way
    return intermediate_result[0]

def is_list_of_ints(list):
    return reduce(lambda a, b: type(a) is int and b, list)

# j = 0
def compare(left, right):
    j = 0
    right_list_size = len(right)
    left_list_size = len(left)
    # right_is_list_of_ints = is_list_of_ints(right)
    # left_is_list_of_ints = is_list_of_ints(left)

    while j < min(right_list_size, left_list_size):
        if type(left[j]) is int and type(right[j]) is int:
            if right[j] < left[j]:
                return False
            elif right[j] > left[j]:
                return True
            else:
                j += 1
        else:
            if (type(left[j]) is int):
                state = compare([left[j]], right[j])
            elif (type(right[j]) is int):
                state = compare(left[j], [right[j]])
            else:
                state = compare(left[j], right[j])
            
            if state != None:
                    return state
            j += 1
            # if (left_list_size == 1):
            #     compare(left[0], right[0])
            # elif (right_list_size == 1):
            #     compare(left[0], right[0])
    if right_list_size == left_list_size:
        return None
    elif right_list_size < left_list_size:
        return False
    elif right_list_size > left_list_size:
        return True

for datum in data:
    left = parse_brackets(datum[0])
    right = parse_brackets(datum[1])
    j=0
    print(compare(left, right))