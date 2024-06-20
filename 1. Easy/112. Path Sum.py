class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:

    def path_sum(root: TreeNode, cur_sum):
        if not root:
            return False
        if cur_sum + root.val == targetSum and not(root.left or root.right):
            return True

        return path_sum(root.left, cur_sum + root.val) or path_sum(root.right, cur_sum + root.val)
    
    return path_sum(root, 0)
    pass



ch2 = TreeNode(8)
ch1 = TreeNode(4)
root = TreeNode(5, ch1, ch2)

print(hasPathSum(root, 13))