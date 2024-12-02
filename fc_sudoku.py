import random 
from cell import Cell
from sudoku import Sudoku
import csv

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

        if (check_constraints(curr_var, var_list, soduku_game) and backtrack_signal == False): 
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
                curr_var.assignment = 0
                curr_var.already_chosen = []
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

    variables2 = soduku_game.get_all_unassigned()
    for var in variables2:
        soduku_game.fixDomain(var.location[0], var.location[1])
        print(var.domain, " ", var.location)

    print("STOP")

        
file = "sudokuMini.csv"
boards = get_test_boards(file)

work = boards[0]
run_foward_check(work)