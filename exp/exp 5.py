from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Check left bank
    if m > 0 and m < c:
        return False

    # Check right bank
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True


def solve():
    # State: (missionaries, cannibals, boat)
    # Boat = 0 means left, 1 means right

    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            print("Solution Found!\n")

            for step in path:
                print("Missionaries:", step[0],
                      "Cannibals:", step[1],
                      "Boat:", "Left" if step[2] == 0 else "Right")

            return

        m, c, boat = state

        for dm, dc in moves:

            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    queue.append((new_state, path))

    print("No solution exists!")


# Main Program
solve()
