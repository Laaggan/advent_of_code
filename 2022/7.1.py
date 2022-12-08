from enum import Enum
import math
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
input = open("data/7_real_data.txt").read()

structure = []
input = input.split("\n")
current_directory = None
previous_dir = None

def find_dir(arr: list[dict], current_directory: str, parent: str):
    try:
        for i, dir in enumerate(arr):
            if (dir["dir"] == current_directory and dir["parent"] == parent):
                return i, dir
    except ValueError():
        print("No matching value means something is wrong")

def modify_dir(arr: list[dict], new_dir: dict):
    i, _ = find_dir(arr, new_dir["dir"], new_dir["parent"])
    arr.pop(i)
    arr.insert(i, new_dir)

iter = 0
directory_stack = []
while iter < len(input) - 1:
    split_line = input[iter].split(" ")    
    # If first character is a $ it is a command
    if (split_line[0] == "$"):
        if (split_line[1] == "cd"):
            if (split_line[2] == ".."):
                previous_dir = directory_stack.pop()
                current_directory = directory_stack[-1]
                iter += 1
            else:
                previous_dir = directory_stack[-1] if len(directory_stack) > 0 else None
                current_directory = split_line[2]
                directory_stack.append(current_directory)
                structure.append({"dir": current_directory, "parent": previous_dir, "dirs": [], "files": [], "total_sum": 0})
                iter += 1
        elif (split_line[1] == "ls"):
            iter = iter + 1
            while input[iter][0] != "$":
                split_ls_line = input[iter].split(" ")
                ind, dir = find_dir(structure, current_directory, previous_dir)
                if (split_ls_line[0] == "dir"):
                    dir["dirs"] = [split_ls_line[1], *dir["dirs"]]
                else:
                    size, name = split_ls_line
                    size = int(size)
                    dir["files"] = [{"name": name, "size": size}, *dir["files"]]
                modify_dir(structure, dir)
                if iter >= len(input) - 1:
                    break
                else:
                    iter += 1

def recursive_summing(dir_key, parent):
    i, dir = find_dir(structure, dir_key, parent)
    if (len(dir["dirs"]) == 0):
        if len(dir["files"]) > 0:
            dir["total_sum"] = sum(map(lambda x: x["size"], dir["files"]))
            modify_dir(structure, dir)
            # structure[dir_key]["is_bottom_dir"] = True
            return dir["total_sum"]
        else:
            return 0
    else:
        # structure[dir_key]["is_bottom_dir"] = False
        total_sub_dir_sum = 0
        for sub_dir in dir["dirs"]:
            total_sub_dir_sum += recursive_summing(sub_dir, dir_key)
        
        if len(dir["files"]) > 0:
            dir["total_sum"] = sum(map(lambda x: x["size"], dir["files"])) + total_sub_dir_sum
        else:
            dir["total_sum"] = total_sub_dir_sum
        modify_dir(structure, dir)
        return dir["total_sum"]

recursive_summing("/", None)
sizes_to_delete = sum([dir["total_sum"] for dir in structure if dir["total_sum"] < 100000])
dirs_to_delete = [[dir["dir"] for dir in structure if dir["total_sum"] < 100000]]
print(dirs_to_delete)
print(sizes_to_delete)
_,root = find_dir(structure, "/", None)

used_size = root["total_sum"]
free_size = 70000000 - used_size
needed_size = 30000000 - free_size

closest_to_needed = math.inf
actual_sum = None
structure.sort(key=lambda x: x["total_sum"])
for dir in structure:
    if (needed_size - dir["total_sum"]) < 0:
        # closest_to_needed = needed_size - (free_size + dir["total_sum"])
        actual_sum = dir["total_sum"]
        break

print(actual_sum)
