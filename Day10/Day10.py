
file_path = "Your file path"

with open(file_path, 'r') as file:
    topographic_map = [list(map(int, line.strip())) for line in file.readlines()]


trailheads = []

for row in range(len(topographic_map)):
    for col in range(len(topographic_map[0])):
        if topographic_map[row][col] == 0:
            trailheads.append((row, col))

#PART1:
def calculate_trailhead_score(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [start]
    reachable_nines = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:
                    stack.append((nx, ny))

    return len(reachable_nines)

total_score = 0

for trailhead in trailheads:
    total_score += calculate_trailhead_score(topographic_map, trailhead)

print("Part 1: ", total_score)

#PART2:
def calculate_trailhead_rating(grid, start):
    rows, cols = len(grid), len(grid[0])
    cache = {}

    def dfs(x, y):
        if (x, y) in cache:
            return cache[(x, y)]
        if grid[x][y] == 9:
            return 1

        total_trails = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == grid[x][y] + 1:
                    total_trails += dfs(nx, ny)

        cache[(x, y)] = total_trails
        return total_trails

    return dfs(*start)

total_rating = 0
for trailhead in trailheads:
    total_rating += calculate_trailhead_rating(topographic_map, trailhead)

print("Part 2: ", total_rating) 
