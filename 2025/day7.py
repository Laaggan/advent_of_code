# Move to utils
def pretty_print_character_matrix(character_matrix):
    print("\n".join(map("".join, character_matrix)) + "\n")

text_data = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............''' 

with open("2025/data/7.txt") as file:
    text_data = file.read()

data = text_data.split("\n")
data_vis = [[c for c in row] for row in text_data.split("\n")]

j_start = None
for j, c in enumerate(data[0]):
    if c == 'S':
        j_start = j
        break

def part1(data, data_vis, j_start):
    beams = set()
    beams.add((0, j_start))
    result_count = 0
    for i in range(len(data) - 1):
        new_beams = []
        for k, beam in enumerate(beams):
            next_i = beam[0] + 1
            current_j = beam[1]
            if data[next_i][current_j] == '^':
                beam1, beam2 = (next_i, current_j - 1), (next_i, current_j + 1)
                new_beams.append((beam, [beam1, beam2]))
                result_count += 1 
                data_vis[next_i][current_j - 1] = "|"
                data_vis[next_i][current_j + 1] = "|"
            else:
                new_beams.append((beam, [(next_i, current_j)]))
                data_vis[next_i][current_j] = "|"
    
        for old_beam, new_beams_list in new_beams:
            beams.remove(old_beam)
        
            for new_beam in new_beams_list:
                beams.add(new_beam)    

    print(result_count)


def part2(data, data_vis, j_start): # Much prettier solution than the first one but does not work due to performance
    result_count = 0
    pos = (0, j_start)
    all_beams = {0: { "pos": pos, "path": [] } }
    new_beams = []
    max_beam_index = max(all_beams.keys())
    for i in range(len(data) - 1):
        print(i)
        for key in all_beams:
            beam = all_beams[key]
            next_i = beam["pos"][0] + 1
            current_j = beam["pos"][1]

            if data[next_i][current_j] == '^':
                beam1, beam2 = (next_i, current_j - 1), (next_i, current_j + 1)
                all_beams[key]["pos"] = beam1
                all_beams[key]["path"].append((next_i, current_j)) # This will keep track of splitters
                
                max_beam_index += 1
                new_beam = (max_beam_index, { "pos": beam2, "path": list(all_beams[key]["path"])}) 
                new_beam = (max_beam_index, { "pos": beam2 })
                new_beams.append(new_beam)

                result_count += 1
                data_vis[next_i][current_j - 1] = "|"
                data_vis[next_i][current_j + 1] = "|"
            else:
                all_beams[key]["pos"] = (next_i, current_j)
                data_vis[next_i][current_j] = "|"
        
        for key, val in new_beams:
            all_beams[key] = val
        new_beams = []
    print(len(all_beams.keys()))

def part21(data, j_start): # Solution which does not keep track of everything
    splitters = []
    for row in data:
        splitter_row = set([idx for idx, val in enumerate(row) if val == "^"])
        if len(splitter_row) > 0:
            splitters.append(splitter_row)
    
    all_beams = [0 for _ in range(len(data[0]))]
    all_beams[j_start] = 1
    for splitter_row in splitters:
        next_beams = list(all_beams)
        for beam_idx, beam_count in enumerate(all_beams):
            if beam_count == 0:
                continue
            
            if beam_idx in splitter_row:
                next_beams[beam_idx + 1] += beam_count # Took a while to realize that there can be more than 1 incoming beam
                next_beams[beam_idx - 1] += beam_count
                next_beams[beam_idx] -= beam_count
        all_beams = list(next_beams)
    print(sum(all_beams))

part21(data, j_start)
