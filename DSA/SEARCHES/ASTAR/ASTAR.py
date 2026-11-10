graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 2)],
    'D': []
}

h = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 0
}


def astar(start, goal):
    queue = [(h[start], 0, start, [start])]

    while queue:
        queue.sort()
        f, cost, node, path = queue.pop(0)

        if node == goal:
            print(path, cost)
            return
        for neighbor, value in graph[node]:
          new_cost = cost + value
          new_f = new_cost + h[neighbor]

          queue.append((new_f, new_cost, neighbor, path + [neighbor]))

astar('A', 'D')