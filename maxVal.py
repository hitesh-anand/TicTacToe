def checkHorizontalMax(board, row, col):
    val = 0

    if col == 0:
        if board[row][col+1] == 'X' and board[row][col+2] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row][col+1] == 'O'):
            count_O+=1
        elif(board[row][col+1] == 'X'):
            count_X+=1
        
        if(board[row][col+2] == 'O'):
            count_O+=1
        elif(board[row][col+2] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif col == 1:
        if board[row][col-1] == 'X' and board[row][col+1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row][col-1] == 'O'):
            count_O+=1
        elif(board[row][col-1] == 'X'):
            count_X+=1
        
        if(board[row][col+1] == 'O'):
            count_O+=1
        elif(board[row][col+1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif col == 2:
        if board[row][col-2] == 'X' and board[row][col-1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row][col-2] == 'O'):
            count_O+=1
        elif(board[row][col-2] == 'X'):
            count_X+=1
        
        if(board[row][col-1] == 'O'):
            count_O+=1
        elif(board[row][col-1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    return val

def checkVerticalMax(board, row, col):
    val = 0

    if row == 0:
        if board[row+1][col] == 'X' and board[row+2][col] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row+1][col] == 'O'):
            count_O+=1
        elif(board[row+1][col] == 'X'):
            count_X+=1
        
        if(board[row+2][col] == 'O'):
            count_O+=1
        elif(board[row+2][col] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 1:
        if board[row-1][col] == 'X' and board[row+1][col] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col] == 'O'):
            count_O+=1
        elif(board[row-1][col] == 'X'):
            count_X+=1
        
        if(board[row-2][col] == 'O'):
            count_O+=1
        elif(board[row-2][col] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 2:
        if board[row-2][col] == 'X' and board[row-1][col] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-2][col] == 'O'):
            count_O+=1
        elif(board[row-2][col] == 'X'):
            count_X+=1
        
        if(board[row-1][col] == 'O'):
            count_O+=1
        elif(board[row-1][col] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    return val


def checkLeftDiagonalMax(board, row, col):
    val = 0

    if row != col:
        return 0

    if row == 0:
        if board[row+1][col+1] == 'X' and board[row+2][col+2] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row+1][col+1] == 'O'):
            count_O+=1
        elif(board[row+1][col+1] == 'X'):
            count_X+=1
        
        if(board[row+2][col+2] == 'O'):
            count_O+=1
        elif(board[row+2][col+2] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 1:
        if board[row-1][col-1] == 'X' and board[row+1][col+1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col-1] == 'O'):
            count_O+=1
        elif(board[row-1][col-1] == 'X'):
            count_X+=1
        
        if(board[row+1][col+1] == 'O'):
            count_O+=1
        elif(board[row+1][col+1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 2:
        if board[row-2][col-2] == 'X' and board[row-1][col-1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-2][col-2] == 'O'):
            count_O+=1
        elif(board[row-2][col-2] == 'X'):
            count_X+=1
        
        if(board[row-1][col-1] == 'O'):
            count_O+=1
        elif(board[row-1][col-1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    return val

def checkRightDiagonalMax(board, row, col):
    val = 0

    if row+col != 2:
        return 0

    if row == 0:
        if board[row+1][col-1] == 'X' and board[row+2][col-2] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row+1][col-1] == 'O'):
            count_O+=1
        elif(board[row+1][col-1] == 'X'):
            count_X+=1
        
        if(board[row+2][col-2] == 'O'):
            count_O+=1
        elif(board[row+2][col-2] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 1:
        if board[row-1][col+1] == 'X' and board[row+1][col-1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col+1] == 'O'):
            count_O+=1
        elif(board[row-1][col+1] == 'X'):
            count_X+=1
        
        if(board[row+1][col+1] == 'O'):
            count_O+=1
        elif(board[row+1][col+1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    elif row == 2:
        if board[row-2][col+2] == 'X' and board[row-1][col+1] == 'X':
            val = 10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-2][col+2] == 'O'):
            count_O+=1
        elif(board[row-2][col+2] == 'X'):
            count_X+=1
        
        if(board[row-1][col+1] == 'O'):
            count_O+=1
        elif(board[row-1][col+1] == 'X'):
            count_X+=1
        
        if count_O == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = 1
        elif count_X == count_O or count_O == 1:
            val = 0
        else:
            val = 2

    return val


def maxVal(board):
    maxVals = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):

            if board[i][j] == 'X' or board[i][j] == 'O':
                maxVals[i][j] = 0
                continue

            val = 0
            num = checkHorizontalMax(board, i, j)
            if num == 10:
                maxVals[i][j] = num
                continue
            val += num
            num = checkVerticalMax(board, i, j)
            if num == 10:
                maxVals[i][j] = num
                continue
            val += num
            num = checkLeftDiagonalMax(board, i, j)
            if num == 10:
                maxVals[i][j] = num
                continue
            val += num
            num = checkRightDiagonalMax(board, i, j)
            if num == 10:
                maxVals[i][j] = num
                continue
            val += num
            maxVals[i][j] = val
    return maxVals

def showBoard(board):
    print('The current state of the board is: ')
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()

# board = [['O', '_', '_'], ['_', '_', '_'],['_','_', '_']]
# showBoard(board)
# maxVals = maxVal(board)
# showBoard(maxVals)