VALUE_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,  # change to 11 for part1
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


def isLess(hand, check_against: str):
    for i, char in enumerate(hand):
        if VALUE_MAP[char] < VALUE_MAP[check_against[i]]:
            return True
        elif VALUE_MAP[char] > VALUE_MAP[check_against[i]]:
            return False
    return False  # Return False if all characters are equal


class Node:
    def __init__(self, hand, index=0):
        self.hand = hand
        self.index = index
        self.next: "Node | None" = None


class OrderedList:
    def __init__(self):
        self.head = None

    def insert(self, hand, index):
        new_node = Node(hand, index)
        if not self.head or isLess(hand, self.head.hand):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and not isLess(hand, current.next.hand):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(int(current.index))
            current = current.next
        return values


if __name__ == "__main__":
    ordered_list = OrderedList()
    ordered_list.insert("32T3K", 9)
    ordered_list.insert("T55J5", 4)
    ordered_list.insert("KK677", 2)

    print(ordered_list.to_list())  # Output will be: 1 -> 2 -> 3 -> 5
