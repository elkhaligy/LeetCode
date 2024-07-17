# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete_set = set(to_delete)
        answer = []
        if self.post_order_traversal(root, to_delete_set, answer):
            answer.append(root)
        
        return answer
    
    def post_order_traversal(self, root: TreeNode, to_delete: set, answer: list[TreeNode]) -> TreeNode:
        if not root:
            return None
        root.left = self.post_order_traversal(root.left, to_delete, answer)
        root.right = self.post_order_traversal(root.right, to_delete, answer) 
        
        if root.val in to_delete:
            if root.left:
                answer.append(root.left)
            if root.right:
                answer.append(root.right)
            return None

        return root
    
#    1
#  2    3
# 4 5  6 7

sol_obj = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(sol_obj.delNodes(root, [3, 5]))