from sudoku import Sudoku
from fc_sudoku import run_foward_check
import app
import csv
import random

# #Main
# data = []
# solution = []
# with open('sudoku.csv', newline='') as csvFile:
#   reader = csv.reader(csvFile)
#   next(reader)
#   count = 49151
#   while count > 0:
#     chance = random.random()
#     if chance > 0.0:
#       board = next(reader)
#       data.append(board[0])
#       solution.append(board[1])
#       count -= 1
#     else:
#       next(reader)
# boards = []
# for i in range(len(data)):
#   boards.append(Sudoku(data[i], solution[i]))

# #Prints all Boards and their respective Solutions
# for i in range(len(data)):
#   print("Board", i+1)
#   boards[i].printBoard()
#   print()
#   print("Solution")
#   boards[i].printSolution()
#   print()

# #Check Arc Consistency
# for i in boards:
#   print("Before Arc Consistency")
#   i.printBoard()
#   i.checkArc()
#   print("After Arc Consistency")
#   i.printBoard()
#   print("Solution")
#   i.printSolution()
#   print("Is it correct?")
#   i.printCorrect()
#   print()

# #Check MCV
# for i in boards:
#   print("Before MCV")
#   i.printBoard()
#   i.timeMCV()
#   print("After MCV")
#   i.printBoard()
#   print("Solution")
#   i.printSolution()
#   print("Is it correct?")
#   i.printCorrect()
#   print()


# #Testing MCV with a predefined valid board to see how time scales
# #with the number of missing initial values
# before = [6,7,9,5,1,8,2,4,3,
#           5,4,3,7,2,9,6,1,8,
#           8,2,1,6,3,4,9,5,7,
#           7,9,4,3,5,2,1,8,6,
#           3,5,8,4,6,1,7,2,9,
#           2,1,6,8,9,7,5,3,4,
#           4,8,5,2,7,6,3,9,1,
#           9,6,2,1,8,3,4,7,5,
#           1,3,7,9,4,5,8,6,2]
# app.testMCV(before)

# #Runs the sudoku game
# app.runGame(boards)

# #Test custom board input
# work = app.customBoardIn()

#Test custom board input with predefined list
# before = [0,7,0,5,0,8,0,4,3,
#           0,4,0,7,0,9,0,1,8,
#           0,2,0,6,0,4,0,5,7,
#           0,9,0,3,0,2,0,8,6,
#           0,5,0,4,0,1,0,2,9,
#           0,1,0,8,0,7,0,3,4,
#           0,8,0,2,0,6,0,9,1,
#           0,6,0,1,0,3,0,7,5,
#           0,3,0,9,0,5,0,6,2]
# work = app.customBoardAll(before)

#Run tests with arc consistency

# #Only run this if there is no arcresults.txt file
# print("Running tests with arc consistency")
# boardcount = 1
# file = open("arcresults.txt", "w")
# for i in boards:
#   print("Running board " + str(boardcount))
#   boardcount += 1
#   time = i.timeArc()
#   file.write(str(time) + "\n")
# file.close()

#Turn arcresults.txt into a histogram
app.displayHistogram("arcresults.txt")
#jEREMY I swear to god if you don't stop this
