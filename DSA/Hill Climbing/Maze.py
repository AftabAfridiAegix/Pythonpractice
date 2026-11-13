
MAZE = {
    'A': ['F'],
    'B': ['G', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D'],
    'F': ['A', 'H'],
    'G': ['B', 'J'],
    'H': ['F', 'I', 'M'],
    'I': ['H', 'J', 'N'],
    'J': ['I', 'G'],
    'K': ['L', 'P'],
    'L': ['K', 'Q'],
    'M': ['H', 'N', 'R'],
    'N': ['M', 'I', 'S'],
    'O': ['P', 'U'],
    'P': ['O', 'K', 'Q'],
    'Q': ['P', 'L', 'V'],
    'R': ['M', 'S'],
    'S': ['R', 'N', 'T'],
    'T': ['S', 'U', 'W'],
    'U': ['T', 'O'],
    'V': ['Q', 'Y'],
    'W': ['T'],
    'X': ['Y'],
    'Y': ['V', 'X']
}

coordinates = {
    'A': (0,0), 'B': (2,0), 'C': (3,0),
    'D': (4,0), 'E': (5,0), 'F': (0,1),
    'G': (2,1), 'H': (0,2), 'I': (1,2),
    'J': (2,2), 'K': (4,2), 'L': (5,2),
    'M': (0,3), 'N': (1,3), 'O': (3,3),
    'P': (4,3), 'Q': (5,3), 'R': (0,4),
    'S': (1,4), 'T': (2,4), 'U': (3,4),
    'V': (5,4), 'W': (2,5), 'X': (4,5),
    'Y': (5,5)
}

def heuristic(node):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates['Y']
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def hill_climbing(start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = MAZE[current]
        best = min(neighbors, key=heuristic)

        print("\nCurrent:", current, "h =", round(heuristic(current), 2))
        print("Neighbors:", [(n, round(heuristic(n), 2)) for n in neighbors])
        print("Selected:", best, "h =", round(heuristic(best), 2))

        if heuristic(best) >= heuristic(current):
            print("Local Minimum Reached!")
            break

        current = best
        path.append(current)

    if current == goal:
        print("Goal Reached!")
    print("Final Path:", " -> ".join(path))

    if current == 'Y':
      print("Goal Reached!")
    else:
      print("Goal Not Reached! Goal is y")

hill_climbing('A', 'Y')
