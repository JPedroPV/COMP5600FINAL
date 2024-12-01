from sudoku import Sudoku
import app
import csv
import random

#Main
data = []
solution = []
with open('sudokuMini.csv', newline='') as csvFile:
  reader = csv.reader(csvFile)
  next(reader)
  count = 1
  while count > 0:
    chance = random.random()
    if chance > 0.0:
      board = next(reader)
      data.append(board[0])
      solution.append(board[1])
      count -= 1
    else:
      next(reader)
boards = []
for i in range(len(data)):
  boards.append(Sudoku(data[i], solution[i]))

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


#Testing MCV on custom set to confirm it works as intended on a board with
#more inital values due to a high running time.
before = [6,7,9,5,1,8,2,4,3,
          5,4,3,7,2,9,6,1,8,
          8,2,1,6,3,4,9,5,7,
          7,9,4,3,5,2,1,8,6,
          3,5,8,4,6,1,7,2,9,
          2,1,6,8,9,7,5,3,4,
          4,8,5,2,7,6,3,9,1,
          9,6,2,1,8,3,4,7,5,
          1,3,7,9,4,5,8,6,2]

afterr = [6,7,9,5,1,8,2,4,3,
          5,4,3,7,2,9,6,1,8,
          8,2,1,6,3,4,9,5,7,
          7,9,4,3,5,2,1,8,6,
          3,5,8,4,6,1,7,2,9,
          2,1,6,8,9,7,5,3,4,
          4,8,5,2,7,6,3,9,1,
          9,6,2,1,8,3,4,7,5,
          1,3,7,9,4,5,8,6,2]

#app.testMCV(before)

# test = Sudoku(before,afterr)
# print("Before")
# test.printBoard()
# print("MCV")
# test.checkMCV()
# print("After MCV")
# test.printBoard()
# print("Is it correct?")
# test.printCorrect()

# #Runs the sudoku game
# app.runGame(boards)

# #Test custom board input
# app.customBoardIn()

#Test custom board input with predefined list
#app.customBoardAll(before)
