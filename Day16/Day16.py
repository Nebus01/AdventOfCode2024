from collections import deque

file_name = "Your file path"

with open(file_name, "r") as file:
    m = [list(line.rstrip()) for line in file]

def findRoutes(m: list[list[str]]):
    r, c = len(m), len(m[0])
    s = None
    e = None

    for r in range(r):
        for c in range(c):
            if m[r][c] == 'S':
                s = (r, c)
            elif m[r][c] == 'E':
                e = (r, c)
        if s and e:
            break

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    routes = []
    visited = {}
    q = deque([(s, [s], 0, 0)]) 

    while q:
        (x, y), h, score, d = q.popleft()

        if (x, y) == e:
            routes.append((h, score))
            continue

        if ((x, y), d) in visited and visited[((x, y), d)] < score:
            continue

        visited[((x, y), d)] = score
            
        for n_d, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and m[nx][ny] != '#' and (nx, ny) not in h:
                if n_d == d:
                    q.append(((nx, ny), h + [(nx, ny)], score + 1, n_d))
                else:
                    q.append(((x, y), h + [], score + 1000, n_d))

    return routes


#PART1:
routes = findRoutes(m)
min = min(route[1] for route in routes)
print("Part 1: ", min)


#PART2:
best = [route for route in routes if route[1] == min]
out = {tile for route in best for tile in route[0]}
print("Part 2: ", len(out))

