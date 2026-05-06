import heapq

# Graph with cost
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 1},
    'E': {'G': 2},
    'F': {'G': 4},
    'G': {}
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 4,
    'G': 0
}

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor, weight in graph[current].items():

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                heapq.heappush(pq, (priority, neighbor))

                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()

    return path, cost[goal]


# Example
path, total_cost = astar('A', 'G')

print("Path:", path)
print("Cost:", total_cost)
