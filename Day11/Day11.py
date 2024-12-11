from collections import Counter

file_path = "Your file path"

with open(file_path, "r") as file:
    stones = list(map(int, file.readline().strip().split()))


def split_number(n):
    num_str = str(n)
    half = len(num_str) // 2
    return int(num_str[:half]), int(num_str[half:])

def process_stones_optimized(stones, blinks):
    
    stone_counter = Counter(stones)

    for _ in range(blinks):
        new_counter = Counter()

        for stone, count in stone_counter.items():
            if stone == 0:
                #stone with 0 becomes 1
                new_counter[1] += count
            elif len(str(stone)) % 2 == 0:
                #stone with even number of digits splits
                left, right = split_number(stone)
                new_counter[left] += count
                new_counter[right] += count
            else:
                #stone replaced by stone * 2024
                new_counter[stone * 2024] += count

        stone_counter = new_counter

    return sum(stone_counter.values())

#PART1:
blinks1 = 25
total_stones1 = process_stones_optimized(stones, blinks1)
print("Part 1: ", total_stones1)

#PART2:
blinks2 = 75
total_stones2 = process_stones_optimized(stones, blinks2)
print("Part 2: ", total_stones2)


