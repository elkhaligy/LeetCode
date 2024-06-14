from collections import deque

# Graph
def bfs_graph(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # n for neighbor
        for n in graph[current_node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
    
    return traversal_order
def bfs_graph_shorted_path(graph, start, target):
    # queue (str, lst)
    queue = deque( [(start, [start])] )
    # visited set(str)
    visited = set([start])

    while queue:
        current_node, path = queue.popleft()
        if current_node == target:
            return path
        for n in graph[current_node]:
            if n not in visited:
                queue.append((n, path + [n]))
                visited.add(n)

    return None
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
# -- bfs_graph --
# start_node = "A"
# traversal_order = bfs_graph(graph, start_node)
# print(traversal_order)

# -- bfs_graph_shorted_path --
# start = "A"
# end = "E"
# print(bfs_graph_shorted_path(graph, start, end))

# ----------------------------------------------------------------------------------
# Tree
class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root: TreeNode) -> list[int]:
    queue = deque([root])
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        
        
    return traversal_order

def bfs_tree_levels(root: TreeNode) -> list[list[int]]:
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
        
    return result
# Constructing a simple binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# print(bfs_tree_levels(root))

# ---------------------------------------------------------------------------
# Matrix
def bfs_maze_solver(maze, start, end):
    row_len, col_len = len(maze), len(maze[0])
    # next col, prev col, next row, prev row
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # queue: (tup, lst)
    queue = deque( [(start, [start])] )
    visited = set([start])

    while queue:
        (cur_row, cur_col) , path = queue.popleft()

        if (cur_row, cur_col) == end:
            return path
        for row, col in directions:
            new_row , new_col = cur_row + row, cur_col + col

           

            if (0 <= new_row < row_len) and (0 <= new_col < col_len) and ((new_row, new_col) not in visited) and (maze[new_row][new_col] == 0):
                queue.append( ((new_row, new_col), path + [(new_row, new_col)]) )
                visited.add((new_row, new_col))

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (0, 4)
print(bfs_maze_solver(maze, start, end))
