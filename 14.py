from numpy import Inf

path = 'input/real_input_day_14.txt'
data = open(path).read().split('\n\n')
template = data[0]
rules = [a.split(' -> ') for a in data[1].split('\n')]
rules_dict = {b: c for b, c in rules}
print(template)

def star_1():
    updated_template = template
    N = 10

    for i in range(N):
        new_template = ''
        for j in range(len(updated_template) - 1):
            inserted_value = rules_dict[updated_template[j:(j + 2)]]
            new_template = new_template + updated_template[j] + inserted_value
        updated_template = new_template + updated_template[-1]

    values = list(set(updated_template))
    result = {x: updated_template.count(x) for x in values}

    c_max = 0
    c_min = Inf
    for key, value in result.items():
        if value > c_max:
            c_max = value
        if value < c_min:
            c_min = value

    return c_max, c_min, c_max - c_min

def star_2():
    generating_rules_dict = {key: (f'{key[0]}{value}', f'{value}{key[1]}') for key, value in rules_dict.items()}
    result_dict = {key: 0 for key in rules_dict.keys()}
    count_dict = {value: 0 for _, value in rules_dict.items()}
    empty_dict = {key: 0 for key in rules_dict.copy().keys()}
    N = 40
    for j in range(len(template) - 1):
        result_dict[template[j:(j + 2)]] += 1
    for c in template:
        count_dict[c] += 1

    for k in range(N):
        new_result_dict = empty_dict.copy()
        for current_pair, count in result_dict.items():
            if count > 0:
                add_pair_1, add_pair_2 = generating_rules_dict[current_pair]
                added_char = rules_dict[current_pair]
                new_result_dict[add_pair_1] += count
                new_result_dict[add_pair_2] += count
                count_dict[added_char] += count
        result_dict = new_result_dict

    c_max = 0
    c_min = Inf
    for key, value in count_dict.items():
        if value > c_max:
            c_max = value
        if value < c_min:
            c_min = value

    return c_max, c_min, c_max - c_min



print(star_1())
print(star_2())