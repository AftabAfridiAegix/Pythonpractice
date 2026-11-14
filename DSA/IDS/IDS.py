graph = {
    'A' :['B', 'C'],
    'B' :['D', 'E'],
    'C' :['F', 'G'],
    'D' :[],
    'E' :[],
    'F' :[],
    'G' :[]

}

def dls(node, limit):
    print(node)
    if limit == 0:
        return

    for neighbor in graph[node]:
       dls(neighbor, limit - 1)
      
          
def ids(start):
    for limit in range(3):
        dls(start, limit)
        print()
ids('A')
