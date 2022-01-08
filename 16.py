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
# Example of a operator packet where length of subpackets is specified
INPUT = '38006F45291200'
# Example of a operator packet where number of upcoming subpackets is specified
INPUT = 'EE00D40C823060'
INPUT = '8A004A801A8002F478'
INPUT = '620080001611562C8802118E34'
INPUT = 'C0015000016115A2E0802F182340'
INPUT = 'A0016C880162017C3686B18A3D4780'

INPUT = '6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C'

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

i = 0
decimal_result = []


def parse_binary_input(i, binary_input):
    i, packet_version, type_id = get_packet_version_and_type_id(i, binary_input)
    # This is the only case where we know exactly what to do
    if type_id == PacketTypes.LITERAL.value:
        i, result = parse_packet(i, binary_input)
        remaining = binary_input[i:]
    else:
        if int(binary_input[i]) == 0:
            i += 1
            len_packet_string = decode_binary_string(binary_input[i:i + 15])
            i += 15
            sub_packets = binary_input[i:i+len_packet_string]

            # So here we probably need to do recursion
            j = 0
            while j < len_packet_string:
                j, remaining = parse_binary_input(j, sub_packets)
            i += len_packet_string
        else:
            i += 1
            num_sub_packets = decode_binary_string(binary_input[i:i + 11])
            i += 11

            j = 0
            remaining = binary_input[i:]
            for k in range(num_sub_packets):
                j, _ = parse_binary_input(j, remaining)
            i += j
            remaining = remaining[i:]
    return i, remaining

parse_binary_input(i, binary_string)
print(version_sum)