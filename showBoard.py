def showBoard(board):
    print('The current state of the board is: ')
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()


# board = [['X', 'O', '_'], ['O', 'X', '_'],['O','_', 'X']]
# showBoard(board)