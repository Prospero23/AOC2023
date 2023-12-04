def solver(split_lines: list[str]):
    total_cards_length = len(split_lines)
    total_cards = 0
    card_store = [1 for _ in range(total_cards_length)]

    for index, current_card_amount in enumerate(card_store):
        number_add = solve_card(split_lines[index])

        while current_card_amount > 0:
            add_cards(index, number_add, card_store)
            total_cards += 1
            current_card_amount -= 1

    return total_cards


def solve_card(line: str):
    winning_numbers = set()
    result = 0

    game_data = line.split(":")[1]
    number_lists = game_data.split("|")  # winners, losers

    for i, number_list in enumerate(number_lists):
        numbers = number_list.strip().split()

        if i == 0:
            for number in numbers:
                winning_numbers.add(number)
        else:
            for number in numbers:
                if number in winning_numbers:
                    result += 1
    return result


def add_cards(number_start: int, number_add: int, cards_array: list[int]):
    while number_add > 0 and number_start + number_add < len(cards_array):
        cards_array[number_start + number_add] += 1
        number_add -= 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="input scratchofz to be checked")
    parser.add_argument("text_file", help="text file to be read")
    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        input = file.read()
        input_lines = input.splitlines()
        answer = solver(input_lines)

    print(answer)
