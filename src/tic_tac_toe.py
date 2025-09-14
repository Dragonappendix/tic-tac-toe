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

win_conditions = [[0, 3, 6], [0, 4, 8], [0, 1, 2], [1, 4, 7], 
                    [2, 5, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6]]

def check_win_condition(board):
    for win_condition in win_conditions:
        if (board[win_condition[0]] == board[win_condition[1]] == board[win_condition[2]] == '[X]' 
        or board[win_condition[0]] == board[win_condition[1]] == board[win_condition[2]] == '[O]'):
            return True



def check_space_conflict(board, space_number):
    return board[space_number-1] != '[ ]'
    


def take_turn(board, player):
    space_number = input("Pick an available space.")
    while str(space_number) not in '123456789':
        space_number = input("")
    while check_space_conflict(board, space_number):
        space_number = input("Invalid selection. Pick an available space.")
    mark_space(board, space_number, player)
    display_board(board)
    return board
        
        


def play_round():
    board = initialize_board()
    display_board(board)
    while True:
        take_turn(board, 1)
        if check_win_condition(board):
            print("Player 1 wins!")
            break
        take_turn(board, 2)
        if check_win_condition(board):
            print("Player 2 wins!")
            break
    


def play_game():
    again = True
    while again:
        play_round()
        if input("Play another round? (Y/N)") == 'N':
            break

play_game()