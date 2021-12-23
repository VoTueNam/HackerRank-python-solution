import math

def printGrid(grid):
     for i in grid:
          for y in i:
               print(y,end="")
          print("")


def replain(i,j,grid):
     grid[i][j] = "."
     if not i-1 < 0:
          grid[i-1][j] = "."
     if not j-1 < 0:
          grid[i][j-1] = "."
     if i+1 <= len(grid)-1:
          grid[i+1][j] = "."
     if j+1 <= len(grid[i])-1:
          grid[i][j+1] = "."
     return grid


def bomberMan(n, grid):
     if n == 3:
          n -=1
     if n == 0:
          return grid
     indices = []
     for i in grid:
          indices.append([i for i, x in enumerate(i) if x == "O"])

     grid = [
     ["O","O","O","O","O","O","O"],
     ["O","O","O","O","O","O","O"],
     ["O","O","O","O","O","O","O"],
     ["O","O","O","O","O","O","O"],
     ["O","O","O","O","O","O","O"],
     ["O","O","O","O","O","O","O"]]
     
     if n == 1:
          for i in range(len(grid)):
               "".join(grid[i])
          return grid
     
     for i in range(len(indices)):
          if indices:
               for c in indices[i]:
                    grid = replain(i,c,grid)
     for i in range(len(grid)):
          grid[i]="".join(grid[i])
     if n == 2:
          return grid
     return bomberMan(n-3,grid)



grid = [
".......",
"...O.O.",
'....O..',
'..O....',
'OO...OO',
'OO.O...']

n = 5

printGrid(grid)
print("after\n")

# grid = [
# ["O","O","O","O","O","O","O"],
# ["O","O","O","O","O","O","O"],
# ["O","O","O","O","O","O","O"],
# ["O","O","O","O","O","O","O"],
# ["O","O","O","O","O","O","O"],
# ["O","O","O","O","O","O","O"]]

grid = bomberMan(4,grid)
printGrid(grid)