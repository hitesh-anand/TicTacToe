import numpy as np

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    draw = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                draw = 0
                break
    if draw == 1:
        return -1
    b = np.array(board)
    for newBoard in [b, np.transpose(b)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(b)

# board = [['O', 'X', 'O'], ['_', 'X', '_'],['_','O', '_']]
# ch = checkWin(board)

# print('The winner of the game is: ', ch)
