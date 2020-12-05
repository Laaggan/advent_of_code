import re
data = open('input.txt.txt').read().split("\n\n")
keys = ('ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt')


def old_case(data):
    res = 0
    for passport in data:
        is_valid = False
        current_keys = []
        # Vanilla split splits on any white space
        # you live and you learn!
        _dict = [entry.split(":") for entry in passport.split()]

        for key, value in _dict:
            current_keys.append(key)

        if len(current_keys) == 8:
            is_valid = True
        elif 'cid' not in current_keys and len(current_keys) == 7:
            is_valid = True

        if is_valid:
            res += 1
    return res


def validate_height(_input):
    try:
        n = len(_input)
        unit = _input[-2:]
        value = int(_input[:(n - 2)])
    except:
        return False

    if unit == 'cm':
        res = 150 <= value <= 193
    elif unit == 'in':
        res = 59 <= value <= 76
    else:
        return False

    return res


def validate_eye_color(_input):
    valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    res = _input in valid_colors
    return res


def validate_hair_color(_input):
    expr = "#[0-9a-f]{6}"
    res = bool(re.search(expr, _input))
    return res


def validate_passport_number(_input):
    expr = "[\d]{9}"
    res = bool(re.search(expr, _input))
    return res


def new_case(data):
    res = 0
    for passport in data:
        is_valid = False
        current_keys = []
        # Vanilla split splits on any white space
        # you live and you learn!
        _dict = [entry.split(":") for entry in passport.split()]

        for key, value in _dict:
            if key == "byr" and not 1920 <= int(value) <= 2020:
                break
            elif key == "iyr" and not 2010 <= int(value) <= 2020:
                break
            elif key == "eyr" and not 2020 <= int(value) <= 2030:
                break
            elif key == "hgt" and not validate_height(value):
                break
            elif key == "ecl" and not validate_eye_color(value):
                break
            elif key == "hcl" and not validate_hair_color(value):
                break
            elif key == "pid" and not validate_passport_number(value):
                break
            current_keys.append(key)

        if len(current_keys) == 8:
            is_valid = True
        elif 'cid' not in current_keys and len(current_keys) == 7:
            is_valid = True

        if is_valid:
            res += 1
    return res


#print(old_case(data))

# 163 is too high
# 157 is too high
print(new_case(data))
