def solver(game: str):
    game_data = game.split(":")[1]
    hands = game_data.split(";")

    min_number = {"red": 0, "blue": 0, "green": 0}

    for hand in hands:
        colors = hand.split(",")
        for color in colors:
            split_color = color.strip().split()
            if int(split_color[0]) > min_number[split_color[1]]:
                min_number[split_color[1]] = int(split_color[0])

    return min_number["red"] * min_number["blue"] * min_number["green"]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="part 2 of the DAY")
    parser.add_argument("text_file", help="text file to read")

    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        text = file.read()
        split_text = text.splitlines()

        result = 0
        for line in split_text:
            current_result = solver(line)
            result += current_result

        print(f"the result is {result}")
