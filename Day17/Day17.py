import re

file_path = "Your file path"

with open(file_path, "r") as file:
    input = file.read()

a, b, c, *instructions = map(int, re.findall(r'\d+', input))


#PART1:
def part1(a, b, c):
    def resolve_operand(op):
        return [0, 1, 2, 3, a, b, c][op]

    pointer = 0
    while pointer < len(instructions):
        operation, operand = instructions[pointer], instructions[pointer + 1]
        pointer += 2

        if operation == 0:
            a = a >> resolve_operand(operand)
        elif operation == 1:
            b = b ^ operand
        elif operation == 2:
            b = resolve_operand(operand) & 0b111
        elif operation == 3:
            pointer = operand if a != 0 else pointer
        elif operation == 4:
            b = b ^ c
        elif operation == 5:
            yield resolve_operand(operand) & 0b111
        elif operation == 6:
            b = a >> resolve_operand(operand)
        elif operation == 7:
            c = a >> resolve_operand(operand)

print("Part 1: ", ",".join(str(x) for x in part1(a, b, c)))            
            
#PART2:
def part2():
    target = instructions[::-1]

    def find_a(a=0, depth=0):
        if depth == len(target):
            return a
        for i in range(8):
            output = list(part1(a * 8 + i, 0, 0))
            if output and output[0] == target[depth]:
                if result := find_a(a * 8 + i, depth + 1):
                    return result
        return 0

    return find_a()



print("Part 2: ", part2())
