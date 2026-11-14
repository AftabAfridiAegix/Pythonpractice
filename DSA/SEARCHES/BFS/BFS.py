GRAPH = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
    }

def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)

        if node == goal:
            print("Goal Found:", node)
            return

        if node not in visited:
            visited.add(node)
            print(node)
            queue.extend(graph[node])

bfs(GRAPH, 'A', 'F')