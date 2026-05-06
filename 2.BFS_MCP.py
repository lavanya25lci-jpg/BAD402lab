from collections import deque

# Check whether a state is valid
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Left side condition
    if m > 0 and m < c:
        return False

    # Right side condition
    mr = 3 - m
    cr = 3 - c

    if mr > 0 and mr < cr:
        return False

    return True


# BFS for Missionaries and Cannibals Problem
def bfs():
    start = (3, 3, 1)   # all on left side
    goal = (0, 0, 0)    # all on right side

    queue = deque([(start, [start])])
    visited = set()

    # Possible boat moves
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        m, c, boat = state

        for dm, dc in moves:

            # Boat moving from left to right
            if boat == 1:
                new_state = (m-dm, c-dc, 0)

            # Boat moving from right to left
            else:
                new_state = (m+dm, c+dc, 1)

            nm, nc, nb = new_state

            if is_valid(nm, nc) and new_state not in visited:
                queue.append((new_state, path + [new_state]))

    return None


# Run BFS
solution = bfs()

if solution:
    print("Solution found:\n")
    for step in solution:
        print(step)
else:
    print("No solution found")
