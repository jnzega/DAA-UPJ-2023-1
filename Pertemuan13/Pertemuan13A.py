def bfs(graph, start):
    visited = []
    queue = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    print(visited)

graph = {0 : [7, 9, 11],
         1 : [8, 10],
         2 : [3, 12],
         3 : [2, 4],
         4 : [3],
         5 : [6],
         6 : [7],
         7 : [0, 3, 11],
         8 : [1, 9, 12],
         9 : [0, 8, 10],
         10 : [1, 9],
         11 : [0, 7],
         12 : [2, 8]
         }

bfs(graph, 12)