def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    # m rows, n cols
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    grid = obstacleGrid

    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = -1
    grid[0][0] = 1
    # first row 1
    for i in range(1, n):
        if grid[0][i] == -1:
            grid[0][i] = grid[0][i - 1]
    # first col 1
    for i in range(1, m):
        if grid[i][0] == -1:
            grid[i][0] = grid[i - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == -1:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]







print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))