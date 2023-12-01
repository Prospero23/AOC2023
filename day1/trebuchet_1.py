def treb_solve(input: list[str]) -> int:
    result = 0

    for current_string in input:
        first_index = 0
        last_index = len(current_string) - 1
        # find first and last numbers
        while current_string[first_index].isdigit() is not True:
            first_index += 1
        while current_string[last_index].isdigit() is not True:
            last_index -= 1
        # add the two strings together then add them to the result
        current_result = current_string[first_index] + current_string[last_index]
        result += int(current_result)

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="day one of AOC 2023.")
    parser.add_argument("text_file", help="the text file that will be parsed")

    args = parser.parse_args()

    with open(args.text_file, "r") as file:
        text = file.read()
        split_text = text.splitlines()

        result = treb_solve(split_text)
        print("the result is: " + str(result))
