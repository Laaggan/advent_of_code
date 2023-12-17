data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

data = """AAAAA 1
AKK22 1
KAK22 1
QKQK2 1
AKKQ5 1
KAKQ5 1
QKK45 1"""
# sum(list[7, 6, 5, 4, 3, 2, 1]) == 28

data = """AAAAA 1
KKKKK 1
AAAAK 1
KKKKA 1
AAAKK 1
KKKAA 1
AAAKQ 1
KKKAQ 1
AAKKQ 1
AAKQJ 1
AKQJT 1
AKQJ9 1"""

data = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41"""
# Should output 6592

data = open("data/7.txt", "r").read()

values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
values_2 = 'AKQJT98765432'
possible_hands = ['5', '4', 'F', '3', 'D', '2', 'H']

data = [x.split() for x in data.split("\n")]
hands = list(map(lambda x: x[0], data))
bids = list(map(lambda x: int(x[1]), data))

hands_result = []
hands_counts = []
for hand in hands:
    counts = dict()
    for c in hand:
        for v in values:
            if c == v:
                if counts.get(c) is None:
                    counts[c] = 1
                else:
                    counts[c] += 1
        
    num_keys = len(counts)
    count_values = counts.values()
    if (num_keys == 1):
        result = '5'
    elif (num_keys == 2):
        if 4 in count_values:
            result = '4'
        else:
            result = 'F'
    elif (num_keys == 3):
        if 3 in count_values:
            result = '3'
        else:
            result = 'D'
    elif (num_keys == 4):
            result = '2'
    elif (num_keys == 5):
        result = 'H'
        
    hands_result.append(result)
    hands_counts.append(counts)

def determine_winners(hands: list[str], ranks: dict, loc_rank: int) -> dict:
    sorted_chars = list(map(lambda x: (values_2.index(x[0][0]), x[0][0], x[1]), hands))
    sorted_chars.sort(reverse=True)
    only_chars = list(map(lambda x: x[0], sorted_chars))

    char_counts = dict()
    for char_ind, char, i in sorted_chars:
        char_counts[char_ind] = only_chars.count(char_ind)
    
    sorted_char_inds = list(char_counts)
    sorted_char_inds.sort()
    for char_ind in sorted_char_inds:
        char = values_2[char_ind]
        if char_counts[char_ind] == 1:
            i = list(filter(lambda x: x[0] == char_ind, sorted_chars))[0][2]
            ranks[i] = loc_rank
            loc_rank -= 1
        else:
            ranks, loc_rank = determine_winners(list(map(lambda y: (y[0][1:], y[1]), filter(lambda x: x[0][0] == char, hands))), ranks, loc_rank)
    
    return ranks, loc_rank

ranks = dict()
unassigned_ranks = reversed(range(1, len(hands_result) + 1))
rank = len(hands_result)
for type in possible_hands:
    type_of_hand_indices = []
    for i, hand_result in enumerate(hands_result):
        if hand_result == type:
            type_of_hand_indices.append(i)
    
    if len(type_of_hand_indices) == 0:
        continue
    if len(type_of_hand_indices) == 1:
        ranks[type_of_hand_indices[0]] = rank
        rank -= 1
    else:
        chars = list(map(lambda x: (data[x][0], x), type_of_hand_indices))
        ranks, rank = determine_winners(chars, ranks, rank)

final_result = 0
for key in ranks:
    final_result += int(data[key][1])*ranks[key]

# print(sum(list(range(1, len(data) + 1))))
for key in ranks:
    print(key, data[key])

print(final_result)