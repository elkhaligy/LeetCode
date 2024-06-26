# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        inorder_traversal = []
        self.inorder(root, inorder_traversal)
        return self.create_bst(inorder_traversal, 0, len(inorder_traversal) - 1)
    def inorder(self, root: TreeNode, inorder_traversal: list[int]):
        if root is None:
            return
        self.inorder(root.left, inorder_traversal)
        inorder_traversal.append(root.val)
        self.inorder(root.right, inorder_traversal)

    def create_bst(self, inorder_traversal: list[int], start: int, end: int):
        if start > end:
            return None

        mid = (start + end) // 2
        left_subtree = self.create_bst(inorder_traversal, start, mid - 1)
        right_subtree = self.create_bst(inorder_traversal, mid + 1, end)

        node = TreeNode(inorder_traversal[mid], left_subtree, right_subtree)

        return node