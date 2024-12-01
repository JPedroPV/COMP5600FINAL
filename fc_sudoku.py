import random 
from cell import Cell
from sudoku import Sudoku
import csv

# class Var:
#     def __init__(self, domain):
#         """
#         Initializes the DomainAssignment class.
#         :param assignment: An integer value for the assignment.
#         :param domain: A list of values representing the domain.
#         """
#         self.assignment = domain[0] # Integer assignment
#         self.domain = domain if domain is not None else []
#         self.already_chosen = []
#         self.assigned = False

#     def assign(self):
#         assignment_not_found = True
#         i = 0
#         while (assignment_not_found):
#             if not self.domain:
#                 raise ValueError("Can't take from an empty domain")
#             curr_number = random.choice(self.domain)
        
#             if curr_number not in self.already_chosen: 
#                 self.already_chosen.append(curr_number)
#                 self.assignment = curr_number
#                 self.assigned = True
#                 assignment_not_found = False
#                 print("Assignment is: ", self.assignment)

#             else: 
#                 assignment_not_found = True
#                 i+=1
#                 if (i == len(self.domain)): 
#                     print("All Variables have been assigned -- nothing assigned")
#                     return None
        
def get_related_cells(v: Cell, sodoku_game: Sudoku):
    row, col = v.location[0], v.location[1]
    related_cells = sodoku_game.getNeighbors(row, col)
    return related_cells

def solution_exsists(main_var: Cell, already_tried: list):
    if len(main_var.domain) == len(already_tried):
        return False
    else:
        return True
    
def constrain(remove_element, domain2: list):
    if remove_element in domain2: 
        domain2.remove(remove_element)

        if len(domain2) == 0: 
            return False
        else:
            return True

def check_constraints(v1: Cell, v2_list: list, soduku_game: Sudoku): 
    # for v2 in v2_list:
    list_of_original_domains = []

    for i in range(len(v2_list)):
        v2 = v2_list[i]
        list_of_original_domains.append(v2.domain.copy())
        some_bool = constrain(v1.assignment, v2.domain)

        if (some_bool == False):
            v1.assignment = 0

            for j in range(len(list_of_original_domains)):
                v2_list[j].domain = list_of_original_domains[j]

            return False
        
    return True

def foward_checking(variables: list, soduku_game: Sudoku): 
    i = 0
    already_tried = []
    main_var = variables[0]

    while (solution_exsists(main_var, already_tried)):
        
        curr_var = variables[i]

        if (curr_var.location == (1,0)):
            print("Wait")

        var_list = get_related_cells(curr_var, soduku_game)
        backtrack_signal = curr_var.assign_fc()

        if (check_constraints(curr_var, var_list, soduku_game)): 
            i+=1
            
            if i == len(variables):
                print("Were Done -- finished Board")
                # soduku_game.printBoard()
                break
        else:
            #Call fixNeighbors
            if (curr_var == main_var):
                already_tried.append(curr_var.assignment)
            
            if (backtrack_signal == True):
                i-=1
                continue

def get_test_boards(file_in):
    data = []
    solution = []
    with open(rf"{file_in}", mode= 'r', newline='') as csvFile:
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
    return boards

def run_foward_check(soduku_game: Sudoku):
    soduku_game.fixAll()
    soduku_game.printBoard()

    variables = soduku_game.get_all_unassigned()  
    foward_checking(variables, soduku_game)
    soduku_game.printBoard()
        
file = "sudokuMini.csv"
boards = get_test_boards(file)

work = boards[0]
run_foward_check(work)