def flip(board, tileToLip):
    """
    Reverse all tiles in a list
    """
    for i in tileToLip:
        if (board[i[0]][i[1]] == 'B'):
            board[i[0]][i[1]] = 'W'
        elif (board[i[0]][i[1]] == 'W'):
            board[i[0]][i[1]] = 'B'
