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
    space_number = input("Player " + str(player) + ", pick an available space: ")
    while (str(space_number) not in '123456789' 
           or len(str(space_number)) != 1
            or check_space_conflict(board, (int(space_number)))):
        if str(space_number) not in '123456789' or str(space_number) == '' or len(str(space_number)) != 1:
            space_number = input("Invalid selection. Pick a number from 1 to 9: ")
        elif check_space_conflict(board, (int(space_number))):
            space_number = input("Invalid selection. Pick an available space: ")
    space_number = int(space_number)
    mark_space(board, space_number, player)
    display_board(board)
    return board
        
        


def play_round():
    guide_board = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
    display_board(guide_board)
    board = initialize_board()
    turn = 0
    while True:
        take_turn(board, 1)
        if check_win_condition(board):
            print("Player 1 wins!")
            break
        turn += 1
        if turn == 9:
            print("Tie!")
            break
        take_turn(board, 2)
        if check_win_condition(board):
            print("Player 2 wins!")
            break
        turn += 1
    


def play_game():
    again = True
    while again:
        play_round()
        desire = input("Play another round? (Y/N) ")
        while desire not in "YNyn" or desire == '':
            desire = input("Select valid option. (Y/N) ")
        if desire in 'Nn':
            again = False

play_game()