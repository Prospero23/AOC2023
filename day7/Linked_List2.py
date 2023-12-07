def isLess(hand: list[int], check_against: list[int]):
    for i, card_value in enumerate(hand):
        if card_value < check_against[i]:
            return True
        elif card_value > check_against[i]:
            return False
    return False  # Return False if all characters are equal


class Node:
    def __init__(self, hand: list[int], index=0):
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
    ordered_list.insert(
        [
            "3",
            "2",
            "T",
            "3",
            "K",
        ],
        9,
    )

    print(ordered_list.to_list())  # Output will be: 1 -> 2 -> 3 -> 5
