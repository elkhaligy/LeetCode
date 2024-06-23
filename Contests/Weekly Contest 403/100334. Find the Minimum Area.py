def minimumArea(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ones_set = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ones_set.add((i, j))
    #print(ones_set)
    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = float('-inf'), float('-inf')

    for item in ones_set:
        max_row = max(max_row, item[0])
        max_col = max(max_col, item[1])

        min_row = min(min_row, item[0])
        min_col = min(min_col, item[1])


    return (max_row - min_row + 1) * (max_col - min_col + 1)

print(minimumArea(grid  = [[0,0],[1,0]]))
