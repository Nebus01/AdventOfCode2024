WIDTH = 101
HEIGHT = 103

file_path = "Your file path"

class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = int(x)
        self.y = int(y)
        self.dx = int(dx)
        self.dy = int(dy)

    def move(self, seconds=1):
        self.x = (self.x + self.dx * seconds) % WIDTH
        self.y = (self.y + self.dy * seconds) % HEIGHT

def quadrant(x, y):
    if y < HEIGHT // 2:
        if x < WIDTH // 2:
            return 0
        if x > WIDTH // 2:
            return 1
    if y > HEIGHT // 2:
        if x < WIDTH // 2:
            return 2
        if x > WIDTH // 2:
            return 3
    return None

# Read input from file
with open(file_path, "r") as fin:
    lines = fin.read().strip().splitlines()

r = []
for l in lines:
    p, v = l.split()
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    r.append(Robot(*p, *v))

#PART1:
riq = [0] * 4
for robot in r:
    robot.move(100)
    if (q := quadrant(robot.x, robot.y)) is not None:
        riq[q] += 1

part1 = 1
for c in riq:
    part1 *= c

#PART2:
part2 = 100
while True:
    for robot in r:
        robot.move()
    part2 += 1
    if len(set((r.x, r.y) for r in r)) == len(r):
        if any(sum(1 for r in r if r.y == y) > 30 for y in range(HEIGHT)):
            break

#Uncomment to see the pattern :)
'''
robotPositions = set((r.x, r.y) for r in robots)
for y in range(HEIGHT):
    for x in range(WIDTH):
        print("#" if (x, y) in robotPositions else ".", end="")
    print()
'''

print("Part 1: ", part1)
print("Part 2: ", part2)
