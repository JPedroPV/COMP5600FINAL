import random 
from cell import Cell
from sudoku import Sudoku

class Var:
    def __init__(self, domain):
        """
        Initializes the DomainAssignment class.

        :param assignment: An integer value for the assignment.
        :param domain: A list of values representing the domain.
        """
        self.assignment = domain[0] # Integer assignment
        self.domain = domain if domain is not None else []
        self.already_chosen = []
        self.assigned = False

    def assign(self):
        assignment_not_found = True
        i = 0
        while (assignment_not_found):
            if not self.domain:
                raise ValueError("Can't take from an empty domain")
            curr_number = random.choice(self.domain)
        
            if curr_number not in self.already_chosen: 
                self.already_chosen.append(curr_number)
                self.assignment = curr_number
                self.assigned = True
                assignment_not_found = False
                print("Assignment is: ", self.assignment)

            else: 
                assignment_not_found = True
                i+=1
                if (i == len(self.domain)): 
                    print("All Variables have been assigned -- nothing assigned")
                    return None
            
x1 = Var([1,2,3])
x2 = Var([1,2])
x3 = Var([4,5])

x1.assign()
x1.assign()
x1.assign()
x1.assign()

def preprcess_cells(variables):
    #Here we want every neighbor to be fixed
    print("Hello")
        
def get_sudoku_cells(v: Cell):
    print("hell")

def solution_exsists(main_var: Cell, already_tried: list):
    if len(main_var.domain) == len(already_tried):
        return False
    
def constrain(remove_element, domain2: list):
    if remove_element in domain2: 
        domain2.remove(remove_element)

        if len(domain2) == 0: 
            return False
        else:
            return True

def check_constraints(v1: Cell, v2_list: list): 
    for v2 in v2_list:
        some_bool = constrain(v1.assignment, v2.domain)
        
        if (some_bool == False):
            return False

def foward_checking(variables): 
    i = 0
    already_tried = []
    main_var = variables[0]

    while (solution_exsists(main_var)):
        curr_var = variables[i]
        var_list = get_sudoku_cells(curr_var)

        curr_var.assign() 
        if (check_constraints(curr_var, var_list)): 
            i+=1
        else:
            #Call fixNeighbors
            if (curr_var == main_var):
                already_tried.append(curr_var.assignment)

def run_foward_check(sudoku_game: Sudoku):
    main_board = sudoku_game.return_board()
    main_board.fixAll
