import re

data = open("data/4_real_data.txt").read()
data = list(map(lambda x: x.split(","), data.split("\n")))

def get_numbers_from_string(string):
    return list(map(int, re.findall(r'(\d+)', string)))

number_of_contained_elves = 0
for elf_pair in data:
    elf_interval_1 = get_numbers_from_string(elf_pair[0])
    elf_interval_2 = get_numbers_from_string(elf_pair[1])
    
    if (elf_interval_1[0] <= elf_interval_2[0] and elf_interval_1[1] >= elf_interval_2[1]):
        number_of_contained_elves += 1
    elif (elf_interval_1[0] >= elf_interval_2[0] and elf_interval_1[1] <= elf_interval_2[1]):
        number_of_contained_elves += 1
    
print(number_of_contained_elves)