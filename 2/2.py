data = "1-3 a: abcde\n"\
       "1-3 b: cdefg\n"\
       "2-9 c: ccccccccc\n"

data = open("input.txt").read()
data = data.split("\n")
data.pop()

def old_validation(pw):
    req, pw_in = pw.split(":")
    num, char = req.split(" ")
    num = list(map(lambda a: int(a), num.split("-")))

    pw_count = pw_in.count(char)

    if num[0] <= pw_count <= num[1]:
        return True, pw_in
    else:
        return False, pw_in

def new_validation(pw):
    req, pw_in = pw.split(":")
    num, char = req.split(" ")
    ind = list(map(lambda a: int(a), num.split("-")))

    pw_count = pw_in.count(char)
    cond1 = pw_in[ind[0]] == char and not pw_in[ind[1]] == char
    cond2 = not pw_in[ind[0]] == char and pw_in[ind[1]] == char
    if cond1 or cond2:
        return True, pw_in
    else:
        return False, pw_in

old_res = []
new_res = []
for pw in data:
    is_correct, pw_in = new_validation(pw)

    if is_correct:
        new_res.append(pw_in)

    is_correct, pw_in = old_validation(pw)

    if is_correct:
        old_res.append(pw_in)

print("old:", len(old_res))
print("new:", len(new_res))