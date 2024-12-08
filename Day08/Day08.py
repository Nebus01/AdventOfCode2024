
file_path = "Your file path"


with open(file_path, "r") as file:
    grid = [line.strip() for line in file if line.strip()]
    
#PART1:   
def part1(grid):
    N, M = len(grid), len(grid[0])
    nodes = {}
    antinodes = set()

    for i in range(N):
        for j in range(M):
            if grid[i][j] != '.':
                freq = grid[i][j]
                nodes[freq] = nodes.get(freq, []) + [(i, j)]

    for freq, node_list in nodes.items():
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                x1, y1 = node_list[i]
                x2, y2 = node_list[j]

                newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
                if 0 <= newx < N and 0 <= newy < M:
                    antinodes.add((newx, newy))

                newx, newy = x1 + (x1 - x2), y1 + (y1 - y2)
                if 0 <= newx < N and 0 <= newy < M:
                    antinodes.add((newx, newy))

    return len(antinodes)

result_part1 = part1(grid)
print("Part 1: ", result_part1)

#PART2:
def part2(grid):
    N, M = len(grid), len(grid[0])
    nodes = {}
    antinodes = set()

    for i in range(N):
        for j in range(M):
            if grid[i][j] != '.':
                freq = grid[i][j]
                nodes[freq] = nodes.get(freq, []) + [(i, j)]

    for freq, node_list in nodes.items():
        L = len(node_list)
        for i in range(L):
            for j in range(L):
                if i == j:
                    continue

                x1, y1 = node_list[i]
                x2, y2 = node_list[j]

                for factor in range(1, max(N, M)):
                    newx, newy = x1 + factor * (x2 - x1), y1 + factor * (y2 - y1)
                    if 0 <= newx < N and 0 <= newy < M:
                        antinodes.add((newx, newy))
                    else:
                        break

    for positions in nodes.values():
        for pos in positions:
            antinodes.add(pos)

    return len(antinodes)



result_part2 = part2(grid)
print("Part 2: ", result_part2)
