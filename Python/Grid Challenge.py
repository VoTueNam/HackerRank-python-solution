def gridChallenge(grid):
    
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))
    print(grid)
    for i in range(len(grid)-1):
        for y in range(len(grid[i])):
            
            if grid[i][y] > grid[i+1][y]:
                print(grid[i][y], grid[i+1][y])
                return "NO"
    return "YES"

s = ["mpxz","abcd","wlmf"]

print(gridChallenge(s))