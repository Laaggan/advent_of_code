data = open('input.txt').read().split("\n\n")
keys = ('ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt')

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

print(res)
