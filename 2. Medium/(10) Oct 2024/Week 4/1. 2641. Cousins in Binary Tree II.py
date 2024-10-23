from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        # Handle the case where root might be a pointer to NULL
        if root == None:
            return None
        
        queue = deque([root])
        levels_sum = []

        # Obtain each level sum in a binary tree
        # BFS
        while queue:
            curr_sum = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            levels_sum.append(curr_sum)
        
        # Traverse the tree using BFS and update each node value with its own level sum minus sibling sum
        # BFS
        queue = deque([root])
        # Index used to access level sum
        index = 1
        root.val = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                sibling_sum = 0
                if curr_node.left:
                    sibling_sum += curr_node.left.val
                if curr_node.right:
                    sibling_sum += curr_node.right.val

                if curr_node.left:
                    curr_node.left.val = levels_sum[index] - sibling_sum
                    queue.append(curr_node.left)
                if curr_node.right:
                    curr_node.right.val = levels_sum[index] - sibling_sum
                    queue.append(curr_node.right)
            index += 1

        return root
