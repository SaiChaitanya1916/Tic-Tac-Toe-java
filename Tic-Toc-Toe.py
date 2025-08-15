def print_board(board):
    print("  0   1   2")
    for row in range(3):
        print(row, end=" ")
        for col in range(3):
            print(board[row][col], end="")
            if col < 2:
                print(" | ", end="")
        print()
        if row < 2:
            print("  ---------")
    print()

def have_won(board, player):
    # Check rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] == ' ':
            board[row][col] = player

            if have_won(board, player):
                print_board(board)
                print(f"Player {player} has won!")
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("Cell already taken. Try again!")

if __name__ == "__main__":
    main()
