def initialize_board():
    board = ['[ ]' for _ in range(0, 9)]
    return board



def display_board(board):
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])



def mark_space(board, space_number, player):
    if player == 1:
        board[space_number-1] = '[X]'
    else:
        board[space_number-1] = '[O]'
    return board


def check_win_condition(board):
    pass


def check_space_conflict(board, space_number):
    return board[space_number-1] != '[ ]'
    


def take_turn(board, player):
    space_number = input("Pick an available space.")
    while check_space_conflict(board, space_number):
        space_number = input("Invalid selection. Pick an available space.")
    mark_space(board, space_number, player)
    display_board(board)
    return board
        
        


def play_game():
    board = initialize_board()
    display_board(board)
    while not(check_win_condition(board)):
        

play_game()