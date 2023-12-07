from collections import Counter
from Linked_List2 import OrderedList


VALUE_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,  # change to 11 for part1
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

# keep list of hands ? or list of each hand
# each index is for a card strength
hands = [
    OrderedList(),
    OrderedList(),
    OrderedList(),
    OrderedList(),
    OrderedList(),
    OrderedList(),
    OrderedList(),
]


def get_hand_score(input: str):
    result = []
    for card in input:
        result.append(VALUE_MAP[card])
    return result


def get_hand_type(input: list) -> int:
    # change to account for jokers
    count_taker = Counter(input)

    if 1 in count_taker:
        # Exclude the wildcard itself when looking for the most common card
        non_wildcards = [
            (card, count) for card, count in count_taker.items() if card != 1
        ]

        # If there are non-wildcard cards, find the most frequent one
        if non_wildcards:
            most_common_card, most_common_count = max(non_wildcards, key=lambda x: x[1])
            count_taker[most_common_card] += count_taker[1]
        # If all cards are wildcards, treat it as a five-of-a-kind
        else:
            return 6  # Assuming 6 represents a five-of-a-kind

        # Remove the wildcard from the counter
        del count_taker[1]

    card_count = sorted(count_taker.values())

    match card_count:
        case [5]:
            return 6
        case [1, 4]:
            return 5
        case [2, 3]:
            return 4
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 2
        case [1, 1, 1, 2]:
            return 1
        case [1, 1, 1, 1, 1]:
            return 0
    return -1


file = open("day7/input.txt", "r")
text = file.read()

# text = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

split_text = text.splitlines()
scores = []

for i, line in enumerate(split_text):
    line_split = line.split()
    hand = line_split[0]
    score = line_split[1]
    hand_score = get_hand_score(hand)
    value = get_hand_type(hand_score)
    hands[value].insert(hand_score, i)
    scores.append(score)

flattened_list = []
for hand_strength in hands:
    list = hand_strength.to_list()
    for hand in list:
        flattened_list.append(hand)
sum = 0
for i, hand_index in enumerate(flattened_list):
    sum += (i + 1) * int(scores[hand_index])

print(sum)


# result should be 0, 3, 2, 1, 4
