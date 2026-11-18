# Alpha-Beta Pruning Algorithm

def alphabeta(depth, node, is_max, values,
              alpha, beta, max_depth):

    # Leaf node
    if depth == max_depth:
        return values[node]

    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha pruning
            if beta <= alpha:
                break

        return best


# Main Program

values = [3, 5, 6, 9, 1, 2, 0, -1]

max_depth = 3

result = alphabeta(
    0,
    0,
    True,
    values,
    float('-inf'),
    float('inf'),
    max_depth
)

print("Optimal Value:", result)
