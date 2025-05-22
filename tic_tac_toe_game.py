# A simple two-player Tic Tac Toe game in Python
# Written by Erik Lepesov for University of Aberdeen task and to demonstrate basic programming concepts

def print_board(board):
    # Prints the current state of the board in a readable format
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check all win conditions: rows, columns, and both diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is completely filled (tie condition)
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    # Welcome message
    print("Welcome to Tic Tac Toe!")
    print("This is a simple 2-player game.")
    print("Player X goes first. To make a move, enter the row and column number (0, 1, or 2).")

    # Set up an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        # Ask the current player for their move
        move = input(f"Player {current_player}, what is your move? (row and column separated by space): ")
        try:
            row, col = map(int, move.strip().split())
            if row not in range(3) or col not in range(3):
                print("Oops! Row and column must be 0, 1, or 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken. Try a different one!")
                continue
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Congrats! Player {current_player} wins!")
            break

        # Check for tie
        if is_full(board):
            print_board(board)
            print("It's a tie! Well played both.")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
