from sudoku import Sudoku
import random
import matplotlib.pyplot as plt

#Tests the runtime of MCV as values increase
def testMCV(boardIn):
    times = []
    original = boardIn.copy()
    for j in range(24):
        cop = original.copy()
        for i in range(j):
            cop[i] = 0
        su = Sudoku(cop,original)
        t = su.timeMCV()
        times.append(t)
    for i in range(len(times)): 
        print("Removed " + str(i+1) + " numbers, time is: " + str(times[i]))
    nums = []
    for i in range(len(times)):
        nums.append(i + 1)
    fig, ax = plt.subplots()
    ax = plt.plot(nums,times)
    plt.title("Time (ns) taken for execution")
    plt.xlabel("Number of removed values")
    plt.ylabel("Time (ns)")
    plt.show()

#Displays a histogram for the distribution of the values in given file
def displayHistogram(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split("\n")
    #remove empty entries
    data = [i for i in data if i]
    nums = [(int(i) / 10**9) for i in data]
    plt.hist(nums, bins = 100, log = True)
    plt.title("Distribution of values")
    plt.xlabel("Solving time (s)")
    plt.ylabel("Number of Occurences")
    plt.show()

#Creates a custom board from user input and checks if
#there is a viable solution using arc consistency
def customBoardIn():
    board = []
    while(len(board) != 81):
        try:
            userIn = int(input("Give number 0-9"))
            if userIn in range(0,10):
                board.append(userIn)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
        # This decides whether to let the while end or reset
        if(len(board) == 81):
            #Check if it's a valid board with arc consistency
            protoBoard = Sudoku(board,board)
            if(not protoBoard.isValid()):
                board = []
                print("Invalid board, start over")
    protoBoard.checkArc()
    return Sudoku(board, protoBoard.get1DBoard())

#Returns None if the board is invalid
def customBoardAll(userIn):
    protoBoard = None
    if len(userIn) == 81:
        protoBoard = Sudoku(userIn,userIn)
        if(not protoBoard.isValid()):
            print("Invalid board")
            raise ValueError("Invalid board")
    else:
        raise ValueError("Invalid length")
    protoBoard.checkArc()
    return Sudoku(userIn, protoBoard.get1DBoard())

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
        while cont not in range(0,4):
            cont = int(input("Type <0> to continue | <1> to check for errors | <2> get a hint | <3> to quit and reveal the answer "))
            if cont == 0:
                break
            elif cont == 1:
                play.printCorrect()
            elif cont == 2:
                x,y = play.mostConstrained()
                print("Cell " + str(x+1) + " " + str(y+1) + " has the least possible values.")
            elif cont == 3:
                finished = True
                print("Solution is:")
                play.printSolution()
            else:
                print("Invalid input, Try again.")
        print()
