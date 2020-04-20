from functions import find_empty
from functions import valid
from functions import solve


sudoku = [
    [0, 9, 0, 3, 6, 0, 1, 0, 4],
    [0, 7, 5, 0, 0, 2, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 3, 4, 8, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 2, 5, 4, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 8, 0, 0, 6, 3, 0],
    [6, 0, 4, 0, 3, 1, 0, 2, 0],
]
def print_sudoku(grid):
  for i in range(len(grid)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - - - ")
    for j in range(len(grid[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end=" ")
      if j == 8: 
        print(grid[i][j])
      else:
        print(grid[i][j], end= " ")

print_sudoku(sudoku)
solve(sudoku)
print("________________________")
print_sudoku(sudoku)


