from sudoku import Sudoku

import csv
import random

#Main
data = []
solution = []
with open('sudokuMini.csv', newline='') as csvFile:
  reader = csv.reader(csvFile)
  next(reader)
  count = 10
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

# for i in range(len(data)):
#   print("Board", i+1)
#   boards[i].printBoard()
#   print()
#   print("Solution")
#   boards[i].printSolution()
#   print()

# #checkCell() testing
# help = boards[1]
# help.printBoard()
# print(help.checkCell(0, 0))
# print()
# help.updateCell(0, 0, 0)
# help.printBoard()
# print(help.checkCell(0, 0))
# print()
# help.updateCell(0, 0, 1)
# help.printBoard()
# print(help.checkCell(0, 0))
# print()
# help.updateCell(2, 5, 6)
# help.printBoard()
# print(help.checkCell(2, 5))
# print()
# help.updateCell(6, 1, 7)
# help.printBoard()
# print(help.checkCell(6, 1))
# print()

# #checkCellVal testing
# help = boards[1]
# help.printBoard()
# print(help.possNum(3, 4))
# print()

win = boards[3]
win.printBoard()
win.checkArc()
win.printBoard()
