def initialize_board():
    board = [' ' for _ in range(0, 9)]
    return board



def display_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])



def mark_space(board, space_number, player):
    pass


def check_win_condition():
    pass


def check_space_conflict():
    pass

def take_turn(board, player):
    space_number = input("Pick an available space.")
    check_space_conflict(board, space_number)


def play_game():
    board = initialize_board()
    display_board(board)

play_game()