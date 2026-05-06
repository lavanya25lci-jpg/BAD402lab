from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Target reached
        if x == target or y == target:
            return path

        # Possible moves
        next_states = [
            (jug1, y),   # Fill jug1
            (x, jug2),   # Fill jug2
            (0, y),      # Empty jug1
            (x, 0),      # Empty jug2

            # Pour jug1 -> jug2
            (x - min(x, jug2 - y),
             y + min(x, jug2 - y)),

            # Pour jug2 -> jug1
            (x + min(y, jug1 - x),
             y - min(y, jug1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None


# Example
jug1 = 4
jug2 = 3
target = 2

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found")
