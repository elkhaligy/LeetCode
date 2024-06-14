def uniquePaths(m: int, n: int) -> int:
    # m rows, n cols
    grid = [[0 for _ in range(n)] for _ in range(m)]
    # first row 1
    for i in range(n):
        grid[0][i] = 1
    # first col 1
    for i in range(m):
        grid[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]

def uniquePaths_sol2(m: int, n: int) -> int:
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[-1]






print(uniquePaths(m = 3, n = 1))