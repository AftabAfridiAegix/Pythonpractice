
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

h = {
    'A': 5,
    'B': 3,
    'C': 1,
    'D': 0
}


def gbfs(start, goal):
    queue = [(h[start], start, [start])] #[(5, 'A', ['A'])]
          # the tuple stores (heuristic, node, path)

    while queue:
        queue.sort()
        value, node, path = queue.pop(0)

        if node == goal:
            print(path)
            return

        for neighbor in graph[node]:
            queue.append((h[neighbor], neighbor, path + [neighbor]))

gbfs('A', 'D')
# queue.append((h[neighbor], neighbor, path + [neighbor]))
# First iteration — neighbor is B
# - h['B'] → 3
# - neighbor → 'B'
# - path + [neighbor] → ['A', 'B']
# (3, 'B', ['A', 'B'])