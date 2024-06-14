from collections import deque
def islandPerimeter(grid: list[list[int]]) -> int:
    def bfs_maze_solver(maze, start):
        row_len, col_len = len(maze), len(maze[0])
        # next col, prev col, next row, prev row
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # queue: (tup, lst)
        queue = deque( [(start)] )
        visited = set([start])
        ans = 0
        while queue:
            (cur_row, cur_col) = queue.popleft()
            if grid[cur_row][cur_col] == 1:
                for row, col in directions:
                    test_row, test_col = cur_row + row, cur_col + col
                    if test_row < 0 or test_row > row_len - 1:
                        ans += 1
                        continue
                    if test_col < 0 or test_col > col_len - 1:
                        ans += 1
                        continue
                    if maze[test_row][test_col] != 1:
                        ans += 1
                        #continue
            for row, col in directions:
                new_row , new_col = cur_row + row, cur_col + col
                if (0 <= new_row < row_len) and (0 <= new_col < col_len) and ((new_row, new_col) not in visited):
                    queue.append( (new_row, new_col) )
                    visited.add((new_row, new_col))
                    #print(new_row, new_col)
        return ans
    return bfs_maze_solver(grid, (0,0))
print(islandPerimeter(grid = [[0,0,1]]))