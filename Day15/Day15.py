
file_path = "Your file path"

with open(file_path, "r") as file:
    unpgrid, m = file.read().split("\n\n")

m = m.replace("\n", "")
dir = {"<": -1, ">": 1, "^": -1j, "v": 1j}

def parsing(unparsedGrid):
  grid = {i + j*1j: c for j, row in enumerate(unparsedGrid.split("\n")) for i, c in enumerate(row)} # grid is dict with coordinates as keys in form of complex numbers
  robot = next(coord for coord, c in grid.items() if c == "@")
  return grid, robot


#PART1:
def part1(unpgrid, m, dir):
  grid, robot = parsing(unpgrid)

  def move(coord, dir):
    coord += dir
    if grid.get(coord, "#") == "#":
      return False
    if grid.get(coord, "#") == "." or move(coord, dir):
      grid[coord] = grid[coord-dir]
      grid[coord-dir] = "."
      return True
    return False

  for command in m:
    if move(robot, dir[command]):
      robot += dir[command]
  
  return int(sum(coord.real + 100*coord.imag for coord, c in grid.items() if c == "O"))

print("Part 1: ", part1(unpgrid, m, dir))


#PART2:
def part2(unpgrid, m, dir):
  unpgrid = unpgrid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
  grid, r = parsing(unpgrid)

  def move(coord, dir):
    coord += dir
    if grid.get(coord, "#") == "#":
      return False
    if grid.get(coord, "#") == "."\
    or (grid.get(coord, "#") == "[" and move(coord+1, dir) and move(coord, dir))\
    or (grid.get(coord, "#") == "]" and move(coord-1, dir) and move(coord, dir)):
      grid[coord] = grid[coord-dir]
      grid[coord-dir] = "."
      return True
    return False
  
  for com in m:
    c = grid.copy()
    if move(r, dir[com]):
      r += dir[com]
    else:
      grid = c
  
  return int(sum(coord.real + 100*coord.imag for coord, c in grid.items() if c == "["))

print("Part 2: ", part2(unpgrid, m, dir))
