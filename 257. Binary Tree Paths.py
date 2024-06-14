# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root:
            return root
        ans = []
        cur = []
        def dfs(root):
            if not root:
                return
            print(root.val)
            cur.append(root.val)
            dfs(root.left)
            dfs(root.right)
            if root.left == None and root.right == None:
                ans.append(cur[:])
            cur.pop()
        dfs(root)
        ans_formatted = []
        st = ""
        for lst in ans:
            for item in lst:
                st += str(item)
                st += "->"
            ans_formatted.append(st[0:len(st) - 2])
            st = ""
        return ans_formatted
                
