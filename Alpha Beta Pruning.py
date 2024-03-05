# Constants for representing players and empty cells
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

def print_board(board):
    for row in board:
        print(" ".join(map(lambda cell: "X" if cell == PLAYER_X else ("O" if cell == PLAYER_O else "-"), row)))
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def game_over(board):
    # Check if the game is over (someone wins or the board is full)
    return is_winner(board, PLAYER_X) or is_winner(board, PLAYER_O) or is_full(board)

def evaluate(board):
    # Evaluate the board for the minimax algorithm
    if is_winner(board, PLAYER_X):
        return -1
    elif is_winner(board, PLAYER_O):
        return 1
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 3, float('-inf'), float('inf'), False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage
if __name__ == "__main__":
    initial_board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    print("Initial board:")
    print_board(initial_board)

    while not game_over(initial_board):
        player_x_row, player_x_col = map(int, input("Enter your move (row and column): ").split())
        if initial_board[player_x_row][player_x_col] != EMPTY:
            print("Invalid move. Cell is already taken. Try again.")
            continue

        initial_board[player_x_row][player_x_col] = PLAYER_X

        if game_over(initial_board):
            break

        print("Updated board after your move:")
        print_board(initial_board)

        print("Computer's move:")
        player_o_row, player_o_col = find_best_move(initial_board)
        initial_board[player_o_row][player_o_col] = PLAYER_O

        print_board(initial_board)

    if is_winner(initial_board, PLAYER_X):
        print("You win!")
    elif is_winner(initial_board, PLAYER_O):
        print("Computer wins!")
    else:
        print("It's a draw!")
