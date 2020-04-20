
def find_empty(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        return (i, j) #row, col


def valid(grid, num, pos):
  #Check row
  for i in range(len(grid[0])):
    if grid[pos[0]][i] == num and pos[1]  != i:
      return False

  #Check col
  for i in range(len(grid)):
    if grid[i][pos[1]] == num and pos[0] != i:
      return False

  #Check smal Square
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_x*3, box_x*3 +3):
      if grid[i][j] == num and (i,j) != pos:
        False
  
  return True


def solve(grid):
  
  find = find_empty(grid)
  if not find:
    return True
  else:
    row, col = find

  for i in range(1,10):
    if valid(grid, i, (row, col)):
      grid[row][col] = i
      if solve(grid):
        return True
      grid[row][col] = 0

  return False