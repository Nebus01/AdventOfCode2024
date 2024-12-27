
file_path = "Your file path"

with open(file_path, "r") as file:
    raw_data = file.read()

data_parts = raw_data.split("\n\n")
towel_set = data_parts[0].split(", ")
pattern_list = data_parts[1].split("\n")

def count_pattern_ways(pattern, memo=None):
    if memo is None:
        memo = {}
    if pattern in memo:
        return memo[pattern]
    if pattern == "":
        return 1

    total_ways = 0
    for towel in towel_set:
        if pattern.startswith(towel):
            total_ways += count_pattern_ways(pattern[len(towel):], memo)

    memo[pattern] = total_ways
    return total_ways

#PART1:
part1_result = sum(count_pattern_ways(pattern) > 0 for pattern in pattern_list)

print("Part 1:", part1_result)

#PART2:
part2_result = sum(count_pattern_ways(pattern) for pattern in pattern_list)

print("Part 2:", part2_result)
