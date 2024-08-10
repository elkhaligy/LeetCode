from collections import deque
def regionsBySlashes(grid: list[str]) -> int:
    # START converting the small grid into a bigger one
    n = len(grid) 
        # It is nxn, each 1x1 grid to be 3x3
        # nxn grid contains nxn 1x1 grids, each one will be 3x3
        # so we will have nxn 3x3 grids which is nx3 x nx3 grid
    expanded = [[0 for _ in range(n*3)] for _ in range(n * 3)]
    new_n = n * 3

    # FILL the expanded grid with the values needed
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ' ':
                continue
            elif grid[i][j] == '/':
                # Do the following filling
                # 0 0 1
                # 0 1 0
                # 1 0 0
                expanded[i * 3][j * 3 + 2]     = 1
                expanded[i * 3 + 1][j * 3 + 1] = 1
                expanded[i * 3 + 2][j * 3]     = 1
            elif grid[i][j] == '\\':
                # Do the following filling
                # 1 0 0
                # 0 1 0
                # 0 0 1
                expanded[i * 3][j * 3]         = 1
                expanded[i * 3 + 1][j * 3 + 1] = 1
                expanded[i * 3 + 2][j * 3 + 2] = 1
    ## print(expanded)
    # APPLY flood fill algorithm, implemented with BFS
    new_areas = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Go up, Go down, Go right, Go left
    for i in range(new_n):
        for j in range(new_n):
            if expanded[i][j] == 0: # If the cell survived the flood then it must be a new area
                new_areas += 1
                flood_it(expanded, i, j, directions)
    
    return new_areas

# Floodfill algorithm is just a BFS that takes a grid and cell indices, it visites the cell and its neighbors and change their value
def flood_it(expanded: list[list[int]], i: int, j: int, directions: list[int]) -> None:
    queue = deque([(i, j)])
    expanded[i][j] = 1
    n = len(expanded)

    while queue:
        current_cell = queue.popleft()
        for direction in directions:
            new_row = current_cell[0] + direction[0]
            new_col = current_cell[1] + direction[1]
            # Only visit the new cell if it is valid i.e row and col are not out of bound and if it is unvisited before i.e its value is 0
            # When you visit the new cell, change its value to 1 to mark it as visited
            if (0 <= new_row < n and 0 <= new_col < n) and expanded[new_row][new_col] == 0:
                expanded[new_row][new_col] = 1
                queue.append((new_row, new_col))
            
print(regionsBySlashes(grid = [" /","/ "]))
# [[0, 0, 1, 1, 0, 0], 
# [0, 1, 0, 0, 1, 0], 
# [1, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 1], 
# [0, 1, 0, 0, 1, 0], 
# [0, 0, 1, 1, 0, 0]]

# [[0, 0, 0, 0, 0, 1], 
# [0, 0, 0, 0, 1, 0], 
# [0, 0, 0, 1, 0, 0], 
# [0, 0, 1, 0, 0, 0], 
# [0, 1, 0, 0, 0, 0], 
# [1, 0, 0, 0, 0, 0]]

# [[1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 0], 
# [1, 1, 1, 1, 0, 0], 
# [1, 1, 1, 0, 0, 0], 
# [1, 1, 0, 0, 0, 0], 
# [1, 0, 0, 0, 0, 0]]