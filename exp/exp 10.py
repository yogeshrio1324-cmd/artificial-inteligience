# A* Algorithm Implementation

def a_star(graph, heuristic, start, goal):

    open_list = [start]
    closed_list = set()

    g = {start: 0}
    parent = {}

    while open_list:

        current = min(
            open_list,
            key=lambda node: g[node] + heuristic[node]
        )

        if current == goal:

            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            print("Shortest Path:", path)
            print("Total Cost:", g[goal])
            return

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current].items():

            if neighbor in closed_list:
                continue

            new_cost = g[current] + cost

            if neighbor not in g or new_cost < g[neighbor]:

                g[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    print("Path not found!")


# Graph Representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Heuristic Values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

# Main Program
start = 'A'
goal = 'E'

a_star(graph, heuristic, start, goal)
