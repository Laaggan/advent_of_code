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
    
    # opened_brackets -= 1
    i = 0
    # TODO: fix extra bracket in a nicer way
    return intermediate_result[0]

for datum in data:
    # print(datum)
    print(parse_brackets(datum[0]))
    print(parse_brackets(datum[1]))