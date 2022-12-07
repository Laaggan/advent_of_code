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

# commands = Enum("Commands", ["dir", "ls", "cd"])
# Commands(Enum):
#     dir = 

structure = {}
input = input.split("\n")
current_directory = ""
previous_dir = ""

# def traverse_files(text_in):
iter = 0

def parse_input():
    while previous_dir != "/":
        # if line[0] == "$":
        line = input[iter]
        if (line[2:4] == "cd" and line[5:7] != ".."):
            previous_dir = current_directory
            current_directory = line[5:]
            structure[current_directory] = {"dirs": [], "files": []}
            iter += 1
        elif (line[5:7] == ".."):
            current_directory = previous_dir
            iter += 1
        elif (line[2:4] == "ls"):
            iter = iter + 1
            while input[iter][0] != "$":
                if (input[iter][:3] == "dir"):
                    structure[current_directory]["dirs"] = [input[iter][4:], *structure[current_directory]["dirs"]]
                else:
                    size, name = input[iter].split(" ")
                    size = int(size)
                    structure[current_directory]["files"] = [{"name": name, "size": size}, *structure[current_directory]["dirs"]]
                iter += 1

print(structure)