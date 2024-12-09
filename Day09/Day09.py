'''
Note that I had to take inspiration from other users on the char to use for the free char
cause apparently a bad choice would mess up the checksum result, therefore the kinda weird 
choice of the free char :).
'''


file_path = "Your file path"

with open(file_path, "r") as f:
    puzzle_input = f.read()

#PART1:
def parse_disk(text):
    digits = map(int, text)
    disk = []
    expect_file_segment = True
    file_id = 0
    for digit in digits:
        if expect_file_segment:
            disk.extend(chr(file_id) for _ in range(digit))
            file_id += 1
        else:
            disk.extend("🫥" for _ in range(digit))
        expect_file_segment = not expect_file_segment
    return disk


def compute_checksum(disk):
    checksum = 0
    for i, block_id_char in enumerate(disk):
        if block_id_char != "🫥":
            checksum += i * ord(block_id_char)
    return checksum


def compact_disk_part1(disk):
    first_dot = 0
    while True:
        while disk and disk[-1] == "🫥":
            disk.pop()
        try:
            first_dot = disk.index("🫥", first_dot)
        except ValueError:
            break
        disk[first_dot] = disk[-1]
        disk.pop()
    return disk

disk_part1 = parse_disk(puzzle_input)
result_part1 = compute_checksum(compact_disk_part1(disk_part1))
print(f"Part 1: {result_part1}")

#PART2:
def compact_disk_part2(disk):
    while disk and disk[-1] == "🫥":
        disk.pop()

    if not disk:
        return
    last_char = disk[0]
    length = 1
    files = []
    for i in range(1, len(disk)):
        if disk[i] != last_char:
            if last_char != "🫥":
                files.append(("".join(disk[i - length : i]), i - length))
            length = 1
            last_char = disk[i]
        else:
            length += 1
    if last_char != "🫥":
        files.append(("".join(disk[len(disk) - length :]), len(disk) - length))

    disk_str = "".join(disk)
    while files:
        file_blocks, file_start = files.pop()
        flen = len(file_blocks)
        free_segment = "🫥" * flen
        try:
            first_slot = disk_str.index(free_segment, 0, file_start)
        except ValueError:
            continue
        disk_str = (
            disk_str[:first_slot]
            + file_blocks
            + disk_str[first_slot + flen : file_start]
            + free_segment
            + disk_str[file_start + flen :]
        )

    disk.clear()
    disk.extend(disk_str)
    return disk

disk_part2 = parse_disk(puzzle_input)
result_part2 = compute_checksum(compact_disk_part2(disk_part2))
print(f"Part 2: {result_part2}")
