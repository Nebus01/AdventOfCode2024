
file_path = "Your file path"

with open(file_path, "r") as file:
    inputs = file.read().splitlines()

keypad_numeric = {
    "7": -2-3j, "8": -1-3j, "9": -3j,
    "4": -2-2j, "5": -1-2j, "6": -2j,
    "1": -2-1j, "2": -1-1j, "3": -1j,
    " ": -2, "0": -1, "A": 0
}

keypad_directional = {
    " ": -2, "^": -1, "A": 0,
    "<": -2+1j, "v": -1+1j, ">": 1j
}

cached_moves = {}

def local_move(position, target, depth, keypad):
    if (position, target, depth) in cached_moves:
        return cached_moves[(position, target, depth)]

    horizontal_move = ">" * int(target.real - position.real) if target.real > position.real else "<" * int(position.real - target.real)
    vertical_move = "v" * int(target.imag - position.imag) if target.imag > position.imag else "^" * int(position.imag - target.imag)

    possible_paths = [horizontal_move + vertical_move, vertical_move + horizontal_move]

    if position.imag == keypad[" "].imag and target.real == keypad[" "].real:
        possible_paths.remove(horizontal_move + vertical_move)
    elif target.imag == keypad[" "].imag and position.real == keypad[" "].real:
        possible_paths.remove(vertical_move + horizontal_move)

    min_path_length = min([calculate_path_length(path + "A", depth - 1, keypad_directional) for path in possible_paths])
    cached_moves[(position, target, depth)] = min_path_length
    return min_path_length

def calculate_path_length(sequence, depth, keypad):
    if depth == 0:
        return len(sequence)

    current_position = keypad["A"]
    total_steps = 0

    for char in sequence:
        target_position = keypad[char]
        total_steps += local_move(current_position, target_position, depth, keypad)
        current_position = target_position

    return total_steps

def solve_puzzle(inputs, max_depth):
    total = 0
    for sequence in inputs:
        path_length = calculate_path_length(sequence, max_depth, keypad_numeric)
        total += path_length * int(sequence[:3])
    return total

#PART1:
print("Part 1:", solve_puzzle(inputs, 3))

#PART2:
print("Part 2:", solve_puzzle(inputs, 26))
