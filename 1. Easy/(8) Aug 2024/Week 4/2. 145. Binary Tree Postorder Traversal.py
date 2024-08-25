# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        traversal_values = []

        def post_order(root):
            if root == None:
                return

            post_order(root.left)
            post_order(root.right)
            traversal_values.append(root.val)

        post_order(root)

        return traversal_values