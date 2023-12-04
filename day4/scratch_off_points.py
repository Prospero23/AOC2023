def solve_line(line: str):
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
                    if result == 0:
                        result = 1
                    else:
                        result = result * 2
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="input scratchofz to be checked")
    parser.add_argument("text_file", help="text file to be read")
    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        input = file.read()
        input_lines = input.splitlines()
        answer = 0

    for line in input_lines:
        answer += solve_line(line)
    print(answer)
