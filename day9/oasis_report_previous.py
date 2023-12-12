def difference(lst: list[int]):
    return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]


def find_previous(numbers: list[int]) -> int:
    if all(num == 0 for num in numbers):
        return 0

    difference_list = difference(numbers)
    previous_number = numbers[0] - find_previous(difference_list)

    return previous_number


def get_sum_values(text: str):
    text_lines = text.splitlines()
    total = 0

    for line in text_lines:
        nums_list = line.split()
        integers = [int(number) for number in nums_list]

        current_sum = find_previous(integers)
        total += current_sum
    return total


file = open("day9/input.txt")
text = file.read()

result = get_sum_values(text)
print(result)
