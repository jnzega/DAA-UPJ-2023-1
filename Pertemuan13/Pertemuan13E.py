def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

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

visited = set()
dfs(visited, graph, 0)