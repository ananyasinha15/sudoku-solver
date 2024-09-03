import numpy as np

# The grid below is used to hold the values for our sudoku puzzle.
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def possible(x,y,n):
    # Checking column if n exists
    for i in range(0,9):
        if (grid[i][x] == n and i!=y): 
            return False
        
    # Checking row if n exists
    for i in range(0,9):
        if(grid[y][i] == n and i!=x):
            return False
    
    # Checking the 3x3 grid by always setting to the top left corner of the 3x3 grid and then checking the grid for n.
    box_x = x//3 # Floor division
    box_y = y//3

    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range (box_x * 3, box_x * 3 + 3):
            if grid[i][j] == n:
                return False

    return True

# Using backtracking
def solve():
    global grid
    for y in range(9):
        for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1,10):
                        if possible(x,y,n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0
                    return
    print(np.matrix(grid)) 

solve()