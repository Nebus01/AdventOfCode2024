
file_path = "Your file path"

with open(file_path, "r") as f:
    locks = []
    keys = []
    for schematic in f.read().strip().split("\n\n"):
        columns = [0] * 5
        for line in schematic.splitlines():
            for i, char in enumerate(line):
                if char == "#":
                    columns[i] += 1

        if schematic.startswith("#####"):
            locks.append(columns)
        else:
            keys.append(columns)

def count_fitting_pairs(keys, locks):
    fitting_pairs = 0
    
    for key in keys:
        for lock in locks:
            for i in range(5):
                if key[i] + lock[i] > 7:
                    break
            else:
                fitting_pairs += 1

    return fitting_pairs


result = count_fitting_pairs(keys, locks)
print("Final: ", result)


