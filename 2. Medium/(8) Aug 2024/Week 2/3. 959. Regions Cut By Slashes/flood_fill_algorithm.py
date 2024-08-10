from collections import deque

def bfs_flood_fill(grid, start_x, start_y, target_color, replacement_color):
    if grid[start_x][start_y] != target_color:
        return
    
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    
    queue = deque([(start_x, start_y)])

    grid[start_x][start_y] = replacement_color
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == target_color:
                grid[nx][ny] = replacement_color
                queue.append((nx, ny))

# Example usage:
grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

bfs_flood_fill(grid, 0, 0, 1, 2)
print(grid)