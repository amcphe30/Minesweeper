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
# 0 covered no mine, 1 mine, 2 uncovered no mine

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

def hit(r, c):
    if grid[r][c] == 1:
        game_over = True
        print("game over")
    else:
        grid[r][c] = 2
        print_mines()

def click(x, y):
    print("pressed at (" + str(x) + "," + str(y) + ")")

init_mines()
print_mines()
