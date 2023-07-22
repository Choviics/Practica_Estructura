graphs = []
vertices = [] 
edges = []

with open("rosalind_bip.txt", "r") as f:
    graph_count = int(f.readline().strip())

    for line in f:
        if line.strip():
            l = list(map(int, line.strip().split(" ")))
            graph[l[0]].append(l[1])
            graph[l[1]].append(l[0])

        else:
            vertice, edge = map(int, f.readline().strip().split(" "))
            graph = {i+1:[] for i in range(vertice)}
            graphs.append(graph)
            vertices.append(vertice)

def dfs_test_bip(graph, v, visited, color):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            color[i] = not color[v]
            if (not dfs_test_bip(graph, i, visited, color)):
                return False
        else:
            if color[v] == color[i]:
                return False
    return True


for i in range(len(graphs)):
    graph = graphs[i]
    vertice = vertices[i]

    visited = [False for i in range(vertice+1)]
    color = [False for i in range(vertice+1)]
    visited[1] = True
    
    if dfs_test_bip(graph, 1, visited, color):
        print(1, end=" ")
    else:
        print(-1, end=" ")
print()