import random

class Cell:
  val: int #Actual Value assigned in cell
  domain: list #List of possible values that can be in the cell if not assigned
  arcDomain: list #List of possible values, special for arc consistency
  assigned: bool #Checks if a cell is assigned a value

  already_chosen: list #Checks if the element in the domain has already been assigned (for foward checking)
  assignment: int #Assigns the variable or cell
  

  #Initialize Cell Object
  def __init__(self, val):
    self.val = int(val)

    if self.val == 0:
      self.arcDomain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      self.domain = [1,2,3,4,5,6,7,8,9]
      self.assigned = False

      self.already_chosen = []
      self.assignment

    else:
      self.arcDomain = [self.val]
      self.domain = []
      self.assigned = True

  #Get Cell Value
  def getVal(self):
    return self.val
  
  #Get Cell Domain for arc consistency
  def getArcDomain(self):
    return self.arcDomain
  
  #Get Cell Domain
  def getDomain(self):
    return self.domain
  
  #Set Cell Value
  def setVal(self, val):
    self.val = val
    self.arcDomain = [val]
    self.domain = [val]
    self.assigned = True

  #Reset Cell Domain
  def resetCell(self):
    self.val = 0
    self.arcDomain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.domain = [1,2,3,4,5,6,7,8,9]
    self.assigned = False

  #Enforce Arc Consistency
  #Returns True if a value is removed from the domain
  def enforceArc(self, cell):
    removed = False
    if len(cell.arcDomain) == 1:
      if cell.arcDomain[0] in self.arcDomain:
        self.arcDomain.remove(cell.arcDomain[0])
        removed = True
    return removed
  
  def assign_fc(self):
      i = 0 
      assignment_not_found = True
      while (assignment_not_found):
          if not self.domain:
              raise ValueError("Can't take from an empty domain")
          curr_number = random.choice(self.domain)
      
          if curr_number not in self.already_chosen: 
              self.already_chosen.append(curr_number)
              self.assignment = curr_number
              assignment_not_found = False
              print("Assignment is: ", self.assignment)

          else: 
              assignment_not_found = True
              i+=1
              if (i == len(self.domain)): 
                  print("All Variables have been assigned -- nothing assigned")
                  return None
            
  #String representation, returns value
  def __str__(self):
    return str(self.val)
