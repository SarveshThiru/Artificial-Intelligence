# Tic-Tac-Toe Minimax Algorithm

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while not game_over(board):
        print_board(board)
        player_row = int(input("Enter the row (0, 1, or 2): "))
        player_col = int(input("Enter the column (0, 1, or 2): "))

        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue

        if not game_over(board):
            print("Computer's turn...")
            computer_row, computer_col = find_best_move(board)
            board[computer_row][computer_col] = 'O'

    print_board(board)

    if is_winner(board, 'X'):
        print("Congratulations! You win!")
    elif is_winner(board, 'O'):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
