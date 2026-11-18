import heapq

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 0
}


# Best First Search
def best_first_search(start, goal):

    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    while priority_queue:

        h, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        print("Visiting:", node)

        # Check goal
        if node == goal:
            print("\nGoal Found!")
            print("Path:", path)
            return

        # Explore neighbors
        for neighbor in graph[node]:

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    print("Goal not found!")


# Main Program
start = 'A'
goal = 'H'

print("Best First Search Traversal:")
best_first_search(start, goal)
