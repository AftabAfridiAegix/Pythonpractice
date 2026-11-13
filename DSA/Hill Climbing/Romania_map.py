
ROMANIA_MAP = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti']
}

h = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Fagaras': 176,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374
}


def hill_climbing(start, goal, heuristic):
    current = start
    path = [current]

    print("\nStarting:", current, "h =", heuristic[current])
    while current != goal:
        neighbors = ROMANIA_MAP[current]

        best = min(neighbors, key=lambda x: heuristic[x])

        print("\nCurrent:", current, "h =", heuristic[current])
        print("Neighbors:", [(city, heuristic[city]) for city in neighbors])
        print("Selected:", best, "h =", heuristic[best])

        if heuristic[best] >= heuristic[current]:
            print("Local Minimum reached! Get stucked")
            break

        current = best
        path.append(current)
    if current == goal:
        print("Goal Reached!")
    print("Final Path:", " -> ".join(path))

print("\nScenario First")
hill_climbing('Arad', 'Bucharest', h)

print("\nScenario Second")
hill_climbing('Timisoara', 'Bucharest', h)

# Modified heuristic
print("\nScenario Third")
h2 = h.copy()
h2['Sibiu'] = 395

hill_climbing('Arad', 'Bucharest', h2)
