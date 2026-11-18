import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def solve(start):
    pq = []

    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            print("Solution Found!")
            print("Number of moves:", g)

            for step in path:
                print("\n")
                for i in range(0, 9, 3):
                    print(step[i:i+3])

            return

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No solution exists!")


# Main Program
start = tuple(map(int, input(
    "Enter the initial state (use 0 for blank): "
).split()))

if len(start) == 9 and set(start) == set(range(9)):
    solve(start)
else:
    print("Invalid input! Enter numbers from 0 to 8.")
