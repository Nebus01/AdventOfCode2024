
file_path = "Your file path"

with open(file_path, "r") as file:
    grid = [line.strip() for line in file]

#PART1

#Word to find
word = "XMAS"

directions = [
    (0, 1),   # horizontal right
    (1, 0),   # vertical down
    (1, 1),   # diagonal down-right
    (1, -1),  # diagonal down-left
    (0, -1),  # horizontal left
    (-1, 0),  # vertical up
    (-1, -1), # diagonal up-left
    (-1, 1)   # diagonal up-right
]

rows = len(grid)
cols = len(grid[0])

def word_exists(start_row, start_col, direction):
    for i in range(len(word)):
        row = start_row + i * direction[0]
        col = start_col + i * direction[1]
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != word[i]:
            return False
    return True

count = 0
for r in range(rows):
    for c in range(cols):
        for direction in directions:
            if word_exists(r, c, direction):
                count += 1


print("Part 1: ", count)


#PART2

diagonal_pairs = [
    [(-1, -1), (1, 1)],  # M in top-left, S in bottom-right
    [(-1, 1), (1, -1)],  # M in top-right, S in bottom-left
    [(1, -1), (-1, 1)],  # M in bottom-left, S in top-right
    [(1, 1), (-1, -1)]   # M in bottom-right, S in top-left
]

count2 = 0
for r in range(1, rows - 1): 
    for c in range(1, cols - 1):  
        if grid[r][c] == 'A':
            valid = 0
            for pair in diagonal_pairs:
                d1, d2 = pair
                if (grid[r + d1[0]][c + d1[1]] == 'M' and 
                    grid[r + d2[0]][c + d2[1]] == 'S'):
                    valid += 1
            if valid == 2:  
                count2 += 1

print("Part 2: ", count2)          
            
