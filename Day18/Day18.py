
file_path = "Your file path"

with open(file_path, "r") as file:
    raw_data = file.read()

barrier_coordinates = [int(x) + int(y) * 1j for line in raw_data.splitlines() for x, y in [line.split(",")]]

def is_within_bounds(coord):
    return 0 <= coord.real <= 70 and 0 <= coord.imag <= 70

#PART1:
def part1(
    start_point=0 + 0j, 
    end_point=70 + 70j, 
    max_obstacles=1024, 
    heuristic=lambda a, b: abs(a - b)
):
    barriers = set(barrier_coordinates[:max_obstacles])
    active_nodes = {start_point}
    travel_cost = {start_point: 0}
    estimated_cost = {start_point: heuristic(start_point, end_point)}

    while active_nodes:
        current_node = min(active_nodes, key=lambda x: estimated_cost[x])
        if current_node == end_point:
            return travel_cost[end_point]

        active_nodes.remove(current_node)

        for neighbor in {current_node + 1, current_node - 1, current_node + 1j, current_node - 1j}:
            if neighbor in barriers or not is_within_bounds(neighbor):
                continue

            tentative_cost = travel_cost[current_node] + 1

            if tentative_cost < travel_cost.get(neighbor, float("inf")):
                travel_cost[neighbor] = tentative_cost
                estimated_cost[neighbor] = tentative_cost + heuristic(neighbor, end_point)
                active_nodes.add(neighbor)

    return False

print("Part 1: ", part1())

#PART2:
def part2():
    low, high = 1024, len(barrier_coordinates)

    while low < high:
        mid = (low + high) // 2
        if part1(max_obstacles=mid):
            low = mid + 1
        else:
            high = mid

    critical_barrier = barrier_coordinates[low - 1]
    return f"{int(critical_barrier.real)},{int(critical_barrier.imag)}"

print("Part 2: ", part2())
