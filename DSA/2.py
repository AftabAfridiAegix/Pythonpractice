import heapq

def heuristic(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = blank // 3, blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new = list(state)
            idx = r * 3 + c
            new[blank], new[idx] = new[idx], new[blank]
            neighbors.append(tuple(new))

    return neighbors

def gbfs(start, goal):
    queue = [(heuristic(start, goal), start, [start])]
    visited = set()

    while queue:
        h, state, path = heapq.heappop(queue)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(queue, (
                    heuristic(neighbor, goal),
                    neighbor,
                    path + [neighbor]
                ))
    return None
def print_grid(state):
    for i in range(0, 9, 3):
        print(*['_' if x == 0 else x for x in state[i:i+3]])
    print()
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
path = gbfs(start, goal)
if path:
    for step, state in enumerate(path):
        print("Step:", step)
        print("Heuristic:", heuristic(state, goal))
        print_grid(state)

    print("Total steps:", len(path) - 1)
else:
    print("No solution found.")
