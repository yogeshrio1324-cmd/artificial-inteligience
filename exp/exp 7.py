# BFS Implementation

from collections import deque

def BFS(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:")

    while queue:

        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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
BFS(graph, 'A')
