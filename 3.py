from functools import reduce

import numpy as np

#input_path = "input/test_input_day_3.txt"
input_path = "input/real_input_day_3.txt"
input_data = np.array(list(map(lambda x: [int(c) for c in x], open(input_path).read().split("\n"))))
#input_data = [x.split() for x in file]


def binary_vector_to_decimal(vector):
    return reduce(lambda acc, x: x[1] * 2 ** x[0] + acc, list(zip(reversed(range(vector.shape[0])), vector)), 0)


def star_1(data):
    max = data.shape[0]
    gamma_rate = np.zeros((1, data.shape[1]))
    epsilon_rate = np.zeros((1, data.shape[1]))
    for i in range(data.shape[1]):
        ones_count = np.sum(data[:, i])
        zeros_count = max - ones_count

        if ones_count > zeros_count:
            gamma_rate[0, i] = 1
            epsilon_rate[0, i] = 0
        else:
            gamma_rate[0, i] = 0
            epsilon_rate[0, i] = 1
    return binary_vector_to_decimal(gamma_rate[0])*binary_vector_to_decimal(epsilon_rate[0])


def star_2(data):
    pass


print(star_1(input_data))