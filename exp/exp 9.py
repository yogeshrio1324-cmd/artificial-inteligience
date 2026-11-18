from itertools import permutations

# Distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

# Starting city
start = 0

# Generate all possible paths
cities = list(range(n))
cities.remove(start)

min_cost = float('inf')
best_path = None

for path in permutations(cities):

    current_cost = 0
    k = start

    for city in path:
        current_cost += graph[k][city]
        k = city

    # Return to starting city
    current_cost += graph[k][start]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = (start,) + path + (start,)

# Display result
print("Travelling Salesman Problem")
print("Optimal Path:")

for city in best_path:
    print(city, end=" ")

print("\nMinimum Travel Cost:", min_cost)
