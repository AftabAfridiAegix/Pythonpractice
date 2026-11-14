GRAPH = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node == goal:
            print("Goal Found:", node)
            return
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(graph[node]))

dfs(GRAPH, 'A', 'F')