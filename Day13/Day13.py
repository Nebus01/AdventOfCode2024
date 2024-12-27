import numpy as np


input_file = "Your file path"

claw_machines = []

with open(input_file, "r") as file:
    blocks = file.read().strip().split('\n\n')
    for block in blocks:
        lines = block.split('\n')

        button_a_parts = lines[0].split(': ')[1].split(', ')
        button_a = [int(part.split('+')[1]) for part in button_a_parts]

        button_b_parts = lines[1].split(': ')[1].split(', ')
        button_b = [int(part.split('+')[1]) for part in button_b_parts]

        prize_parts = lines[2].split(': ')[1].split(', ')
        prize = [int(part.split('=')[1]) for part in prize_parts]

        claw_machines.append({
            'button_a': button_a,
            'button_b': button_b,
            'prize': prize
        })


def solve_equation(button_a, button_b, prize, increment=0):
    
    a_x, a_y = button_a
    b_x, b_y = button_b
    prize_x, prize_y = prize

    p = np.array([[prize_x + increment], [prize_y + increment]])

    M = np.array([[b_y, -b_x], [-a_y, a_x]])
    det = a_x * b_y - a_y * b_x

    if det == 0:
        return 0

    M_inv = (1 / det) * M

    result = M_inv @ p
    a = round(result[0, 0], 2)
    b = round(result[1, 0], 2)

    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
        return int(a * 3 + b * 1)
    return 0

def solve_claw_machines(claw_machines, increment=0):
    total_tokens = 0
    for machine in claw_machines:
        button_a = machine['button_a']
        button_b = machine['button_b']
        prize = machine['prize']

        total_tokens += solve_equation(button_a, button_b, prize, increment)

    return total_tokens


#PART1 and PART2:
result_part_1 = solve_claw_machines(claw_machines)
result_part_2 = solve_claw_machines(claw_machines, increment=10000000000000)

print("Part 1: ", result_part_1)
print("Part 2: ", result_part_2)
