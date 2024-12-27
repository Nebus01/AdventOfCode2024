from collections import defaultdict

file_path = "Your file path"

with open(file_path, "r") as f:
    connections = [line.strip().split('-') for line in f]


def build_graph(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors & graph[neighbor]
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)
    return triangles

def filter_triangles(triangles):
    return [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

def find_largest_clique(graph):

    nodes = list(graph.keys())
    max_clique = []

    def dfs(clique, candidates):
        nonlocal max_clique
        if not candidates:
            if len(clique) > len(max_clique):
                max_clique = clique
            return
        while candidates:
            n = candidates.pop()
            new_candidates = candidates & graph[n]
            dfs(clique + [n], new_candidates)

    dfs([], set(nodes))
    return max_clique

#PART1:
graph = build_graph(connections)
triangles = find_triangles(graph)
filtered_triangles = filter_triangles(triangles)
print("Part 1: ", len(filtered_triangles))

#PART2:
largest_clique = find_largest_clique(graph)
password = ",".join(sorted(largest_clique))
print("Part 2: ", password)
