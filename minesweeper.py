from array import *
import random

rows = 5
columns = 5
num_of_mines = 5
game_over = False
num_mines_left = num_of_mines

grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
# 0 covered no mine, 1 covered mine, 2 uncovered sand, 3 uncovered mine

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
                grid[r][c] = 1

def print_mines():
    for row in grid:
        for element in row:
            print(element, end=" ")
        print() 

def get_mines():
    return grid

def dig(r, c):
   print("pressed at (" + str(r) + "," + str(c) + ")")
   if grid[r][c] == 1:
       grid[r][c] = 3
       print("game over")
   else:
       grid[r][c] = 2
       print("no bomb")

init_mines()
print_mines()
