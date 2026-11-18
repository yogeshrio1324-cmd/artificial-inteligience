# Tic Tac Toe Game

board = [' ' for i in range(9)]

# Display the board
def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()


# Check winner
def check_winner(player):

    win_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Main game
def tic_tac_toe():

    player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Enter positions from 1 to 9")

    while True:

        print_board()

        try:
            position = int(input(
                "Player " + player + ", enter position (1-9): "
            )) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if position < 0 or position > 8 or board[position] != ' ':
            print("Invalid position! Try again.")
            continue

        board[position] = player

        # Check winner
        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            break

        # Check draw
        if ' ' not in board:
            print_board()
            print("Game Draw!")
            break

        # Switch player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


# Start the game
tic_tac_toe()
