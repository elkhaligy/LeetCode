# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        self.dfs(root, distance)
        return self.result
    
    def dfs(self, root: TreeNode, distance: int) -> list[int]:
        if not root:
            result = [0] * (distance + 1)
            return result
        if root.left == None and root.right == None:
            result = [0] * (distance + 1)
            result[1] += 1
            return result
        
        left = self.dfs(root.left, distance)
        right = self.dfs(root.right, distance)

        for l in range(1, distance + 1):
            for r in range(distance, 0, -1):
                if l + r <= distance:
                    result += left[l] * right[r]

        result = [0] * (distance + 1)
        for i in range(distance - 1, 0, -1):
            result[i + 1] = left[i] + right[i]
        
        return result