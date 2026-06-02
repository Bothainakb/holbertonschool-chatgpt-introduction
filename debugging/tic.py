#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)


def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(
                "Enter row (0, 1, or 2) for player " + player + ": "
            ))
            col = int(input(
                "Enter column (0, 1, or 2) for player " + player + ": "
            ))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid coordinates. Use 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe()
