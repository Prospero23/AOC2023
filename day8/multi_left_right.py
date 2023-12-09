import math


def LCM(a, b):
    return (a * b) // math.gcd(a, b)


def parse_text(input: list[str]):
    node_dict = {}
    starting_nodes = []

    for line in input:
        if len(line) == 0 or "=" not in line:
            continue

        lhs, rhs = [part.strip() for part in line.split("=")]

        rhs_elements = rhs.strip("()").split(",")

        # Cleaning up any extra whitespace from the elements
        rhs_elements = [element.strip() for element in rhs_elements]

        node_dict[lhs] = rhs_elements

        if lhs.endswith("A"):
            starting_nodes.append(lhs)

    return node_dict, starting_nodes


def find_length(input, node_dict):
    steps = 0
    index = 0
    current_node = input

    while current_node[-1] != "Z":
        current_step = instructions[index]
        if current_step == "L":
            current_node = node_dict[current_node][0]
        else:
            current_node = node_dict[current_node][1]

        steps += 1
        index = (index + 1) % len(
            instructions
        )  # Wrap index to start when it reaches the end

    return steps


file = open("day8/input.txt", "r")

text = file.read()

text_lines = text.splitlines()

instructions = list(text_lines[0])
node_dict, nodes_list = parse_text(text_lines)


lengths = []

for node in nodes_list:
    length = find_length(node, node_dict)
    lengths.append(length)

steps = lengths[0]

for length in lengths[1:]:
    steps = LCM(steps, length)


print(steps)


# SAME AS FIRST BUT USE LCM
