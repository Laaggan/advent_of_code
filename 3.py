from functools import reduce
import numpy as np
#input_path = "input/test_input_day_3.txt"
input_path = "input/real_input_day_3.txt"
input_data = np.array(list(map(lambda x: [int(c) for c in x], open(input_path).read().split("\n"))))


def binary_vector_to_decimal(vector):
    return reduce(lambda acc, x: x[1] * 2 ** x[0] + acc, list(zip(reversed(range(vector.shape[0])), vector)), 0)


def find_most_common_binary_digit_in_column(vector, least_common=False):
    for i in range(vector.shape[0]):
        ones_count = np.sum(vector)
        zeros_count = vector.shape[0] - ones_count
        if not least_common:
            if ones_count >= zeros_count:
                return 1
            else:
                return 0
        else:
            if ones_count >= zeros_count:
                return 0
            else:
                return 1


def star_1(data):
    max_number = data.shape[0]
    gamma_rate = np.zeros((1, data.shape[1]))
    epsilon_rate = np.zeros((1, data.shape[1]))
    for i in range(data.shape[1]):
        ones_count = np.sum(data[:, i])
        zeros_count = max_number - ones_count

        if ones_count > zeros_count:
            gamma_rate[0, i] = 1
            epsilon_rate[0, i] = 0
        else:
            gamma_rate[0, i] = 0
            epsilon_rate[0, i] = 1
    return binary_vector_to_decimal(gamma_rate[0])*binary_vector_to_decimal(epsilon_rate[0])


def star_2(data):
    max_number = data.shape[0]
    gamma_rate = np.zeros((1, data.shape[1]))
    epsilon_rate = np.zeros((1, data.shape[1]))
    new_data_1 = data
    new_data_2 = data
    for i in range(data.shape[1]):
        most_common = find_most_common_binary_digit_in_column(new_data_1[:, i])
        new_data_1 = new_data_1[new_data_1[:, i] == most_common]

        if new_data_1.shape[0] == 1:
            break

    for i in range(data.shape[1]):
        least_common = find_most_common_binary_digit_in_column(new_data_2[:, i], True)
        new_data_2 = new_data_2[new_data_2[:, i] == least_common]

        if new_data_2.shape[0] == 1:
            break
    return binary_vector_to_decimal(new_data_1[0])*binary_vector_to_decimal(new_data_2[0])


print(star_1(input_data))
print(star_2(input_data))