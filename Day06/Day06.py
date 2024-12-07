from collections import defaultdict
import time
start_time = time.time()

file_path = "Your file path"

with open(file_path, 'r') as file:
    map_data = file.read()

rows = map_data.strip().split('\n')
height, width = len(rows), len(rows[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
direction_chars = "^>v<"  

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        if char in direction_chars:
            start_pos = (i, j)
            start_dir = direction_chars.index(char)  
            break

#PART1
start_time1 = time.time()
guard_pos = start_pos
direction_index = start_dir
visited = set()
visited.add(guard_pos)
max_moves = height * width  

for _ in range(max_moves):
    di, dj = directions[direction_index]
    next_pos = (guard_pos[0] + di, guard_pos[1] + dj)

    if not (0 <= next_pos[0] < height and 0 <= next_pos[1] < width):
        break

    if rows[next_pos[0]][next_pos[1]] == '#':
        direction_index = (direction_index + 1) % 4
    else:
        guard_pos = next_pos
        visited.add(guard_pos)

result_part1 = len(visited)
print("Part1: ", result_part1)
print("Part 1: process finished --- %s seconds ---" % (time.time() - start_time1))

#PART2
#should be optimized can't do it now
start_time2 = time.time()
valid_obstructions = set()

def simulate_with_obstruction(rows, obstruction):
    guard_pos = start_pos
    direction_index = start_dir
    visited_states = set()  
    max_moves = height * width

    for _ in range(max_moves):
        state = (guard_pos, direction_index)
        if state in visited_states:
            return True 
        visited_states.add(state)

        di, dj = directions[direction_index]
        next_pos = (guard_pos[0] + di, guard_pos[1] + dj)

        if not (0 <= next_pos[0] < height and 0 <= next_pos[1] < width):
            return False  
        if rows[next_pos[0]][next_pos[1]] == '#' or next_pos == obstruction:
            direction_index = (direction_index + 1) % 4
        else:
            guard_pos = next_pos

    return False  

for i in range(height):
    for j in range(width):
        if (i, j) == start_pos or rows[i][j] == '#':
            continue
        if simulate_with_obstruction(rows, (i, j)):
            valid_obstructions.add((i, j))

result_part2 = len(valid_obstructions)
print("Part2: ", result_part2)

print("Part 2: process finished --- %s seconds ---" % (time.time() - start_time2))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
