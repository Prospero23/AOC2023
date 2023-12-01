NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_first_num(input: str) -> str:
    window_size = 3

    for i in range(len(input)):
        # if current index is a number return the number
        if input[i].isdigit():
            return input[i]

        # grow or shrink the window
        while window_size <= 5:
            if i + window_size > len(input):
                break
            # current word slice
            word = input[i : i + window_size].lower()

            # check if slice is in nums
            if word in NUMS:
                return str(NUMS[word])

            window_size += 1

        window_size = 3
    return "-1"  # should not happen


def find_last_num(input: str) -> str:
    window_size = 3

    for i in range(len(input) - 1, -1, -1):
        # if current index is a number return the number
        if input[i].isdigit():
            return input[i]

        # grow or shrink the window
        while window_size <= 5:
            if i - window_size + 1 < 0:
                break
            # current word slice
            word = input[i - window_size + 1 : i + 1]
            # check if slice is in nums
            if word in NUMS:
                return str(NUMS[word])

            window_size += 1

        window_size = 3
    return "-1"  # should not happen


def treb_solve(input: list[str]) -> int:
    result = 0
    for current_string in input:
        first_num = find_first_num(current_string)
        last_num = find_last_num(current_string)
        current_result = first_num + last_num  # fix to string or whatever
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


# for first -> start three long, expand to five. each time check if the string is in the
#  set... if not, either expand right or left. Stop if in the set or reaching  a number

# for left, maybe read the number in inverse
