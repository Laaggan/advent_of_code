from functools import reduce
import numpy as np
#input_path = "input/test_input_day_4.txt"
input_path = "input/real_input_day_4.txt"
input_data = open(input_path).read().split("\n")
draws, boards = input_data[0], input_data[1:]
draws = list(map(int, draws.split(",")))
boards = [x for x in boards if x != ""]
num_boards = (len(boards) / 5)
boards = [list(map(int, row.split())) for row in boards]

final_boards = []
for i in range(round(num_boards)):
    final_boards.append(np.array(boards[5*i:(5*(i + 1))]))

final_boards = np.array(final_boards)
masks = np.zeros(final_boards.shape)


def star_1(draws, final_boards, masks):
    for draw in draws:
        masks[final_boards == draw] = 1
        for ind, mask in enumerate(masks):
            for i in range(5):
                if np.sum(mask[i, :]) == 5:
                    return np.sum(final_boards[ind][mask != 1])*draw
            for i in range(5):
                if np.sum(mask[:, i]) == 5:
                    return np.sum(final_boards[ind][mask != 1]) * draw


def star_2(draws, final_boards, masks):
    has_won = set(range(len(masks)))
    for draw in draws:
        masks[final_boards == draw] = 1
        for ind, mask in enumerate(masks):
            for i in range(5):
                if np.sum(mask[i, :]) == 5:
                    has_won.discard(ind)
                    if len(has_won) == 0:
                        return np.sum(final_boards[ind][mask != 1])*draw
            for i in range(5):
                if np.sum(mask[:, i]) == 5:
                    has_won.discard(ind)
                    if len(has_won) == 0:
                        return np.sum(final_boards[ind][mask != 1])*draw
    return -1

print(star_1(draws, final_boards, masks))
masks = np.zeros(final_boards.shape)
print(star_2(draws, final_boards, masks))
