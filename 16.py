from enum import Enum
from functools import reduce
INPUT = open('input/real_input_day_16.txt').read()
hex_encoding = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
LITERAL_GROUP_LENGTH = 5
version_sum = 0
binary_string = ''


class PacketTypes(Enum):
    LITERAL = 4
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL = 7


for c in INPUT:
    binary_string += hex_encoding[c]


def decode_binary_string(binary_string):
    n = len(binary_string)
    result = 0
    for i, v in enumerate(binary_string):
        result += 2**(n-i-1)*int(v)
    return result


def get_packet_version_and_type_id(i, packet_string):
    packet_version = decode_binary_string(packet_string[i:i + 3])
    type_id = decode_binary_string(packet_string[i + 3:i + 6])
    i += 6
    global version_sum
    version_sum += packet_version
    return i, packet_version, type_id


def parse_packet(i, packet_string):
    result_string = ''
    while True:
        if int(packet_string[i]) == 0:
            i += 1
            result_string += packet_string[i:i + 4]
            i += 4
            break
        i += 1
        result_string += packet_string[i:i + 4]
        value = decode_binary_string(packet_string[i:i + 4])
        i += 4
    return i, result_string


def parse_binary_input(i, binary_input):
    i, packet_version, type_id = get_packet_version_and_type_id(i, binary_input)
    if type_id == PacketTypes.LITERAL.value:
        i, values = parse_packet(i, binary_input)
        remaining = binary_input[i:]
    else:
        if int(binary_input[i]) == 0:
            i += 1
            len_packet_string = decode_binary_string(binary_input[i:i + 15])
            i += 15
            sub_packets = binary_input[i:i+len_packet_string]

            j = 0
            values = []
            while j < len_packet_string:
                j, remaining, value = parse_binary_input(j, sub_packets)
                if type(value) == str:
                    values.append(decode_binary_string(value))
                else:
                    values.append(value)
            i += len_packet_string
        else:
            i += 1
            num_sub_packets = decode_binary_string(binary_input[i:i + 11])
            i += 11

            j = 0
            remaining = binary_input[i:]
            values = []
            for k in range(num_sub_packets):
                j, _, value = parse_binary_input(j, remaining)
                if type(value) == str:
                    values.append(decode_binary_string(value))
                else:
                    values.append(value)
            i += j
            remaining = remaining[i:]

        if type_id == PacketTypes.SUM.value:
            result = reduce(lambda x, y: x+y, values)
        elif type_id == PacketTypes.PRODUCT.value:
            result = reduce(lambda x, y: x*y, values, 1)
        elif type_id == PacketTypes.MAXIMUM.value:
            result = max(values)
        elif type_id == PacketTypes.MINIMUM.value:
            result = min(values)
        elif type_id == PacketTypes.GREATER_THAN.value:
            result = 1 if values[0] > values[1] else 0
        elif type_id == PacketTypes.LESS_THAN.value:
            result = 1 if values[0] < values[1] else 0
        elif type_id == PacketTypes.EQUAL.value:
            result = 1 if values[0] == values[1] else 0

        values = result

    return i, remaining, values


i = 0
print(parse_binary_input(i, binary_string))