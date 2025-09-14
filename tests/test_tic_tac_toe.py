import src.tic_tac_toe as ttt



def test_board_length():
    board = ttt.initialize_board()
    assert len(board) == 9

def test_space_conflict():
    board = ttt.initialize_board()
    board = ttt.mark_space(board, 1, 1)
    board = ttt.mark_space(board, 3, 2)
    assert(ttt.check_space_conflict(board, 1))
    assert(ttt.check_space_conflict(board, 3))
    assert(not(ttt.check_space_conflict(board, 7)))
    assert(not(ttt.check_space_conflict(board, 2)))


def test_mark_space():
    board = ttt.initialize_board()
    board = ttt.mark_space(board, 1, 1)
    assert board == ['[X]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
    board = ttt.mark_space(board, 3, 2)
    assert board == ['[X]','[ ]','[O]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']



def test_win_condition():
    board = ['[X]','[ ]','[ ]','[X]','[ ]','[ ]','[O]','[ ]','[ ]']
    assert not(ttt.check_win_condition(board))
    board = ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
    assert not(ttt.check_win_condition(board))
    board = ['[X]','[X]','[X]','[X]','[ ]','[X]','[O]','[ ]','[O]']
    assert ttt.check_win_condition(board)
    board = ['[O]','[ ]','[ ]','[O]','[ ]','[ ]','[O]','[ ]','[ ]']
    assert ttt.check_win_condition(board)
    board = ['[ ]','[X]','[ ]','[ ]','[X]','[ ]','[ ]','[X]','[ ]']
    assert ttt.check_win_condition(board)
    board = ['[ ]','[ ]','[O]','[X]','[O]','[ ]','[O]','[ ]','[ ]']
    assert ttt.check_win_condition(board)
    board = ['[X]','[ ]','[ ]','[ ]','[ ]','[ ]','[O]','[ ]','[ ]']
    assert not(ttt.check_win_condition(board))
    board = ['[X]','[ ]','[ ]','[X]','[ ]','[ ]','[ ]','[ ]','[ ]']
    assert not(ttt.check_win_condition(board))
