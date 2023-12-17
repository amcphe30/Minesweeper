from array import *
import random

rows = 10
columns = 10
num_of_mines = rows*columns*0.1
game_over = False
num_mines_left = num_of_mines

grid_vals = []
grid_bools = []

# -1 mine, otherwise num of mines around

def init_grid():
    for each in range(rows):
        row_vals = []
        row_bools = []
        for each in range(columns):
            row_vals.append(-1)
            row_bools.append(True)
        grid_vals.append(row_vals)
        grid_bools.append(row_bools)

def init_mines():
    init_grid()
    min = 1
    max = rows * columns
    mines = []
    while len(mines) < num_of_mines:
        rand = random.randint(min, max)
        if rand not in mines:
            mines.append(rand)
    for r in range(rows):
        for c in range(columns):
            if r * 5 + c + 1 in mines:
                grid_vals[r][c] = -2
    for r in range(rows):
        for c in range(columns):
            grid_vals[r][c] = get_num_around(r, c)

def get_num_around(row, column):
    if grid_vals[row][column] == -2:
        return -2
    total = 0
    posR = [row - 1, row, row + 1]
    posC = [column - 1, column, column + 1]
    for r in posR:
        for c in posC:
            if r >= 0 and r < rows and c >= 0 and c < columns:
                if grid_vals[r][c] == -2:
                    total += 1
                
                
    return total

def print_mines():
    for row in grid_vals:
        for element in row:
            print(element, end=" ")
        print() 

def get_mines():
    return grid_vals

def is_covered(r, c):
    return grid_bools[r][c]

def dig(r, c):
   if grid_bools[r][c]:
    grid_bools[r][c] = False
    if grid_vals[r][c] == -2:
        print("game over")
    elif (grid_vals[r][c] == 0):
        posR = [r - 1, r, r + 1]
        posC = [c - 1, c, c + 1]
        for r in posR:
            for c in posC:
                if r >= 0 and r < rows and c >= 0 and c < columns:
                    dig(r, c)
       



init_mines()
print_mines()