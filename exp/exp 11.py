# Map Coloring using CSP and Backtracking

# Define the map (Graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store assigned colors
color_map = {}


# Check whether color is safe
def is_safe(region, color):

    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False

    return True


# Backtracking function
def map_coloring(regions):

    if not regions:
        return True

    region = regions[0]

    for color in colors:

        if is_safe(region, color):

            color_map[region] = color

            if map_coloring(regions[1:]):
                return True

            # Backtracking
            del color_map[region]

    return False


# Main Program
regions = list(graph.keys())

if map_coloring(regions):

    print("Map Coloring Solution:")

    for region, color in color_map.items():
        print(region, ":", color)

else:
    print("No solution exists!")
