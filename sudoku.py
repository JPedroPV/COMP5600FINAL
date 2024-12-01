from cell import Cell
import numpy as np
import time
import random

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
    for i in range(9):
      for j in range(9):
        if not self.board[i][j].assigned:
          self.fixDomain(i,j)

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

  #Prints what cells are incorrect, if none are tells the user that the board is correct
  def printCorrect(self):
    correct = True
    for i in range(9):
      for j in range(9):
        if self.board[i][j].val != self.solution[i][j].val and self.board[i][j].val != 0:
          print("Incorrect Cell: ", i + 1, j + 1)
          correct = False
    if correct:
        print("Correct Solution")
    else:
        print("Incorrect Solution <------------------------------------")
  
  #Returns True if the board is correct
  def checkCorrect(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j].val != self.solution[i][j].val:
          return False
    return True
  
  #TODO implement this with arc consistency.
  def isValid(self):
    return True

  #Check if Sudoku Cell is Valid
  def checkCell(self, row, col):
    val = self.board[row][col].val
    if self.board[row][col].val == 0:
      #print("Empty Cell")
      return False
    for i in range(9):
      if self.board[row][i].val == val and i != col:
        #print("Row Violation")
        return False
      if self.board[i][col].val == val and i != row:
        #print("Column Violation")
        return False
    for i in range(3):
      for j in range(3):
        if self.board[row//3*3+i][col//3*3+j].val == val and i != row and j != col:
          #print("Subcell Violation")
          return False
    return True

  #Check if Sudoku Cell is Valid with given Value
  def checkCellVal(self, row, col, val):
    for i in range(9):
      if self.board[row][i].val == val and i != col:
        #print("Row Violation for value: " + str(val))
        return False
      if self.board[i][col].val == val and i != row:
        #print("Column Violation for value: " + str(val))
        return False
    for i in range(3):
      for j in range(3):
        if self.board[row//3*3+i][col//3*3+j].val == val and i != row and j != col:
          #print("Subcell Violation for value: " + str(val))
          return False
    return True

  #Fixes the domain of a cell by checking what possible values can be in the domain
  def fixDomain(self, row, col):
    possible = []
    for i in range(1, 10):
      if self.checkCellVal(row, col, i):
        possible.append(i)
    self.board[row][col].domain = possible

  #Fix the specified cell's neighbor's domains
  def fixNeighbors(self, row, col):
    for i in range(9):
        if i != col and not self.board[row][i].assigned:
            self.fixDomain(row, i)
        if i != row and not self.board[i][col].assigned:
            self.fixDomain(i, col)
    for i in range(3):
        for j in range(3):
            if (row//3)*3+i != row and (col//3)*3+j != col and not self.board[(row//3)*3+i][(col//3)*3+j].assigned:
                self.fixDomain((row//3)*3+i, (col//3)*3+j)
  
  #Function to find the most constrained value for arc consistency
  def mostConstrainedArc(self):
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

  #Function to find the most constrained value
  def mostConstrained(self):
  #find first unassigned cell
    for i in range(9):
        for j in range(9):
            if not self.board[i][j].assigned:
                mostConstrained = (i, j)
                break
    for i in range(9):
      for j in range(9):
        if len(self.board[i][j].getDomain()) > len(self.board[mostConstrained[0]][mostConstrained[1]].getDomain()) and not self.board[i][j].assigned:
          mostConstrained = (i, j)
    return mostConstrained
  
  #Checks if all values on the board are assigned
  def allAssigned(self):
    for i in range(9):
      for j in range(9):
        if not self.board[i][j].assigned:
          return False
    return True
  
  #Enforces arc consistency given a queue
  def enforceArc(self, queue):
    while len(queue) > 0:
      row, col = queue.pop(0)
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

  #Check for arc consistency
  def checkArc(self):
    # Initial enforce arc consistency
    queue = []
    for i in range(9):
      for j in range(9):
        if self.board[i][j].val != 0:
          queue.append((i,j))

    self.enforceArc(queue)

    while(not self.allAssigned()):
        #find most constrained cell
        mcvI, mcvJ = self.mostConstrainedArc()
    
        #assign value to most constrained cell
        self.board[mcvI][mcvJ].setVal(self.board[mcvI][mcvJ].getArcDomain()[0])
    
        #enforce arc consistency
        self.enforceArc([(mcvI, mcvJ)])

  #Times arc consistency
  def timeArc(self):
    start = time.time_ns()
    self.checkArc()
    end = time.time_ns()
    t = end - start
    print("Time taken (ns):", t)
    return t

  #Check for forward checking
  def checkForward():
    start = time.time()
    end = time.time()
    print("Time taken:", end-start)

  #Check for min conflicts
  def checkMinCon():
    start = time.time()
    end = time.time()
    print("Time taken:", end-start)

  #Check for most constrained variable
  def checkMCV(self):
    if self.allAssigned():
      if self.checkCorrect():
        return True
      return False
    mostX, mostY = self.mostConstrained()
    queue = self.board[mostX][mostY].getDomain()
    random.shuffle(queue)
    print(queue, mostX, mostY)
    if len(queue) == 0:
      print("EMPTY DOMAIN")
      return False
    while len(queue) > 0:
      val = queue.pop()
      print(val)
      self.board[mostX][mostY].setVal(val)
      self.fixNeighbors(mostX, mostY)
      self.printBoard()
      recu = self.checkMCV()
      if recu == True:
        print("RECURSIVE TRUE")
        if self.allAssigned():
          return True
      else:
        self.board[mostX][mostY].resetCell()
        self.fixDomain(mostX, mostY)
        print("RECURSIVE FALSE")
    return False
  
  #Times most constrained variable
  def timeMCV(self):
    start = time.time_ns()
    self.checkMCV()
    end = time.time_ns()
    t = end - start
    print("Time taken (ns):", t)
    return t
