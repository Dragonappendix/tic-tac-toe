import src.tic_tac_toe as ttt



def test_board_length():
    board = ttt.initialize_board()
    assert len(board) == 9

def test_space_conflict():
    test_board_length()
    board = ttt.initialize_board()
    ttt.mark_space()


def test_mark_space():
    board = ttt.initialize_board()
    ttt.mark_space(board, 1, player=1)
    assert board == ['[X]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
    ttt.mark_space(board, 3, player=2)
    assert board == ['[X]','[ ]','[O]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
