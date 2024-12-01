from sudoku import Sudoku
import random


#Tests the runtime of MCV as values increase
def testMCV(boardIn):
    


#Creates a custom board from user input and checks if
#there is a viable solution using arc consistency
def customBoardIn():
    board = []
    while(len(board) != 81):
        userIn = int(input("Give number 0-9"))
        if userIn in range(0,10):
            board.append(userIn)
        else:
            print("Invalid input")
    return Sudoku(board,board)

def customBoardAll(userIn):
    if len(userIn) == 81:
        board = Sudoku(userIn,userIn)
    else:
        print("Invalid Length")
    board.checkArc()

#Runs Sudoku given a random board from a list of boards
def runGame(gameBoards):
    print("Getting random board")
    num = random.randint(0,len(gameBoards) - 1)
    play = gameBoards[num]
    print("Sudoku Start")
    play.printBoard()
    finished = False
    while not finished:
        inR, inC, inV = -1,-1,-1
        while inR not in range(1,10):
            inR = int(input("Give input for <row> "))
        while inC not in range(1,10):
            inC = int(input("Give input for <column> "))
        while inV not in range(0,10):
            inV = int(input("Give input for <value> "))
        play.board[inR - 1][inC - 1].setVal(inV)
        play.printBoard()
        if play.checkCorrect():
            print("Congratulations")
            finished = True
            break
        cont = -1
        while cont not in range(0,3):
            cont = int(input("Type <0> to continue | <1> to check for errors | <2> to quit and reveal the answer "))
            if cont == 0:
                break
            elif cont == 1:
                play.printCorrect()
            elif cont == 2:
                finished = True
                print("Solution is:")
                play.printSolution()
            else:
                print("Invalid input, Try again.")
        print()
