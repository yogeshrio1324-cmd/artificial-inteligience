# Minimax Algorithm for Tic Tac Toe

board = [' ' for i in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(board[i*3], '|', board[i*3+1], '|', board[i*3+2])
        if i < 2:
            print('--+---+--')
    print()


# Check winner
def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Minimax Algorithm
def minimax(is_max):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if ' ' not in board:
        return 0

    if is_max:
        best_score = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score


# Find best move for computer
def best_move():

    best_score = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


# Main Game
def play_game():

    print("TIC TAC TOE - MINIMAX")
    print("You are X and Computer is O")

    while True:

        print_board()

        # Human move
        try:
            move = int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Enter a valid number!")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = 'X'

        if check_winner('X'):
            print_board()
            print("You Win!")
            break

        if ' ' not in board:
            print_board()
            print("Game Draw!")
            break

        # Computer move
        print("Computer is thinking...")
        move = best_move()
        board[move] = 'O'

        if check_winner('O'):
            print_board()
            print("Computer Wins!")
            break

        if ' ' not in board:
            print_board()
            print("Game Draw!")
            break


# Start game
play_game()
