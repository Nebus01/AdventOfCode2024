from collections import defaultdict, deque

file_path = "Your file path"

with open(file_path, "r") as file:
    content = file.read()
rules_section, updates_section = content.strip().split("\n\n")
    
rules = []
for line in rules_section.strip().split("\n"):
    x, y = map(int, line.split("|"))
    rules.append((x, y))
    
updates = []
for line in updates_section.strip().split("\n"):
    updates.append(list(map(int, line.split(","))))
    

def validate_update(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False
    return True

def find_correct_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        if validate_update(update, rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates

def topological_sort(update, rules):
    subset_set = set(update)
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for x, y in rules:
        if x in subset_set and y in subset_set:
            graph[x].append(y)
            indegree[y] += 1
            if x not in indegree:
                indegree[x] = 0

    queue = deque([node for node in update if indegree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def sum_middle_pages(updates):
    middle_values = [update[len(update) // 2] for update in updates]
    return sum(middle_values)


correct_updates, incorrect_updates = find_correct_updates(rules, updates)

#PART1:
result_part1 = sum_middle_pages(correct_updates)
print("Part 1: ", result_part1)

#PART2: 
corrected_updates = [topological_sort(update, rules) for update in incorrect_updates]
result_part2 = sum_middle_pages(corrected_updates)
print("Part 2: ", result_part2)
