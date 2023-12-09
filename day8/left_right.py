def parse_text(input: list[str]):
    node_dict = {}

    for line in input:
        if len(line) == 0 or "=" not in line:
            continue

        lhs, rhs = [part.strip() for part in line.split("=")]

        rhs_elements = rhs.strip("()").split(",")

        # Cleaning up any extra whitespace from the elements
        rhs_elements = [element.strip() for element in rhs_elements]

        node_dict[lhs] = rhs_elements

    return node_dict


file = open("day8/input.txt", "r")

text = file.read()

text_lines = text.splitlines()

instructions = list(text_lines[0])
node_dict = parse_text(text_lines)


current_node = "AAA"
steps = 0
index = 0

# Navigate the network
while current_node != "ZZZ":
    current_step = instructions[index]
    if current_step == "L":
        current_node = node_dict[current_node][0]
    else:
        current_node = node_dict[current_node][1]

    steps += 1
    index = (index + 1) % len(
        instructions
    )  # Wrap index to start when it reaches the end

print(steps)
