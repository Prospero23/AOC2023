import re


def is_symbol(char):
    pattern = r"[^\w\s\.]"
    return bool(re.match(pattern, char))


def is_adjacent_to_symbol(schematic, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if (
            0 <= nx < len(schematic)
            and 0 <= ny < len(schematic[nx])
            and is_symbol(schematic[nx][ny])
        ):
            return True
    return False


def solver(schematic: str):
    total_sum = 0
    split_schematic = schematic.splitlines()
    for i, line in enumerate(split_schematic):
        j = 0
        while j < len(line):
            if line[j].isdigit():
                start = j
                while j < len(line) and line[j].isdigit():
                    j += 1
                number = int(line[start:j])

                # Check if any digit of the number is adjacent to a symbol
                if any(
                    is_adjacent_to_symbol(split_schematic, i, k)
                    for k in range(start, j)
                ):
                    total_sum += number
            else:
                j += 1
    return total_sum


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="part 2 of the DAY")
    parser.add_argument("text_file", help="text file to read")

    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        schemantic = file.read()
        result = solver(schemantic)

        print(result)
