from bestMove import bestMove
from minVal import minVal, showBoard
from maxVal import maxVal
from showBoard import showBoard
from createBoard import createBoard
from updateBoard import updateBoard
from finished import checkWin, checkDiagonals, checkRows
import random

def showRules():
    print('''
    1. The cells are 0-indexed. So, choose the coordinates of your cell accordingly. For example, the top-left cell is (0,0),
    the two cells to its right are (0,1), and (0,2) respectively.
    Similarly, the right-most cell is (2,2).
    2. Note that the user(you) can choose only 'O' and the computer will always play with 'X'.
    3. At the start of the game, you will be asked whether you want to move first or the computer should move first. If you want to play the first move, type O(capital letter O).
    Else, type capital X.
    4. Each time your turn comes, you will have to provide first the x-coordinate(between 0 to 2 corresponding to each of the three rows). Similarly, you
    would have to provide a y-coordinate too(a number between 0 to 2 corresponding to each column).
    5. You will not have to wait for the computer's turn. It will move automatically and the resultant board will be shown to you later on before your
    next move.
    
    Hope you enjoy the game!
    ''')




def play():
    showRules()
    board = createBoard()
    showBoard(board)
    print('Who will take the first go? ( Type X or O)')
    ch = input()
    while not(ch == 'X' or ch == 'O'):
        print('Please enter a valid character! Try again...')
        ch = input()
    start = 1
    while(True):
        print(ch,"'s chance...")
        if(ch == 'O'):
            if start == 1:
                start = 0
            print('Enter the x-coordinate of the cell where you wish to move: ')
            x = int(input())
            print('Enter the y-coordinate of the cell where you wish to move: ')
            y = int(input())
            pos = [x,y]
            print('Marking a "O" at (',x," , ",y,")")
            ret, board = updateBoard(board, pos, ch)
            while(ret == 0):
                print('Enter the x-coordinate of the cell where you wish to move: ')
                x = int(input())
                print('Enter the y-coordinate of the cell where you wish to move: ')
                y = int(input())
                pos = [x,y]
                print('Marking a "O" at (',x," , ",y,")")
                ret, board = updateBoard(board, pos , ch)
            ch = 'X'
        elif(ch == 'X'):
            if start == 1:
                x = random.randint(0,2)
                y = random.randint(0,2)
                pos = [x,y]
                start = 0
            else:
                pos = bestMove(minVal(board), maxVal(board))
            print('Marking a "X" at (',pos[0]," , ",pos[1],")")
            ret, board = updateBoard(board, pos, ch)
            ch = 'O'

        showBoard(board)
        print()
        c = checkWin(board)
        if checkWin(board) != 0 and checkWin(board) != '_':
            # ch = checkWinner(board)
            if c == 'X':
                print('You lost! Better Luck Next time :(')
            elif c == 'O':
                print('Congrats! You won :)')
            elif c == -1:
                print('Match draw! Nice game, right?')
            break
    print()
    print('Want to play one more time? (Y/N)')
    c = input()
    if c=='Y':
        print()
        play()
    else:
        print('No problem! Hope you had a nice time. See ya later!')
        return
        
play()