# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst_On2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        self.inorder_traversal = []
        self.inorder(root)
        self.replace(root)
        return root
        
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder_traversal.append(root.val)
        self.inorder(root.right)
        
    def replace(self, root):
        if root is None:
            return
        self.replace(root.left)
        self.replace(root.right)

        replacement_val = 0
        for num in self.inorder_traversal[::-1]:
            if num > root.val:
                replacement_val += num
            else:
                break
        root.val += replacement_val