import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_max):
    if check_winner(board, "O"): return 1
    if check_winner(board, "X"): return -1
    if is_full(board): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main game
board = [[" "]*3 for _ in range(3)]
while True:
    print_board(board)
    row = int(input("Enter your move row (0-2): "))
    col = int(input("Enter your move col (0-2): "))
    if board[row][col] != " ":
        print("Invalid move, try again.")
        continue
    board[row][col] = "X"
    if check_winner(board, "X"):
        print_board(board)
        print("You win!")
        break
    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break
    ai_row, ai_col = best_move(board)
    board[ai_row][ai_col] = "O"
    if check_winner(board, "O"):
        print_board(board)
        print("AI wins!")
        break
    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break
