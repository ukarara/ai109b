board = [-1] * 8


def printboard(result):
    for v in result:
        length = len(result)
        print('□ '*v + '■ ' + '□ '* (length-v-1))
    print('\n')

def is_valid(board, row, col):
    for r in range(row):
        if col == board[r] or abs(row - r) == abs(col - board[r]):
            return False
        continue
    return True

def eightQueen(board, row):
    if row >= len(board):
        printboard(board)
        return True

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            if eightQueen(board, row+1):
                pass
                #return True
    return False

eightQueen(board, 0)