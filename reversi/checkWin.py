def checkWin(board):
    """
    Count all points of two players and check who's win
    """
    countW = 0
    countB = 0
    for i in board:
        countB += i.count('B')
        countW += i.count('W')
    if (countB > countW):
        print('End of the game. W: %d, B: %d' % (countW, countB))
        print('B wins.')
    elif (countB < countW):
        print('End of the game. W: %d, B: %d' % (countW, countB))
        print('W wins.')
    else:
        print('Draw.')
