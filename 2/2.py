data = "1-3 a: abcde\n"\
       "1-3 b: cdefg\n"\
       "2-9 c: ccccccccc\n"

data = open("input.txt").read()
data = data.split("\n")
data.pop()

res = []
for pw in data:
    req, pw_in = pw.split(":")
    num, char = req.split(" ")
    num = list(map(lambda a: int(a), num.split("-")))

    pw_count = pw_in.count(char)

    if num[0] <= pw_count <= num[1]:
        res.append(pw_in)

print(len(res))