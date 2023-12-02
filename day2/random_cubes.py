MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def random_cubes(game: str, max_cubes: dict[str, int] = MAX_CUBES) -> int:
    """Function that returns if hand could be in hand of max_cubes.
    Takes line with format: Game #: 1 red, 2 blue, 3 green; 1 red ...."""

    parts = game.split(":")
    game_number = int(parts[0].split()[1])
    game_data = parts[1]
    grabs = game_data.split(";")  # each hand

    for grab in grabs:
        colors = grab.split(",")
        for color in colors:
            split_color = color.strip().split()
            if int(split_color[0]) > max_cubes[split_color[1]]:
                return 0
    return game_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AOC day 2 baby")
    parser.add_argument(
        "text_file", help="file that you want to zoom through real quick like"
    )

    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        text = file.read()
        split_text = text.splitlines()

        # where sum will be stored
        result = 0

        for line in split_text:
            current_result = random_cubes(line)
            result += current_result

        print(f"the result is {result}")
