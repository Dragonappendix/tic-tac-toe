def initialize_board():
    board = [" " for _ in 9]
    return board


def display_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

