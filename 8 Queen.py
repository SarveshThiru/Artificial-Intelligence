def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq(board, col):
    if col >= 8:
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nq(board, col + 1) == True:
                return True

            board[i][col] = 0

    return False

def solve():
    board = [[0 for _ in range(8)] for _ in range(8)]

    if solve_nq(board, 0) == False:
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = " ")
        print()

solve()
