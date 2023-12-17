from array import *
import random

rows = 5
columns = 5
num_of_mines = 5
game_over = False
num_mines_left = num_of_mines

grid = [[-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1]]
num_around = [[-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1]]
# -1 covered no mine, -2 covered mine, -3 uncovered mine, otherwise num of mines around

def init_mines():
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
                grid[r][c] = -2

def get_num_around(row, column):
    if grid[row][column] == -2 or grid[row][column] == -3:
        return grid[row][column]
    total = 0
    posR = [row - 1, row, row + 1]
    posC = [column - 1, column, column + 1]
    for r in posR:
        for c in posC:
            if r >= 0 and r < rows and c >= 0 and c < columns:
                if grid[r][c] == -2 or grid[r][c] == -3:
                    total += 1
                
    return total

def print_mines():
    for row in grid:
        for element in row:
            print(element, end=" ")
        print() 

def get_mines():
    return grid

def dig(r, c):
   print("pressed at (" + str(r) + "," + str(c) + ")")
   if grid[r][c] == -2:
       grid[r][c] = -3
       print("game over")
   else:
       grid[r][c] = get_num_around(r, c)
       print("safe, " + str(grid[r][c]) + " bombs around")



init_mines()
print_mines()

for r in range(rows):
        for c in range(columns):
            num_around[r][c] = get_num_around(r, c)

for row in num_around:
        for element in row:
            print(element, end=" ")
        print() 