def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph = {
    'Amin' : ['Wasim', 'Nick', 'Mike'],
    'Wasim' : ['Imran', 'Amin'],
    'Imran' : ['Wasim', 'Faras'],
    'Faras' : ['Imran'],
    'Mike' : ['Amin'],
    'Nick' : ['Amin'],
}
visited = set()
dfs(visited, graph, 'Amin')