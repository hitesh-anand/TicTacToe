def checkHorizontalMin(board, row, col):
    val = 0

    if col == 0:
        if board[row][col+1] == 'O' and board[row][col+2] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    elif col == 1:
        if board[row][col-1] == 'O' and board[row][col+1] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    else:
        if board[row][col-1] == 'O' and board[row][col-2] == 'O':
            val = -10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row][col-1] == 'O'):
            count_O+=1
        elif(board[row][col-1] == 'X'):
            count_X+=1
        
        if(board[row][col-2] == 'O'):
            count_O+=1
        elif(board[row][col-2] == 'X'):
            count_X+=1
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    return val

def checkVerticalMin(board, row, col):
    val = 0

    if row == 0:
        if board[row+1][col] == 'O' and board[row+2][col] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    elif row == 1:
        if board[row-1][col] == 'O' and board[row+1][col] == 'O':
            val = -10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col] == 'O'):
            count_O+=1
        elif(board[row-1][col] == 'X'):
            count_X+=1
        
        if(board[row+1][col] == 'O'):
            count_O+=1
        elif(board[row+1][col] == 'X'):
            count_X+=1
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    else:
        if board[row-1][col] == 'O' and board[row-2][col] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    return val

def checkLeftDiagonalMin(board, row, col):
    val = 0

    if row!=col :
        return 0

    if row == 0:
        if board[row+1][col+1] == 'O' and board[row+2][col+2] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    elif col == 1:
        if board[row-1][col-1] == 'O' and board[row+1][col+1] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    else:
        if board[row-1][col-1] == 'O' and board[row-2][col-2] == 'O':
            val = -10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col-1] == 'O'):
            count_O+=1
        elif(board[row-1][col-1] == 'X'):
            count_X+=1
        
        if(board[row-2][col-2] == 'O'):
            count_O+=1
        elif(board[row-2][col-2] == 'X'):
            count_X+=1
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    return val    


def checkRightDiagonalMin(board, row, col):
    val = 0

    if row + col != 2:
        return 0

    if row == 0:
        if board[row+1][col-1] == 'O' and board[row+2][col-2] == 'O':
            val = -10
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
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    elif col == 1:
        if board[row-1][col+1] == 'O' and board[row+1][col-1] == 'O':
            val = -10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col+1] == 'O'):
            count_O+=1
        elif(board[row-1][col+1] == 'X'):
            count_X+=1
        
        if(board[row+1][col-1] == 'O'):
            count_O+=1
        elif(board[row+1][col-1] == 'X'):
            count_X+=1
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    else:
        if board[row-1][col+1] == 'O' and board[row-2][col+2] == 'O':
            val = -10
            return val
        
        count_X = 0
        count_O = 0

        if(board[row-1][col+1] == 'O'):
            count_O+=1
        elif(board[row-1][col+1] == 'X'):
            count_X+=1
        
        if(board[row-2][col+2] == 'O'):
            count_O+=1
        elif(board[row-2][col+2] == 'X'):
            count_X+=1
        
        if count_X == 2:
            val = 0
        elif count_X == 0 and count_O == 0:
            val = -1
        elif count_X == count_O or count_X == 1:
            val = 0
        else:
            val = -2

    return val


def minVal(board):
    minVals = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):

            if board[i][j] == 'X' or board[i][j] == 'O':
                minVals[i][j] = 0
                continue

            val = 0
            num = checkHorizontalMin(board, i, j)
            if num == -10:
                minVals[i][j] = num
                continue
            val += num
            num = checkVerticalMin(board, i, j)
            if num == -10:
                minVals[i][j] = num
                continue
            val += num
            num = checkLeftDiagonalMin(board, i, j)
            if num == -10:
                minVals[i][j] = num
                continue
            val += num
            num = checkRightDiagonalMin(board, i, j)
            if num == -10:
                minVals[i][j] = num
                continue
            val += num
            minVals[i][j] = val
    return minVals


def showBoard(board):
    print('The current state of the board is: ')
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()

# board = [['O', '_', 'O'], ['_', 'X', '_'],['_','_', 'O']]
# showBoard(board)
# minVals = minVal(board)
# showBoard(minVals)