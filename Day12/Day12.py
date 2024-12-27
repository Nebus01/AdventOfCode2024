
input_file = "Your file path"

with open(input_file, "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

#PART1:
def get_connected_components(grid):
    n, m = len(grid), len(grid[0])
    component = [[-1 for _ in range(m)] for _ in range(n)]
    components = {}
    ctr = 0

    def flood_fill(i, j, c):
        if i < 0 or i >= n or j < 0 or j >= m or component[i][j] != -1 or grid[i][j] != grid[start[0]][start[1]]:
            return
        component[i][j] = c
        if c not in components:
            components[c] = []
        components[c].append((i, j))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            flood_fill(i + dx, j + dy, c)

    for i in range(n):
        for j in range(m):
            if component[i][j] == -1:
                start = (i, j)
                flood_fill(i, j, ctr)
                ctr += 1

    return components, component

def calculate_perimeter(grid, components, component):
    n, m = len(grid), len(grid[0])
    total_cost = 0

    for c in components.keys():
        perimeter = 0
        for i, j in components[c]:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + dx, j + dy
                if ni < 0 or ni >= n or nj < 0 or nj >= m or component[ni][nj] != c:
                    perimeter += 1
        total_cost += len(components[c]) * perimeter

    return total_cost

components, component = get_connected_components(grid)
part1_result = calculate_perimeter(grid, components, component)
print("Part 1: ",part1_result)

#PART2:
def get_boundary_size(c, components, grid, component):
    n, m = len(grid), len(grid[0])
    sides = []

    for i, j in components[c]:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + dx, j + dy
            if ni < 0 or ni >= n or nj < 0 or nj >= m or component[ni][nj] != c:
                sides.append([(i, j, dx, dy)])

    def adj_side(s1, s2):
        return (
            abs(s1[0] - s2[0]) == 1 - abs(s1[2])
            and abs(s1[1] - s2[1]) == 1 - abs(s1[3])
            and s1[2] == s2[2]
            and s1[3] == s2[3]
        )

    while True:
        changed = False
        i = 0
        while i < len(sides):
            j = i + 1
            while j < len(sides):
                if any(adj_side(s1, s2) for s1 in sides[i] for s2 in sides[j]):
                    sides[i] += sides[j]
                    sides.pop(j)
                    changed = True
                else:
                    j += 1
            i += 1
        if not changed:
            break

    return len(sides)

def calculate_boundary_size(grid, components, component):
    total_cost = 0
    for c in components.keys():
        total_cost += len(components[c]) * get_boundary_size(c, components, grid, component)
    return total_cost


part2_result = calculate_boundary_size(grid, components, component)
print("Part 2: ",part2_result)
