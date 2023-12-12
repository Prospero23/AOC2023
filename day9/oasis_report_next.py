def differences(lst):
    return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]


def get_next_value(nums_list: list[int]) -> int:
    if all([num == 0 for num in nums_list]):
        return 0

    differences_list = differences(nums_list)

    next_number = nums_list[-1] + get_next_value(differences_list)

    return next_number


def get_sum_values(text: str):
    text_lines = text.splitlines()
    total = 0

    for line in text_lines:
        nums_list = line.split()
        integers = [int(number) for number in nums_list]

        current_sum = get_next_value(integers)
        total += current_sum
    return total


file = open("day9/input.txt", "r")
text = file.read()


result = get_sum_values(text)

print(result)
