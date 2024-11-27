from cell import Cell

import numpy as np
import time

class Sudoku:
  board: np.ndarray
  solution: np.ndarray

  #Inititalize Sudoku Board Object
  def __init__(self, initBoard, solved):
    # initBoard = [int(x) for x in list(initBoard)]
    # solved = [int(x) for x in list(solved)]
    initBoard = [Cell(x) for x in list(initBoard)]
    solved = [Cell(x) for x in list(solved)]
    self.board = np.reshape(initBoard, (9,9))
    self.solution = np.reshape(solved, (9,9))

  #Print Sudoku Board
  def printBoard(self):
    for i in range(9):
      if i % 3 == 0 and i != 0:
        print("---------------------")
      for j in range(9):
        if j % 3 == 0 and j != 0:
          print("| ", end="")
        print(self.board[i][j], end=" ")
      print()
    print()

  #Print Sudoku Solution
  def printSolution(self):
    for i in range(9):
      if i % 3 == 0 and i != 0:
        print("---------------------")
      for j in range(9):
        if j % 3 == 0 and j != 0:
          print("| ", end="")
        print(self.solution[i][j], end=" ")
      print()

  #Update Sudoku Cell
  def updateCell(self, row, col, val):
    self.board[row][col] = Cell(val)

  #Check if Sudoku Cell is Valid
  def checkCell(self, row, col):
    val = self.board[row][col].val
    if self.board[row][col].val == 0:
      print("Empty Cell")
      return False
    for i in range(9):
      if self.board[row][i].val == val and i != col:
        print("Row Violation")
        return False
      if self.board[i][col].val == val and i != row:
        print("Column Violation")
        return False
    for i in range(3):
      for j in range(3):
        if self.board[row//3*3+i][col//3*3+j].val == val and i != row and j != col:
          print("Subcell Violation")
          return False
    return True

  #Check if Sudoku Cell is Valid with given Value
  def checkCellVal(self, row, col, val):
    for i in range(9):
      if self.board[row][i].val == val and i != col:
        print("Row Violation for value: " + str(val))
        return False
      if self.board[i][col].val == val and i != row:
        print("Column Violation for value: " + str(val))
        return False
    for i in range(3):
      for j in range(3):
        if self.board[row//3*3+i][col//3*3+j].val == val and i != row and j != col:
          print("Subcell Violation for value: " + str(val))
          return False
    return True

  #Check a cell's possible values given current state of board
  def possNum(self, row, col):
    possible = []
    for i in range(1, 10):
      if self.checkCellVal(row, col, i):
        possible.append(i)
    return possible
  
  def mostConstrained(self):
    #find first unassigned cell
    for i in range(9):
        for j in range(9):
            if not self.board[i][j].assigned:
                mostConstrained = (i, j)
                break
    for i in range(9):
      for j in range(9):
        if len(self.board[i][j].getArcDomain()) > len(self.board[mostConstrained[0]][mostConstrained[1]].getArcDomain()) and not self.board[i][j].assigned:
          mostConstrained = (i, j)
    return mostConstrained
  
  def allAssigned(self):
    for i in range(9):
      for j in range(9):
        if not self.board[i][j].assigned:
          return False
    return True
  
  def enforceArc(self, queue):
    while len(queue) > 0:
      row, col = queue.pop(0)
      val = self.board[row][col].val
      for i in range(9):
        if i != col:
          if self.board[row][i].enforceArc(self.board[row][col]):
            if len(self.board[row][i].getArcDomain()) == 1:
              queue.append((row, i))
        if i != row:
          if self.board[i][col].enforceArc(self.board[row][col]):
            if len(self.board[i][col].getArcDomain()) == 1:
              queue.append((i, col))
      for i in range(3):
        for j in range(3):
          if (row//3)*3+i != row and (col//3)*3+j != col:
            if self.board[(row//3)*3+i][(col//3)*3+j].enforceArc(self.board[row][col]):
              if len(self.board[(row//3)*3+i][(col//3)*3+j].getArcDomain()) == 1:
                queue.append(((row//3)*3+i, (col//3)*3+j))

  def checkArc(self):
    start = time.time()

    # Initial enforce arc consistency
    queue = []
    for i in range(9):
      for j in range(9):
        if self.board[i][j].val != 0:
          queue.append((i,j))

    self.enforceArc(queue)

    while(not self.allAssigned()):
        #find most constrained cell
        mcvI, mcvJ = self.mostConstrained()
        print("Most Constrained Cell: ", mcvI, mcvJ)
        print("Domain: ", self.board[mcvI][mcvJ].getArcDomain())
        print()
    
        #assign value to most constrained cell
        self.board[mcvI][mcvJ].setVal(self.board[mcvI][mcvJ].getArcDomain()[0])
    
        #enforce arc consistency
        self.enforceArc([(mcvI, mcvJ)])
    
    #find most constrained cell
    mcvI, mcJ = self.mostConstrained()
    print("Most Constrained Cell: ", mcvI, mcJ)
    print("Domain: ", self.board[mcvI][mcJ].getArcDomain())

    end = time.time()
    print("Time taken:", end-start)

  def checkForward():
    start = time.time()
    end = time.time()
    print("Time taken:", end-start)

  def checkMinCon():
    start = time.time()
    end = time.time()
    print("Time taken:", end-start)

  def checkMCV(self):
    start = time.time()
    mostX, mostY = self.mostConstrained()
    end = time.time()
    print("Time taken:", end-start)
