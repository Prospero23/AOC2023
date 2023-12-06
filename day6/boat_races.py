# increases one for each ms held down up to max time
# two pointers
def is_record(time_pressed, race_time, record_dist):
    speed = time_pressed
    time_to_travel = race_time - time_pressed
    if time_to_travel * speed > record_dist:
        return True
    return False


# range of lengths of button press you can do
def get_range(race_time: int, record_dist: int) -> int:
    min_time = 0
    max_time = race_time

    while not is_record(min_time, race_time, record_dist):
        min_time += 1

    while not is_record(max_time, race_time, record_dist):
        max_time -= 1

    return max_time - min_time + 1


file = open("input.txt", "r")
text = file.read()

split_text = text.splitlines()

times = split_text[0].split(":")[1].strip().split()
distances = split_text[1].split(":")[1].strip().split()

print(f"times: {times}")
print(f"distances: {distances}")

result = 1

for i, time in enumerate(times):
    current_range = get_range(int(time), int(distances[i]))
    print(current_range)
    result = current_range * result

print(result)
