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

graph = {
    'Amin' : ['Wasim', 'Nick', 'Mike'],
    'Wasim' : ['Imran', 'Amin'],
    'Imran' : ['Wasim', 'Faras'],
    'Faras' : ['Imran'],
    'Mike' : ['Amin'],
    'Nick' : ['Amin'],
}

bfs(graph, 'Amin')