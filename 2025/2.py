data = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

with open("2025/data/2.txt", 'r') as file:
    data = file.read()

data = [list(map(int, x.split("-"))) for x in data.split(",")]

result = []
for pair in data:
    for i in range(pair[0], pair[1] + 1):
        c_str = str(i)
        
        # middle is max mirror
        middle = len(c_str) // 2
        
        for j in range(1, middle + 1):
            # if string is not divisible by a sequence length it cannot be mirror
            if len(c_str) % j != 0:
                continue
            num_patterns = len(c_str) // j
            pattern = c_str[:j]
            is_mirror = True
            for pos in range(1, num_patterns):
                if pattern != c_str[(pos*j):((pos+1)*j)]:
                    is_mirror = False
                    break
            
            if is_mirror:
                result.append(i)
                
print(sum(set(result)))