class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

ans = []
def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return
    inorderTraversal(root.left)
    ans.append(root.val)
    inorderTraversal(root.right)



ch2 = TreeNode(8)
ch1 = TreeNode(4)
root = TreeNode(5, ch1, ch2)

print(inorderTraversal(root))
print(ans)