import copy


def initBoard(board):
    """
    Initialize a board
    """
    for i in range(0, 8):
        board.append([])
        for j in range(0, 8):
            board[i].append('.')
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'


def drawBoard(board):
    """
    Show board to terminal
    """
    tmp = copy.deepcopy(board)
    tmp1 = []
    alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    tmp.insert(0, alpha)
    numb = 1
    for i in tmp:
        if numb == 1:
            numb += 1
            continue
        else:
            i.insert(0, numb-1)
        numb += 1
    for i in tmp:
        print(' '.join([str(j) for j in i]))
