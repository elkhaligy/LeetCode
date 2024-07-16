from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Breadth-First-Search Algorithm
        # BFS Consists of 3 parts
        # A queue
        # A visited set
        # A loop on the queue
        # The algorithm itself is pretty simple

        start_node = self._find_start_node(root, startValue)
        parent_map = {} # node value: its parent reference
        path_tracker = {} # destination: (source, "Direction")
        visited_nodes = set()
        visited_nodes.add(start_node)
        self._populate_parent(root, parent_map)
        q = deque([start_node])

        while q:
            curr_node = q.popleft()

            if curr_node.val == destValue:
                return self._backtrack(curr_node, path_tracker, start_node)

            if curr_node.val in parent_map:
                parent_node = parent_map[curr_node.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    visited_nodes.add(parent_node)
                    path_tracker[parent_node] = (curr_node, "U")

            if curr_node.left and curr_node.left not in visited_nodes:
                q.append(curr_node.left)
                visited_nodes.add(curr_node.left)
                path_tracker[curr_node.left] = (curr_node, "L")

            if curr_node.right and curr_node.right not in visited_nodes:
                q.append(curr_node.right)
                visited_nodes.add(curr_node.right)
                path_tracker[curr_node.right] = (curr_node, "R")

        return ""
    
    def _find_start_node(self, root: TreeNode, startValue: int):
        if not root:
            return None

        if root.val == startValue:
            return root
        
        left_node = self._find_start_node(root.left, startValue)
        if left_node:
            return left_node
        else:
            right_node = self._find_start_node(root.right, startValue)
            return right_node
    
    def _populate_parent(self, root, parent_map):
        if not root:
            return None

        if root.left:
            parent_map[root.left.val] = root
            self._populate_parent(root.left, parent_map)
        if root.right:
            parent_map[root.right.val] = root
            self._populate_parent(root.right, parent_map)
    
    def _backtrack(self, curr_node, path_tracker, start_node):
        path = []
        for key, val in path_tracker.items():
            print(f"dest: {key.val}, src{val[0].val}, dir{val[1]}")

        while curr_node != start_node:
            path.append(path_tracker[curr_node][1])
            curr_node = path_tracker[curr_node][0]
        
        path = path[::-1]
        return "".join(path)



sol_obj = Solution()

#    1
#  2   3
# 4 5 6 7
root = TreeNode(1, TreeNode(2,TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(sol_obj.getDirections(root, 2, 3))