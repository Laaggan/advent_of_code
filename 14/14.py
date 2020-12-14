import re
input_path = "small_input.txt"
data = open(input_path).read().split("\n")

mask_regex = "(?=mask = ).+"
mask = re.match(mask_regex, data[0])

print(mask)