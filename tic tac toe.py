import random

# Display the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check if there's a winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

# Check if board is full
def is_full(board):
    return all(space != " " for space in board)

# Player move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in range(9) and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Computer move (random choice)
def computer_move(board):
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(empty_positions)
    board[move] = "O"
    print(f"Computer chooses position {move + 1}")

# Main game loop
def tic_tac_toe():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        player_move(board)
        display_board(board)
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        computer_move(board)
        display_board(board)
        if check_winner(board, "O"):
            print("💻 Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
