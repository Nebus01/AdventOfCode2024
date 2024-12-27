from collections import deque

file_path = "Your file path"

with open(file_path, "r") as file:
    racetrack = file.readlines()

grid = {
    complex(x, y): cell
    for y, row in enumerate(racetrack)
    for x, cell in enumerate(row.strip())
}

start = next(coord for coord, value in grid.items() if value == "S")
end = next(coord for coord, value in grid.items() if value == "E")

def calculate_distances(source, grid):
    queue = deque([(source, 0)])
    distances = {}

    while queue:
        coord, cost = queue.popleft()
        if coord in distances and distances[coord] <= cost:
            continue
        distances[coord] = cost

        for direction in [1, -1, 1j, -1j]:
            neighbor = coord + direction
            if neighbor in grid and grid[neighbor] != "#":
                queue.append((neighbor, cost + 1))

    return distances

def count_valid_cheats(max_cheat_length, min_savings):
    start_distances = calculate_distances(start, grid)
    end_distances = calculate_distances(end, grid)
    normal_cost = start_distances[end]
    valid_cheats = 0

    for cheat_start, value in grid.items():
        if value == "#":
            continue

        for cheat_length in range(2, max_cheat_length + 1):
            for dx in range(cheat_length + 1):
                dy = cheat_length - dx

                potential_cheat_ends = {
                    cheat_start + dx + dy * 1j,
                    cheat_start - dx + dy * 1j,
                    cheat_start + dx - dy * 1j,
                    cheat_start - dx - dy * 1j
                }

                for cheat_end in potential_cheat_ends:
                    if cheat_end not in grid or grid[cheat_end] == "#":
                        continue

                    cheat_cost = (
                        start_distances.get(cheat_start, float("inf")) +
                        end_distances.get(cheat_end, float("inf")) +
                        cheat_length
                    )

                    if cheat_cost <= normal_cost - min_savings:
                        valid_cheats += 1

    return valid_cheats

#PART1:
part1_result = count_valid_cheats(max_cheat_length=2, min_savings=100)
print("Part 1:", part1_result)

#PART2:
part2_result = count_valid_cheats(max_cheat_length=20, min_savings=100)
print("Part 2:", part2_result)
