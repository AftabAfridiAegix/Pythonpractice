graph = {
    'A' : [('B', 2), ('C', 2)],
    'B' : [('D', 4)],
    'C' : [('D', 1)],
    'D' :[]
}

def ucs(graph, start, goal):
    queue = [(0, start, [start])]

    while queue:
        queue.sort()
        cost, node, path = queue.pop(0) # (2, 'B', ['A', 'B']) cost, node, path

        if node == goal:
            print(path, cost)
            return

        for neighbor, value in graph[node]:
            new_cost = cost + value
            queue.append((new_cost, neighbor, path + [neighbor]))

ucs(graph, 'A', 'D') 