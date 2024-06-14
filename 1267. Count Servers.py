def countServers(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    ans = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    row_sums = [sum(row) for row in grid]
    transposed_matrix = list(zip(*grid))
    col_sums = [sum(col) for col in transposed_matrix]

    for i in range(rows):
        if sum(grid[i]) >= 2:
            for j in range(cols):
                visited[i][j] = True if grid[i][j] == 1 else False
    transposed_visited = list(zip(*visited))
    visited_sum = [sum(col) for col in transposed_visited]
    #print(visited_sum)
    #print(visited)
    #print(col_sums)
    #print(row_sums)
    for i in row_sums:
        if i >= 2:
            ans += i
    z = 0
    for i in col_sums:
        if i >= 2:
            ans += i
            ans -= visited_sum[z]
        z += 1
    return ans
    


print(countServers([[1,1,0,0],
                    [0,0,1,0],
                    [0,0,1,0],
                    [0,0,0,1]]))