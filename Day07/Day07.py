from itertools import product

def calculate_results(lines, allow_concatenation=False):
    part_result = 0

    for line in lines:
        result_str, numbers_str = line.split(":")
        result = int(result_str.strip())
        numbers = list(map(int, numbers_str.strip().split()))

        previous_results = {numbers[0]}

        for next_num in numbers[1:]:
            new_results = {
                prev + next_num for prev in previous_results
            } | {
                prev * next_num for prev in previous_results
            }
            if allow_concatenation:
                new_results |= {
                    int(f'{prev}{next_num}') for prev in previous_results
                }
            previous_results = {r for r in new_results if r <= result}

        if result in previous_results:
            part_result += result

    return part_result

file_path = "Your file path"

with open(file_path, "r") as file:
    lines = [line.strip() for line in file if line.strip()]

#PART1:
part1 = calculate_results(lines, allow_concatenation=False)
print("Part 1:", part1)

#PART2:
part2 = calculate_results(lines, allow_concatenation=True)
print("Part 2:", part2)
