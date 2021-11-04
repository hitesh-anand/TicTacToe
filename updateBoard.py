def updateBoard(board, pos, ch):
    if board[pos[0]][pos[1]] != '_':
        print('The current position is already filled! Please enter a valid position')
        return 0, board
    board[pos[0]][pos[1]] = ch
    return 1, board