def isOnBoard(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7


def isValidMove(board, tile, xstart, ystart):
    """
    Returns False if the player's move on space xstart, ystart is invalid
    If it is a valid move, returns a list of spaces that would become
    the player's if they made a move here
    """
    if board[xstart][ystart] != '.' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile
    # Assign B and W
    if tile == 'B':
        otherTile = 'W'
    else:
        otherTile = 'B'
    tilesToFlip = []
    direction = [
                [0, 1], [1, 1], [1, 0], [1, -1],
                [0, -1], [-1, -1], [-1, 0], [-1, 1]
                ]
    for xdirection, ydirection in direction:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
        else:
            continue
    board[xstart][ystart] = '.'
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def getValidMoves(board, tile, validMoves):
    """
    Returns a list of [x,y] lists of valid moves for the given player on the
    given board.
    """
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y):
                validMoves.append([x, y])
