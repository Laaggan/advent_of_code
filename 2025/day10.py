import itertools
from scipy.sparse import csr_array, triu
from scipy.sparse.csgraph import dijkstra

text_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

with open("2025/data/10.txt") as file:
    text_input = file.read()

def transform_state(state, button_seq):
    next_state = list(state)
    for button in button_seq:
        next_state[button] = 1 if state[button] == 0 else 0
    return tuple(next_state)

def part1():
    data = [(
        tuple([1 if c == "#" else 0 for c in row.split()[0][1:-1]]),
        [list(map(int, button[1:-1].split(","))) for button in row.split()[1:-1]],
        list(map(int, row.split()[-1][1:-1].split(",")))) for row in text_input.split("\n")]

    result = []
    for row in data:
        n = len(row[0])
        target_state = row[0]
        adj_matrix = [[0 for _ in range(2**n)] for _ in range(2**n)]
        button_seqs = row[1]
        state_to_idx = {}
        combs = [comb for comb in itertools.product(range(2), repeat=len(row[0]))]
        for i, comb in enumerate(combs):
            state_to_idx[comb] = i
        
        for comb in combs:
            for button_seq in button_seqs:
                comb_idx = state_to_idx[comb]
                next_state = transform_state(comb, button_seq)
                next_state_idx = state_to_idx[next_state]
                i, j = min(comb_idx, next_state_idx), max(comb_idx, next_state_idx) # To make it upper triangular
                adj_matrix[i][j] = 1
        
        # print(adj_matrix)
        A = csr_array(adj_matrix, dtype='int32')
        target_idx = state_to_idx[target_state]
        dist_matrix, predecessors = dijkstra(csgraph=A, directed=False, indices=None, return_predecessors=True)
        dist_matrix[0][target_idx]
        
        result.append(dist_matrix[0][target_idx])
    print(sum(result))

part1()

