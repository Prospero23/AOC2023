from collections import Counter
from Linked_List import OrderedList

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


def get_hand_type(input: str) -> int:
    count_taker = Counter(input)
    card_count = sorted((list(count_taker.values())))

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


split_text = text.splitlines()
scores = []

for i, line in enumerate(split_text):
    line_split = line.split()
    hand = line_split[0]
    score = line_split[1]
    value = get_hand_type(hand)
    hands[value].insert(hand, i)
    scores.append(score)

flattened_list = []
for hand_strength in hands:
    list = hand_strength.to_list()
    for hand in list:
        flattened_list.append(hand)
print(flattened_list)
print(scores)
sum = 0
for i, hand_index in enumerate(flattened_list):
    sum += (i + 1) * int(scores[hand_index])

print(sum)


# result should be 0, 3, 2, 1, 4
