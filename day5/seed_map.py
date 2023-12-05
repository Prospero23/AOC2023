example_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def parse_data(data):
    # Split the data into sections
    sections = data.split("\n\n")

    # Extract seeds
    seeds = list(map(int, sections[0].split(": ")[1].split()))

    # Parse each map
    maps = {}
    for section in sections[1:]:
        lines = section.split("\n")
        map_name = lines[0].strip(":")
        map_data = [list(map(int, line.split())) for line in lines[1:]]
        maps[map_name] = map_data

    return seeds, maps


def map_number(number, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= number < src_start + length:
            offset = number - src_start
            return dest_start + offset
    return number  # If not in the mapping, return the number itself


def process_seeds(seeds, maps):
    results = []

    for seed in seeds:
        soil = map_number(seed, maps["seed-to-soil map"])
        fertilizer = map_number(soil, maps["soil-to-fertilizer map"])
        water = map_number(fertilizer, maps["fertilizer-to-water map"])
        light = map_number(water, maps["water-to-light map"])
        temperature = map_number(light, maps["light-to-temperature map"])
        humidity = map_number(temperature, maps["temperature-to-humidity map"])
        location = map_number(humidity, maps["humidity-to-location map"])
        results.append(location)

    return results


with open("input.txt", "r") as file:
    data = file.read()
    seeds, maps = parse_data(data)
    processed_locations = process_seeds(seeds, maps)
    print(sorted(processed_locations))
