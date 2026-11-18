# DFS Implementation

def DFS(graph, start, visited=None):

    if visited is None:
        visited = set()

    visited.add(start)

    print(start, end=" ")

    for neighbor in graph[start]:

        if neighbor not in visited:
            DFS(graph, neighbor, visited)


# Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Main Program
print("DFS Traversal:")
DFS(graph, 'A')
