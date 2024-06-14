from collections import deque
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    def bfs(maze, start, color):
        row_len, col_len = len(maze), len(maze[0])
        # next col, prev col, next row, prev row
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # queue: (tup, lst)
        queue = deque( [(start)] )
        visited = set([start])
        ans = 0
        original_color = maze[sr][sc]
        maze[sr][sc] = color
        while queue:
            (cur_row, cur_col) = queue.popleft()
            
            for row, col in directions:
                new_row , new_col = cur_row + row, cur_col + col
                if (0 <= new_row < row_len) and (0 <= new_col < col_len) and ((new_row, new_col) not in visited) and maze[new_row][new_col] == original_color:
                    queue.append( (new_row, new_col) )
                    visited.add((new_row, new_col))
                    #print(new_row, new_col)
                    maze[new_row][new_col] = color
        return maze
    return bfs(image, (sr,sc), color)
print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))