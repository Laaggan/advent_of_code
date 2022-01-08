from enum import Enum
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


class PacketTypes(Enum):
    LITERAL = 4
    OPERATOR = -1


def decode_binary_string(binary_string):
    n = len(binary_string)
    result = 0
    for i, v in enumerate(binary_string):
        result += 2**(n-i-1)*int(v)
    return result


INPUT = 'D2FE28'
INPUT = '38006F45291200'
INPUT = 'EE00D40C823060'
INPUT = '8A004A801A8002F478'

binary_string = ''
for c in INPUT:
    binary_string += hex_encoding[c]

packet_version = decode_binary_string(binary_string[0:3])
type_id = decode_binary_string(binary_string[3:6])


def get_packet_version_and_type_id(i, packet_string):
    packet_version = decode_binary_string(packet_string[i:i + 3])
    type_id = decode_binary_string(packet_string[i + 3:i + 6])
    i += 6
    global version_sum
    version_sum += packet_version
    return i, packet_version, type_id


def parse_packet(i, packet_string):
    current_packet_length = 0
    i, packet_version, type_id = get_packet_version_and_type_id(i, packet_string)

    end_of_packet = False
    while not end_of_packet:
        end_of_packet = int(packet_string[i]) == 0
        i += 1
        current_packet_length += 1
        value = decode_binary_string(packet_string[i:i + 4])

        i += 4
        current_packet_length += 4
        if end_of_packet:
            i += current_packet_length % LITERAL_GROUP_LENGTH
    return i, packet_version, type_id

i = 0
decimal_result = []
while i < len(binary_string):
    if type_id == PacketTypes.LITERAL.value:
        i, a, b = parse_packet(i, binary_string)
    else:
        i, a, b = get_packet_version_and_type_id(i, binary_string)
        if int(binary_string[i]) == 0:
            i += 1
            len_packet_string = decode_binary_string(binary_string[i:i + 15])
            i += 15
            sub_packets = binary_string[i:i+len_packet_string]

            j = 0
            while j < len_packet_string:
                j, a, b = parse_packet(j, sub_packets)
            i += len_packet_string

        else:
            i += 1
            num_sub_packets = decode_binary_string(binary_string[i:i + 11])
            i += 11

            j = 0
            for k in range(num_sub_packets):
                j, a, b = parse_packet(j, binary_string[i:])
            i += j

    print(i)
