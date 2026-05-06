# AO* Algorithm in Python

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('E', 1)], [('F', 1)]],
    'C': [[('G', 1)]],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Initial heuristic values
H = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0
}

solution = {}

def ao_star(node):
    # If terminal node
    if not graph[node]:
        return H[node]

    min_cost = float('inf')
    best_path = None

    # Check all AND-OR paths
    for path in graph[node]:
        cost = 0

        for child, edge_cost in path:
            cost += edge_cost + ao_star(child)

        if cost < min_cost:
            min_cost = cost
            best_path = path

    H[node] = min_cost
    solution[node] = best_path

    return min_cost


# Run AO*
cost = ao_star('A')

print("Minimum cost:", cost)
print("\nSolution path:")

for node, path in solution.items():
    print(node, "->", path)
