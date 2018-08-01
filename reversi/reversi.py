from board import initBoard, drawBoard
from checkWin import checkWin
from drawLine import flip
from validMoves import isOnBoard, isValidMove, getValidMoves
from convert import convertToArray, convertToAbc

if __name__ == "__main__":
    import random
    board = []
    point = []
    count = 0
    initBoard(board)
    while True:
        validMoves = []
        if count % 2 == 0:
            turn = 'B'
        else:
            turn = 'W'
        drawBoard(board)
        getValidMoves(board, turn, validMoves)
        # print(validMoves)
        # checkInvalidMove

        # ////////////
        if validMoves == []:
            point.append(count)
            print("Player %s cannot play." % (turn))
            count += 1
            try:
                # input_user = random.choice(string_valid_moves)
                # input_user = input("Player %s: " % (turn))
                if (point[-1] - point[-2] == 1):
                    checkWin(board)
                    break
            except IndexError:
                pass
            continue
        else:
            # Sort valid moves
            string_valid_moves = [convertToAbc(i) for i in validMoves]
            string_valid_moves.sort()

            print("Valid choices: {}".format(' '.join(string_valid_moves)))
            try:
                input_user = input("Player %s: " % (turn))
                # input_user = random.choice(string_valid_moves)
                while input_user not in [convertToAbc(i) for i in validMoves]:

                    print("{}: Invalid choice".format(input_user))
                    print("Valid choices: {}".format(
                                    ' '.join(string_valid_moves)))
                    # input_user = input("Player %s: " % (turn))
                    input_user = input("Player %s: " % (turn))
                convertToArray(input_user)
                location = convertToArray(input_user)
                tile_to_flip = isValidMove(
                    board, turn, location[0], location[1])
                board[location[0]][location[1]] = turn
                flip(board, tile_to_flip)
                count += 1
            except EOFError:
                raise EOFError("EOF when reading a line")
        # /////////////////////
        # input_user = input("Player %s: " % (turn))
        # # Input not in validMoves
        # while input_user not in [convertToAbc(i) for i in validMoves]:
        #     input_user = input("Player %s: " % (turn))
        #
