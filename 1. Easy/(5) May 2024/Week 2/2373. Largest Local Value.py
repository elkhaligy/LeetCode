def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    maxLocal = [[0 for _ in range(n-2)] for _ in range(n-2)]

    for i in range(len(maxLocal)):
        for j in range(len(maxLocal)):
            for k in range(i, 3 + i):
                for f in range(j, 3 + j):
                    #print(grid[k][f], end=' ')
                    maxLocal[i][j] = max(grid[k][f], maxLocal[i][j])
                #print()
            #print()

    return maxLocal
def find_max(grid, row, col):
    ans = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            ans = max(ans, grid[i][j])
    return ans

def largestLocal_Sol2(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    maxLocal = [[0 for _ in range(n-2)] for _ in range(n-2)]

    for i in range(len(maxLocal)):
        for j in range(len(maxLocal)):
            maxLocal[i][j] = find_max(grid, i, j)

    return maxLocal
print(largestLocal_Sol2(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
