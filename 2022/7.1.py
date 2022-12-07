from enum import Enum
input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
# input = open("data/7_real_data.txt").read()

# commands = Enum("Commands", ["dir", "ls", "cd"])
# Commands(Enum):
#     dir = 

structure = {}
input = input.split("\n")
current_directory = ""
previous_dir = ""

# def traverse_files(text_in):
iter = 0
directory_stack = []
while iter < len(input) - 1:
    split_line = input[iter].split(" ")    
    # If first character is a $ it is a command
    if (split_line[0] == "$"):
        if (split_line[1] == "cd"):
            if (split_line[2] == ".."):
                directory_stack.pop()
                current_directory = previous_dir
                iter += 1
            else:
                directory_stack.append(split_line[2])
                previous_dir = current_directory
                current_directory = split_line[2]
                structure[current_directory] = {"dirs": [], "files": []}
                iter += 1
        elif (split_line[1] == "ls"):
            iter = iter + 1
            while input[iter][0] != "$":
                split_ls_line = input[iter].split(" ")
                if (split_ls_line[0] == "dir"):
                    structure[current_directory]["dirs"] = [split_ls_line[1], *structure[current_directory]["dirs"]]
                else:
                    size, name = split_ls_line
                    size = int(size)
                    structure[current_directory]["files"] = [{"name": name, "size": size}, *structure[current_directory]["files"]]
                if iter >= len(input) - 1:
                    break
                else:
                    iter += 1

all_dirs = set([key for key in structure])
visited = set()
def recursive_summing(dir_key):
    if visited == all_dirs:
        return
    else:
        visited.add(dir_key)

    if (len(structure[dir_key]["dirs"]) == 0):
        bottom_dir_sum = sum(map(lambda x: x["size"], structure[dir_key]["files"]))
        structure[dir_key]["total_sum"] = bottom_dir_sum
        structure[dir_key]["is_bottom_dir"] = True
        return bottom_dir_sum
    else:
        structure[dir_key]["is_bottom_dir"] = False
        total_sub_dir_sum = 0
        for sub_dir in structure[dir_key]["dirs"]:
            total_sub_dir_sum += recursive_summing(sub_dir)
        
        structure[dir_key]["total_sum"] = sum(map(lambda x: x["size"], structure[dir_key]["files"]))
        structure[dir_key]["total_sum"] += total_sub_dir_sum
        return structure[dir_key]["total_sum"]

recursive_summing("/")
sizes_to_delete = sum([structure[key]["total_sum"] for key in structure if structure[key]["total_sum"] < 100000])
dirs_to_delete = [key for key in structure if structure[key]["total_sum"] < 100000]
print(dirs_to_delete)
print(sizes_to_delete)
print(structure["/"]["total_sum"])