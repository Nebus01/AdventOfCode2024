import re

file_path = "Your file path"

with open(file_path, "r") as f:
    initial_values_section, gates_section = f.read().strip().split("\n\n")

variables = {name: int(value) for name, value in (line.split(": ") for line in initial_values_section.splitlines())}
gates = [re.match(r"(\w+) (\w+) (\w+) -> (\w+)", gate).groups() for gate in gates_section.splitlines()]


def simulate_gates(gates, variables):
    remaining_gates = gates.copy()
    while remaining_gates:
        for gate in remaining_gates[:]:
            a, op, b, c = gate
            if a in variables and b in variables:
                if op == "AND":
                    variables[c] = variables[a] & variables[b]
                elif op == "OR":
                    variables[c] = variables[a] | variables[b]
                elif op == "XOR":
                    variables[c] = variables[a] ^ variables[b]
                remaining_gates.remove(gate)

def compute_binary_output(variables):
    z_variables = {name: value for name, value in variables.items() if name.startswith("z")}
    sorted_z = sorted(z_variables.items(), key=lambda x: int(x[0][1:]), reverse=True)
    binary_string = "".join(str(value) for _, value in sorted_z)
    return int(binary_string, 2)

#PART1:
def part1(gates, variables):
    simulate_gates(gates, variables)
    return compute_binary_output(variables)

print("Part 1: ", part1(gates.copy(), variables))

#PART2:
def part2(gates):
    faulty_gates = set()
    for a, op, b, c in gates:
        if c != "z45":
            if c.startswith("z") and op != "XOR":
                faulty_gates.add(c)
        if op == "XOR" and {a[0], b[0]} != {"x", "y"} and not c.startswith("z"):
            faulty_gates.add(c)
        if {a, b} != {"x00", "y00"}:
            if op == "XOR" and {a[0], b[0]} == {"x", "y"} and not any(c in {other_a, other_b} for other_a, other_op, other_b, other_c in gates if other_op == "XOR"):
                faulty_gates.add(c)
            if op == "AND" and not any(c in {other_a, other_b} for other_a, other_op, other_b, other_c in gates if other_op == "OR"):
                faulty_gates.add(c)
    return ",".join(sorted(faulty_gates))

print("Part 2: ", part2(gates))

